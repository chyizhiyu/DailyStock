from __future__ import annotations

import json
import logging
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pandas as pd

from dailystock.config import Settings, load_settings, project_root
from dailystock.data_sources.akshare import AkShareDataProvider
from dailystock.data_sources.base import DataProvider
from dailystock.data_sources.local_db import LocalDbDataProvider
from dailystock.data_sources.sample import SampleDataProvider
from dailystock.data_sources.tushare import TushareDataProvider
from dailystock.executor.futu_client import FutuClient
from dailystock.executor.step5_futu_executor import run_futu_executor
from dailystock.filters.step1_fetch_meta import fetch_meta
from dailystock.filters.step2_hard_filters import (
    run_hard_filters,
    run_non_financial_hard_filters,
)
from dailystock.filters.step3_financial_quality import run_financial_quality_filters
from dailystock.filters.step4_valuation import run_valuation_filters
from dailystock.models.screening import (
    ExecutionFrameResult,
    FilterFrameResult,
    PipelineRequest,
    PipelineResult,
    StepSummary,
)
from dailystock.reports.dashboard import build_dashboard
from dailystock.reports.exporters import export_dataframe, export_json

logger = logging.getLogger(__name__)


class DailyStockPipeline:
    def __init__(
        self,
        settings: Settings | None = None,
        provider: DataProvider | None = None,
    ) -> None:
        self.settings = settings or load_settings()
        self.provider = provider or self._build_provider(self.settings)

    def run(self, request: PipelineRequest) -> PipelineResult:
        effective_dry_run = self._effective_dry_run(request)
        if effective_dry_run != request.dry_run:
            logger.info(
                "[Pipeline Safety] Requested live execution was downgraded to dry-run by config."
            )
        request = request.model_copy(update={"dry_run": effective_dry_run})
        run_dir = self._run_dir(request)
        steps: list[StepSummary] = []
        artifacts: list[str] = []

        meta, summary = self._time_frame_step(
            "step1_fetch_meta",
            input_count=0,
            work=lambda: fetch_meta(self.provider, as_of=request.as_of, markets=request.markets),
        )
        self._export_frame(run_dir, "step1_meta", meta, summary, artifacts)
        _log_step_summary("Step 1 Fetch Meta", summary)
        steps.append(summary)

        codes = meta["code"].tolist()
        daily_bars = _time_data_load(
            "Daily Bars",
            len(codes),
            lambda: self.provider.load_daily_bars(codes, as_of=request.as_of, lookback_days=30),
        )
        pre_hard_result = _time_data_load(
            "Step 2 Pre-Financial Hard Filter",
            len(meta),
            lambda: run_non_financial_hard_filters(
                meta,
                daily_bars,
                as_of=request.as_of,
                settings=self.settings.hard_filters,
            ),
            output_count=lambda result: len(result.candidates),
        )
        hard_financial_codes = pre_hard_result.candidates["code"].tolist()
        hard_financials = _time_data_load(
            "Hard Financials",
            len(hard_financial_codes),
            lambda: self.provider.load_financials(hard_financial_codes, as_of=request.as_of),
        )
        hard_result, summary = self._time_filter_step(
            "step2_hard_filters",
            input_count=len(meta),
            work=lambda: run_hard_filters(
                meta,
                daily_bars,
                hard_financials,
                as_of=request.as_of,
                settings=self.settings.hard_filters,
            ),
        )
        self._export_filter_result(run_dir, "step2_hard_filters", hard_result, summary, artifacts)
        _log_step_summary("Step 2 Hard Filter", summary)
        steps.append(summary)

        quality_codes = hard_result.candidates["code"].tolist()
        quality_financials = _time_data_load(
            "Quality Financials",
            len(quality_codes),
            lambda: self.provider.load_financials(quality_codes, as_of=request.as_of),
        )
        quality_result, summary = self._time_filter_step(
            "step3_financial_quality",
            input_count=len(hard_result.candidates),
            work=lambda: run_financial_quality_filters(
                hard_result.candidates,
                quality_financials,
                self.settings.quality_filters,
            ),
        )
        self._export_filter_result(
            run_dir,
            "step3_financial_quality",
            quality_result,
            summary,
            artifacts,
        )
        _log_step_summary("Step 3 Financial Quality", summary)
        steps.append(summary)

        valuation_history = self.provider.load_valuation_history(
            codes=None,
            as_of=request.as_of,
            lookback_years=self.settings.valuation_filters.lookback_years,
        )
        valuation_codes = quality_result.candidates["code"].tolist()
        dividends = _time_data_load(
            "Dividends",
            len(valuation_codes),
            lambda: self.provider.load_dividends(valuation_codes, as_of=request.as_of),
        )
        free_cash_flow = _time_data_load(
            "Free Cash Flow",
            len(valuation_codes),
            lambda: self.provider.load_free_cash_flow(valuation_codes, as_of=request.as_of),
        )
        valuation_result, summary = self._time_filter_step(
            "step4_valuation",
            input_count=len(quality_result.candidates),
            work=lambda: run_valuation_filters(
                quality_result.candidates,
                valuation_history,
                dividends,
                free_cash_flow,
                self.settings.valuation_filters,
            ),
        )
        self._export_filter_result(run_dir, "step4_valuation", valuation_result, summary, artifacts)
        _log_step_summary("Step 4 Valuation", summary)
        steps.append(summary)

        client = FutuClient(settings=self.settings.futu, dry_run=request.dry_run)
        execution_result, summary = self._time_execution_step(
            "step5_futu_executor",
            input_count=len(valuation_result.candidates),
            work=lambda: run_futu_executor(
                valuation_result.candidates,
                client=client,
                dry_run=request.dry_run,
                max_spread_bps=self.settings.futu.max_spread_bps,
                max_order_notional=self.settings.futu.max_order_notional,
                max_position_pct=self.settings.futu.max_position_pct,
            ),
        )
        self._export_execution_result(run_dir, execution_result, summary, artifacts)
        _log_step_summary("Step 5 Futu Executor", summary)
        steps.append(summary)

        dashboard = build_dashboard(
            request=request,
            steps=steps,
            candidates=valuation_result.candidates,
            execution_plan=execution_result.execution_plan,
        )
        dashboard_path = run_dir / "dashboard.md"
        dashboard_path.write_text(dashboard, encoding="utf-8")
        artifacts.append(str(dashboard_path))

        result = PipelineResult(
            request=request,
            final_candidates=_records(valuation_result.candidates),
            steps=steps,
            execution_plan=_records(execution_result.execution_plan),
            artifacts=artifacts + [str(run_dir / "result.json")],
        )
        export_json(result.model_dump(mode="json"), run_dir / "result.json")
        return result

    @staticmethod
    def _build_provider(settings: Settings) -> DataProvider:
        source = settings.app.data_source.lower()
        if source == "sample":
            data_dir = _resolve_path(settings.app.sample_data_dir)
            return SampleDataProvider(data_dir)
        if source == "akshare":
            return AkShareDataProvider(
                cache_dir=_resolve_path(settings.app.akshare_cache_dir),
                seed_dir=_resolve_path(settings.app.akshare_seed_dir),
            )
        if source == "tushare":
            return TushareDataProvider()
        if source in {"local_db", "local-db", "duckdb", "sqlite"}:
            return LocalDbDataProvider()
        raise ValueError(f"Unsupported data source: {settings.app.data_source}")

    def _effective_dry_run(self, request: PipelineRequest) -> bool:
        return (
            request.dry_run
            or self.settings.futu.dry_run
            or not self.settings.futu.enable_live_trading
        )

    def _run_dir(self, request: PipelineRequest) -> Path:
        output_dir = _resolve_path(self.settings.app.output_dir)
        run_dir = output_dir / request.as_of.strftime("%Y%m%d")
        run_dir.mkdir(parents=True, exist_ok=True)
        return run_dir

    @staticmethod
    def _time_frame_step(
        name: str,
        input_count: int,
        work: Callable[[], pd.DataFrame],
    ) -> tuple[pd.DataFrame, StepSummary]:
        started = time.perf_counter()
        frame = work()
        summary = StepSummary(
            name=name,
            input_count=input_count,
            output_count=len(frame),
            elapsed_seconds=time.perf_counter() - started,
        )
        return frame, summary

    @staticmethod
    def _time_filter_step(
        name: str,
        input_count: int,
        work: Callable[[], FilterFrameResult],
    ) -> tuple[FilterFrameResult, StepSummary]:
        started = time.perf_counter()
        result = work()
        summary = StepSummary(
            name=name,
            input_count=input_count,
            output_count=len(result.candidates),
            elapsed_seconds=time.perf_counter() - started,
            rejection_counts=result.rejection_counts,
        )
        return result, summary

    @staticmethod
    def _time_execution_step(
        name: str,
        input_count: int,
        work: Callable[[], ExecutionFrameResult],
    ) -> tuple[ExecutionFrameResult, StepSummary]:
        started = time.perf_counter()
        result = work()
        action = result.execution_plan.get("action", pd.Series(dtype=str))
        skipped = result.execution_plan.loc[action.isin(["SKIP", "BLOCKED"])]
        summary = StepSummary(
            name=name,
            input_count=input_count,
            output_count=len(result.execution_plan),
            elapsed_seconds=time.perf_counter() - started,
            rejection_counts=skipped["decision_reason"].value_counts().to_dict()
            if not skipped.empty
            else {},
        )
        return result, summary

    @staticmethod
    def _export_frame(
        run_dir: Path,
        name: str,
        frame: pd.DataFrame,
        summary: StepSummary,
        artifacts: list[str],
    ) -> None:
        path = export_dataframe(frame, run_dir / f"{name}.csv")
        summary.artifacts.append(str(path))
        artifacts.append(str(path))

    def _export_filter_result(
        self,
        run_dir: Path,
        name: str,
        result: FilterFrameResult,
        summary: StepSummary,
        artifacts: list[str],
    ) -> None:
        self._export_frame(run_dir, f"{name}_candidates", result.candidates, summary, artifacts)
        if not result.rejected.empty:
            self._export_frame(run_dir, f"{name}_rejected", result.rejected, summary, artifacts)

    def _export_execution_result(
        self,
        run_dir: Path,
        result: ExecutionFrameResult,
        summary: StepSummary,
        artifacts: list[str],
    ) -> None:
        self._export_frame(run_dir, "step5_scanned", result.scanned, summary, artifacts)
        self._export_frame(
            run_dir,
            "step5_execution_plan",
            result.execution_plan,
            summary,
            artifacts,
        )


def _resolve_path(path: str | Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return project_root() / candidate


def _records(frame: pd.DataFrame) -> list[dict[str, object]]:
    if frame.empty:
        return []
    return json.loads(frame.to_json(orient="records", date_format="iso"))


def _time_data_load(
    label: str,
    input_count: int,
    work: Callable[[], Any],
    output_count: Callable[[Any], int] | None = None,
) -> Any:
    started = time.perf_counter()
    result = work()
    elapsed = time.perf_counter() - started
    count = output_count(result) if output_count else len(result)
    logger.info(
        "[Data Load %s] Input: %s stocks, Output: %s rows, Time elapsed: %.3f s",
        label,
        input_count,
        count,
        elapsed,
    )
    return result


def _log_step_summary(label: str, summary: StepSummary) -> None:
    reclaimed = max(summary.input_count - summary.output_count, 0)
    logger.info(
        "[%s] Input: %s stocks, Output: %s stocks, Reclaimed: %s stocks, "
        "Time elapsed: %.3f s, Rejections: %s",
        label,
        summary.input_count,
        summary.output_count,
        reclaimed,
        summary.elapsed_seconds,
        summary.rejection_counts or {},
    )
