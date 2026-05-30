from __future__ import annotations

import math

import pandas as pd


def safe_ratio(numerator: float | int | None, denominator: float | int | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return float(numerator) / float(denominator)


def annualized_cagr(
    first: float | int | None,
    last: float | int | None,
    years: int,
) -> float | None:
    if first is None or last is None or years <= 0:
        return None
    first_value = float(first)
    last_value = float(last)
    if first_value <= 0 or last_value <= 0:
        return None
    return math.pow(last_value / first_value, 1 / years) - 1


def percentile_rank_lower(value: float | int | None, history: pd.Series) -> float | None:
    if value is None:
        return None
    clean = pd.to_numeric(history, errors="coerce").dropna()
    if clean.empty:
        return None
    return float((clean < float(value)).mean())
