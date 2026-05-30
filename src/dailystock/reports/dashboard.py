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
