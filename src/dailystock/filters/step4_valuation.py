from __future__ import annotations

import pandas as pd

from dailystock.config import ValuationFilterSettings
from dailystock.models.screening import FilterFrameResult
from dailystock.utils.metrics import percentile_rank_lower
from dailystock.utils.validation import require_columns, split_by_rules


def run_valuation_filters(
    candidates: pd.DataFrame,
    valuation_history: pd.DataFrame,
    dividends: pd.DataFrame,
    free_cash_flow: pd.DataFrame,
    settings: ValuationFilterSettings,
) -> FilterFrameResult:
    require_columns(
        valuation_history,
        ["code", "date", "industry", "pe_ttm", "pb"],
        "valuation_history",
    )
    require_columns(dividends, ["code", "date", "industry", "dividend_yield"], "dividends")
    require_columns(free_cash_flow, ["code", "date", "fcf_yield"], "free_cash_flow")

    current_valuation = _latest_by_code(
        valuation_history.loc[valuation_history["code"].isin(candidates["code"])],
        date_column="date",
    )
    current_dividends = _latest_by_code(
        dividends.loc[dividends["code"].isin(candidates["code"])],
        date_column="date",
    )
    current_fcf = _latest_by_code(
        free_cash_flow.loc[free_cash_flow["code"].isin(candidates["code"])],
        date_column="date",
    )
    dividend_stats = (
        _latest_by_code(dividends, date_column="date")
        .groupby("industry")["dividend_yield"]
        .agg(["median", "count"])
    )

    enriched = candidates.copy()
    for column in ["pe_ttm", "pb"]:
        if column not in enriched:
            enriched[column] = pd.NA

    valuation_current = current_valuation[["code", "industry", "pe_ttm", "pb"]].rename(
        columns={
            "industry": "valuation_industry",
            "pe_ttm": "valuation_pe_ttm",
            "pb": "valuation_pb",
        }
    )
    enriched = enriched.merge(valuation_current, on="code", how="left")
    enriched["valuation_industry"] = enriched["valuation_industry"].fillna(enriched["industry"])
    enriched["pe_ttm"] = _coalesce_numeric(enriched["valuation_pe_ttm"], enriched["pe_ttm"])
    enriched["pb"] = _coalesce_numeric(enriched["valuation_pb"], enriched["pb"])
    enriched = enriched.drop(columns=["valuation_pe_ttm", "valuation_pb"])
    enriched = enriched.merge(
        current_dividends[["code", "dividend_yield"]],
        on="code",
        how="left",
    )
    enriched = enriched.merge(current_fcf[["code", "fcf_yield"]], on="code", how="left")

    pe_percentiles: list[float | None] = []
    pb_percentiles: list[float | None] = []
    industry_dividend_medians: list[float | None] = []
    industry_dividend_counts: list[int] = []
    for _, row in enriched.iterrows():
        industry = row["valuation_industry"]
        history = valuation_history.loc[valuation_history["industry"] == industry]
        pe_percentiles.append(percentile_rank_lower(row.get("pe_ttm"), history["pe_ttm"]))
        pb_percentiles.append(percentile_rank_lower(row.get("pb"), history["pb"]))
        if industry in dividend_stats.index:
            industry_dividend_medians.append(float(dividend_stats.loc[industry, "median"]))
            industry_dividend_counts.append(int(dividend_stats.loc[industry, "count"]))
        else:
            industry_dividend_medians.append(None)
            industry_dividend_counts.append(0)

    enriched["pe_percentile"] = pe_percentiles
    enriched["pb_percentile"] = pb_percentiles
    enriched["industry_dividend_median"] = industry_dividend_medians
    enriched["industry_dividend_count"] = industry_dividend_counts

    return split_by_rules(
        enriched,
        [
            (
                "missing_valuation_data",
                lambda frame: frame[
                    [
                        "pe_ttm",
                        "pb",
                        "pe_percentile",
                        "pb_percentile",
                        "dividend_yield",
                        "fcf_yield",
                        "industry_dividend_median",
                    ]
                ]
                .notna()
                .all(axis=1),
            ),
            (
                "pe_valuation_percentile",
                lambda frame: pd.to_numeric(frame["pe_percentile"], errors="coerce").between(
                    settings.min_pe_percentile,
                    settings.max_pe_percentile,
                    inclusive="both",
                ),
            ),
            (
                "pb_valuation_percentile",
                lambda frame: pd.to_numeric(frame["pb_percentile"], errors="coerce").between(
                    settings.min_pb_percentile,
                    settings.max_pb_percentile,
                    inclusive="both",
                ),
            ),
            (
                "dividend_yield",
                _dividend_yield_ok,
            ),
            (
                "fcf_yield",
                lambda frame: pd.to_numeric(frame["fcf_yield"], errors="coerce")
                > settings.min_fcf_yield,
            ),
        ],
    )


def _dividend_yield_ok(frame: pd.DataFrame) -> pd.Series:
    dividend_yield = pd.to_numeric(frame["dividend_yield"], errors="coerce")
    median = pd.to_numeric(frame["industry_dividend_median"], errors="coerce")
    sample_count = pd.to_numeric(frame["industry_dividend_count"], errors="coerce").fillna(0)
    return (dividend_yield > median) | ((sample_count <= 1) & (dividend_yield >= median))


def _coalesce_numeric(primary: pd.Series, fallback: pd.Series) -> pd.Series:
    primary_numeric = pd.to_numeric(primary, errors="coerce")
    fallback_numeric = pd.to_numeric(fallback, errors="coerce")
    return primary_numeric.where(primary_numeric.notna(), fallback_numeric)


def _latest_by_code(frame: pd.DataFrame, date_column: str) -> pd.DataFrame:
    if frame.empty:
        return frame.copy()
    dated = frame.copy()
    dated[date_column] = pd.to_datetime(dated[date_column])
    return dated.sort_values(["code", date_column]).groupby("code", as_index=False).tail(1)
