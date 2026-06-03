from __future__ import annotations

from datetime import date

from dailystock.config import load_settings
from dailystock.models.screening import PipelineRequest
from dailystock.pipeline import DailyStockPipeline


def test_pipeline_runs_full_sample_funnel(tmp_path) -> None:
    settings = load_settings()
    settings.app.data_source = "sample"
    settings.app.output_dir = str(tmp_path)
    request = PipelineRequest(as_of=date(2026, 5, 29), markets=["CN", "HK"], dry_run=True)

    result = DailyStockPipeline(settings=settings).run(request)

    assert {candidate["code"] for candidate in result.final_candidates} == {"CN000001", "HK00001"}
    assert [(step.name, step.input_count, step.output_count) for step in result.steps] == [
        ("step1_fetch_meta", 0, 11),
        ("step2_hard_filters", 11, 4),
        ("step3_financial_quality", 4, 3),
        ("step4_valuation", 3, 2),
        ("step5_futu_executor", 2, 2),
    ]
    step2 = next(step for step in result.steps if step.name == "step2_hard_filters")
    assert step2.rejected_market_counts == {"CN": 5, "HK": 2}
    assert step2.rejection_market_counts["risk_screen"] == {"CN": 1, "HK": 2}
    assert result.execution_plan
    assert all(plan["dry_run"] for plan in result.execution_plan)
    assert all(plan["risk_status"] == "OK" for plan in result.execution_plan)
    assert any(path.endswith("dashboard.md") for path in result.artifacts)
    assert any(path.endswith("feishu_summary.md") for path in result.artifacts)
    assert any(path.endswith("result.json") for path in result.artifacts)
    dashboard_path = next(path for path in result.artifacts if path.endswith("dashboard.md"))
    dashboard = open(dashboard_path, encoding="utf-8").read()
    assert "## Rejection Breakdown By Market" in dashboard
    assert "| step2_hard_filters | risk_screen | 1 | 2 |" in dashboard


def test_pipeline_uses_strictest_dry_run_setting(tmp_path) -> None:
    settings = load_settings()
    settings.app.data_source = "sample"
    settings.app.output_dir = str(tmp_path)
    settings.futu.dry_run = True
    settings.futu.enable_live_trading = True
    request = PipelineRequest(as_of=date(2026, 5, 29), markets=["CN", "HK"], dry_run=False)

    result = DailyStockPipeline(settings=settings).run(request)

    assert result.request.dry_run is True
    assert all(plan["dry_run"] for plan in result.execution_plan)
