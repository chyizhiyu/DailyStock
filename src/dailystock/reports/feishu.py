from __future__ import annotations

from collections.abc import Mapping, Sequence

import pandas as pd

from dailystock.models.screening import PipelineRequest, StepSummary

STEP_LABELS = {
    "step1_fetch_meta": "全市场",
    "step2_hard_filters": "硬过滤",
    "step3_financial_quality": "财务质量",
    "step4_valuation": "估值筛选",
}

REASON_LABELS = {
    "risk_screen": "风险标记",
    "listing_age": "上市年限",
    "liquidity": "流动性",
    "market_cap": "市值",
    "performance_floor": "业绩底线",
    "profitability": "盈利能力",
    "leverage": "杠杆",
    "cash_flow_quality": "现金流质量",
    "growth": "成长性",
    "missing_valuation_data": "估值数据缺失",
    "pe_valuation_percentile": "PE分位过高",
    "pb_valuation_percentile": "PB分位过高",
    "dividend_yield": "股息率",
    "spread_too_wide": "价差超限",
    "not_tradable": "不可交易",
}


def build_feishu_summary(
    request: PipelineRequest,
    steps: Sequence[StepSummary],
    candidates: pd.DataFrame,
    execution_plan: pd.DataFrame,
    *,
    max_rows: int = 8,
) -> str:
    """Build a short plain-text conclusion for direct Feishu delivery."""

    tradable_plan = _tradable_plan(execution_plan)
    action_counts = _action_counts(execution_plan)
    watch_count = int(action_counts.get("WATCH", 0))
    buy_count = int(action_counts.get("BUY", 0))
    selected_count = watch_count + buy_count
    hk_selected = _market_count(tradable_plan, "HK")

    if selected_count:
        conclusion = f"{selected_count}只进入观察/买入池"
    else:
        conclusion = "无股票进入观察/买入池"
    if "HK" in request.markets and hk_selected == 0:
        conclusion += "；港股无终选"

    lines = [
        f"DailyStock 扫描结论｜{request.as_of}",
        f"结论：{conclusion}。",
        f"漏斗：{_funnel_text(steps, selected_count)}",
        f"市场：{_market_progress_text(steps, tradable_plan, request.markets)}",
        "",
        "最终观察池：",
    ]
    lines.extend(_candidate_lines(tradable_plan, candidates, max_rows=max_rows))

    hk_status = _market_rejection_summary(steps, "HK")
    if "HK" in request.markets and hk_status:
        lines.extend(["", f"港股：{hk_status}"])

    risk_text = _risk_summary(request, execution_plan, action_counts)
    lines.extend(["", f"风控：{risk_text}"])
    return "\n".join(lines) + "\n"


def _tradable_plan(execution_plan: pd.DataFrame) -> pd.DataFrame:
    if execution_plan.empty or "action" not in execution_plan:
        return pd.DataFrame()
    return execution_plan.loc[execution_plan["action"].isin(["BUY", "WATCH"])].copy()


def _action_counts(execution_plan: pd.DataFrame) -> dict[str, int]:
    if execution_plan.empty or "action" not in execution_plan:
        return {}
    return {
        str(action): int(count)
        for action, count in execution_plan["action"].fillna("UNKNOWN").value_counts().items()
    }


def _funnel_text(steps: Sequence[StepSummary], selected_count: int) -> str:
    counts = [
        step.output_count
        for step in steps
        if step.name in STEP_LABELS
    ]
    counts.append(selected_count)
    return " → ".join(str(count) for count in counts)


def _market_progress_text(
    steps: Sequence[StepSummary],
    tradable_plan: pd.DataFrame,
    markets: Sequence[str],
) -> str:
    parts: list[str] = []
    for market in markets:
        counts = [
            step.output_market_counts.get(str(market), 0)
            for step in steps
            if step.name in STEP_LABELS
        ]
        counts.append(_market_count(tradable_plan, str(market)))
        parts.append(f"{market} " + "→".join(str(count) for count in counts))
    return "；".join(parts)


def _market_count(frame: pd.DataFrame, market: str) -> int:
    if frame.empty or "market" not in frame:
        return 0
    return int(frame["market"].astype(str).eq(market).sum())


def _candidate_lines(
    tradable_plan: pd.DataFrame,
    candidates: pd.DataFrame,
    *,
    max_rows: int,
) -> list[str]:
    frame = tradable_plan if not tradable_plan.empty else candidates
    if frame.empty:
        return ["无"]

    lines: list[str] = []
    for _, row in frame.head(max_rows).iterrows():
        code = str(row.get("code", "-"))
        name = str(row.get("name", "-"))
        market = str(row.get("market", "-"))
        metrics = [
            _metric("PE", row.get("pe_ttm"), multiplier=1, suffix="x"),
            _metric("ROE", row.get("roe")),
            _metric("股息", row.get("dividend_yield")),
        ]
        metric_text = "｜".join(metric for metric in metrics if metric)
        lines.append(f"- {market} {code} {name}｜{metric_text}")

    remaining = len(frame) - min(len(frame), max_rows)
    if remaining > 0:
        lines.append(f"- 另有 {remaining} 只，详见完整报告")
    return lines


def _metric(
    label: str,
    value: object,
    *,
    multiplier: float = 100,
    suffix: str = "%",
) -> str:
    numeric = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(numeric):
        return ""
    return f"{label} {float(numeric) * multiplier:.1f}{suffix}"


def _market_rejection_summary(steps: Sequence[StepSummary], market: str) -> str:
    step3 = _step(steps, "step3_financial_quality")
    step4 = _step(steps, "step4_valuation")
    if step3 is None or step4 is None:
        return ""

    before = step3.output_market_counts.get(market, 0)
    after = step4.output_market_counts.get(market, 0)
    counts: dict[str, int] = {}
    for reason, markets in step4.rejection_market_counts.items():
        count = int(markets.get(market, 0))
        if count:
            counts[reason] = count
    reasons = _format_reason_counts(counts, limit=3)
    text = f"财务筛选后{before}只，估值筛选后{after}只"
    return f"{text}；主要淘汰：{reasons}" if reasons else text


def _risk_summary(
    request: PipelineRequest,
    execution_plan: pd.DataFrame,
    action_counts: Mapping[str, int],
) -> str:
    parts = ["dry-run，仅观察，未下单" if request.dry_run else "实盘模式"]
    skipped = int(action_counts.get("SKIP", 0))
    blocked = int(action_counts.get("BLOCKED", 0))
    if skipped:
        reason_counts = (
            execution_plan.loc[execution_plan["action"].eq("SKIP"), "decision_reason"]
            .fillna("UNKNOWN")
            .value_counts()
            .to_dict()
            if "decision_reason" in execution_plan
            else {}
        )
        parts.append(f"跳过{skipped}只（{_format_reason_counts(reason_counts, limit=2)}）")
    if blocked:
        parts.append(f"风控拦截{blocked}只")
    return "；".join(parts) + "。"


def _format_reason_counts(values: Mapping[str, int], *, limit: int) -> str:
    ranked = sorted(values.items(), key=lambda item: int(item[1]), reverse=True)[:limit]
    return "、".join(
        f"{REASON_LABELS.get(str(reason), str(reason))}{int(count)}"
        for reason, count in ranked
    )


def _step(steps: Sequence[StepSummary], name: str) -> StepSummary | None:
    return next((step for step in steps if step.name == name), None)
