from __future__ import annotations

from collections.abc import Callable, Iterable

import pandas as pd

from dailystock.models.screening import FilterFrameResult

Rule = tuple[str, Callable[[pd.DataFrame], pd.Series]]


def require_columns(frame: pd.DataFrame, columns: Iterable[str], source: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        raise ValueError(f"{source} is missing required columns: {', '.join(missing)}")


def split_by_rules(frame: pd.DataFrame, rules: list[Rule]) -> FilterFrameResult:
    current = frame.copy()
    rejected_frames: list[pd.DataFrame] = []
    rejection_counts: dict[str, int] = {}

    for reason, keep_rule in rules:
        if current.empty:
            break
        keep = keep_rule(current).reindex(current.index).fillna(False).astype(bool)
        rejected = current.loc[~keep].copy()
        if not rejected.empty:
            rejected["rejection_reason"] = reason
            rejected_frames.append(rejected)
            rejection_counts[reason] = len(rejected)
        current = current.loc[keep].copy()

    rejected_all = (
        pd.concat(rejected_frames, ignore_index=True) if rejected_frames else pd.DataFrame()
    )
    return FilterFrameResult(
        candidates=current.reset_index(drop=True),
        rejected=rejected_all.reset_index(drop=True),
        rejection_counts=rejection_counts,
    )


def bool_series(frame: pd.DataFrame, column: str, default: bool = False) -> pd.Series:
    if column not in frame:
        return pd.Series(default, index=frame.index)
    return frame[column].fillna(default).astype(bool)
