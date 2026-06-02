from __future__ import annotations

from collections.abc import Mapping, Sequence

import pandas as pd

from dailystock.models.screening import PipelineRequest, StepSummary
from dailystock.reports.dashboard import _format_cell


def build_feishu_summary(
    request: PipelineRequest,
    steps: Sequence[StepSummary],
    candidates: pd.DataFrame,
    execution_plan: pd.DataFrame,
    *,
    max_rows: int = 20,
) -> str:
    """Build a compact Markdown summary that OpenClaw can paste into Feishu."""

    lines = [
        "# DailyStock Weekly Screen",
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
        lines.append(
            "| "
            + " | ".join(
                [
                    step.name,
                    str(step.input_count),
                    str(step.output_count),
                    _format_rejections(step.rejection_counts),
                    f"{step.elapsed_seconds:.3f}",
                ]
            )
            + " |"
        )

    lines.extend(["", "## Market Coverage", ""])
    lines.append(_market_coverage_table(steps, request.markets))

    lines.extend(["", "## Step 5 Decisions", ""])
    if execution_plan.empty or "action" not in execution_plan:
        lines.append("_No execution plan was produced._")
    else:
        action_counts = execution_plan["action"].fillna("UNKNOWN").value_counts().to_dict()
        reason_counts = (
            execution_plan["decision_reason"].fillna("UNKNOWN").value_counts().to_dict()
            if "decision_reason" in execution_plan
            else {}
        )
        lines.append(f"- Actions: `{_format_rejections(action_counts)}`")
        lines.append(f"- Reasons: `{_format_rejections(reason_counts)}`")

    tradable_plan = _tradable_plan(execution_plan)
    lines.extend(["", "## WATCH / BUY Candidates", ""])
    if tradable_plan.empty:
        fallback = candidates.head(max_rows)
        if fallback.empty:
            lines.append("_No candidates survived the funnel._")
        else:
            lines.append(
                "_No WATCH/BUY rows after Step 5; showing valuation survivors instead._"
            )
            lines.append(_candidate_table(fallback, max_rows=max_rows))
    else:
        lines.append(_candidate_table(tradable_plan, max_rows=max_rows))
        remaining = len(tradable_plan) - min(len(tradable_plan), max_rows)
        if remaining > 0:
            lines.append(f"\n_...and {remaining} more WATCH/BUY rows._")

    if not execution_plan.empty:
        skipped = execution_plan.loc[
            execution_plan.get("action", pd.Series(dtype=str)).isin(["SKIP", "BLOCKED"])
        ]
        if not skipped.empty:
            lines.extend(["", "## Blocked / Skipped", ""])
            lines.append(_skip_table(skipped, max_rows=max_rows))

    return "\n".join(lines) + "\n"


def _tradable_plan(execution_plan: pd.DataFrame) -> pd.DataFrame:
    if execution_plan.empty or "action" not in execution_plan:
        return pd.DataFrame()
    return execution_plan.loc[execution_plan["action"].isin(["BUY", "WATCH"])].copy()


def _candidate_table(frame: pd.DataFrame, *, max_rows: int) -> str:
    columns = [
        column
        for column in [
            "code",
            "name",
            "market",
            "industry",
            "action",
            "decision_reason",
            "pe_ttm",
            "pb",
            "roe",
            "dividend_yield",
            "fcf_yield",
            "spread_bps",
            "risk_status",
        ]
        if column in frame.columns
    ]
    return _markdown_table(frame[columns].head(max_rows))


def _skip_table(frame: pd.DataFrame, *, max_rows: int) -> str:
    columns = [
        column
        for column in ["code", "name", "market", "action", "decision_reason", "spread_bps"]
        if column in frame.columns
    ]
    return _markdown_table(frame[columns].head(max_rows))


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


def _format_rejections(values: Mapping[str, int]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in values.items()) or "-"


def _market_coverage_table(steps: Sequence[StepSummary], markets: Sequence[str]) -> str:
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
