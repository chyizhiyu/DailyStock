from __future__ import annotations

import pandas as pd

from dailystock.models.screening import PipelineRequest, StepSummary


def build_dashboard(
    request: PipelineRequest,
    steps: list[StepSummary],
    candidates: pd.DataFrame,
    execution_plan: pd.DataFrame,
) -> str:
    lines = [
        "# DailyStock Funnel Dashboard",
        "",
        f"- As of: `{request.as_of}`",
        f"- Markets: `{','.join(request.markets)}`",
        f"- Dry run: `{request.dry_run}`",
        "",
        "## Funnel",
        "",
        "| Step | Input | Output | Rejections | Seconds |",
        "| --- | ---: | ---: | --- | ---: |",
    ]
    for step in steps:
        reasons = (
            ", ".join(f"{key}: {value}" for key, value in step.rejection_counts.items()) or "-"
        )
        lines.append(
            f"| {step.name} | {step.input_count} | {step.output_count} | {reasons} | "
            f"{step.elapsed_seconds:.3f} |"
        )

    lines.extend(["", "## Market Coverage", ""])
    lines.append(_market_coverage_table(steps, request.markets))

    rejection_breakdown = _rejection_breakdown_table(steps, request.markets)
    if rejection_breakdown:
        lines.extend(["", "## Rejection Breakdown By Market", ""])
        lines.append(rejection_breakdown)

    lines.extend(["", "## Final Candidates", ""])
    if candidates.empty:
        lines.append("_No candidates survived the valuation funnel._")
    else:
        display_cols = [
            column
            for column in [
                "code",
                "name",
                "market",
                "industry",
                "roe",
                "pe_ttm",
                "pe_percentile",
                "pb",
                "pb_percentile",
                "dividend_yield",
                "fcf_yield",
            ]
            if column in candidates.columns
        ]
        lines.append(_markdown_table(candidates[display_cols]))

    lines.extend(["", "## Execution Plan", ""])
    if execution_plan.empty:
        lines.append("_No execution plan was produced._")
    else:
        display_cols = [
            column
            for column in [
                "code",
                "action",
                "decision_reason",
                "bid",
                "ask",
                "spread_bps",
                "volume_signal",
                "tradable",
                "planned_notional",
                "planned_position_pct",
                "risk_status",
                "risk_reason",
                "dry_run",
            ]
            if column in execution_plan.columns
        ]
        lines.append(_markdown_table(execution_plan[display_cols]))

    return "\n".join(lines) + "\n"


def _markdown_table(frame: pd.DataFrame) -> str:
    if frame.empty:
        return ""
    headers = list(frame.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in frame.iterrows():
        lines.append("| " + " | ".join(_format_cell(row[column]) for column in headers) + " |")
    return "\n".join(lines)


def _format_cell(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:.4g}"
    return str(value)


def _market_coverage_table(steps: list[StepSummary], markets: list[str]) -> str:
    headers = ["Step"]
    for market in markets:
        headers.extend([f"{market} Out", f"{market} Rejected"])
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] + ["---:"] * (len(headers) - 1)) + " |",
    ]
    for step in steps:
        row = [step.name]
        for market in markets:
            row.append(str(step.output_market_counts.get(str(market), 0)))
            row.append(str(step.rejected_market_counts.get(str(market), 0)))
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def _rejection_breakdown_table(steps: list[StepSummary], markets: list[str]) -> str:
    rows: list[list[str]] = []
    for step in steps:
        reasons = step.rejection_counts.keys() or step.rejection_market_counts.keys()
        for reason in reasons:
            market_counts = step.rejection_market_counts.get(str(reason), {})
            if not market_counts:
                continue
            rows.append(
                [step.name, str(reason)]
                + [str(market_counts.get(str(market), 0)) for market in markets]
            )
    if not rows:
        return ""

    headers = ["Step", "Reason", *[str(market) for market in markets]]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---", "---"] + ["---:"] * len(markets)) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)
