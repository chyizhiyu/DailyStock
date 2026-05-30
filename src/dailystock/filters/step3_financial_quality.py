from __future__ import annotations

import pandas as pd

from dailystock.config import QualityFilterSettings
from dailystock.models.screening import FilterFrameResult
from dailystock.utils.validation import require_columns, split_by_rules


def run_financial_quality_filters(
    candidates: pd.DataFrame,
    financials: pd.DataFrame,
    settings: QualityFilterSettings,
) -> FilterFrameResult:
    require_columns(
        financials,
        [
            "code",
            "fiscal_year",
            "roe",
            "gross_margin",
            "net_margin",
            "debt_asset_ratio",
            "operating_cash_flow",
            "net_profit",
            "revenue",
        ],
        "financials",
    )
    enriched = candidates.merge(_quality_metrics(financials, settings), on="code", how="left")
    enriched["has_quality_financials"] = enriched["has_quality_financials"].fillna(False)

    return split_by_rules(
        enriched,
        [
            (
                "missing_quality_financials",
                lambda frame: frame["has_quality_financials"].astype(bool),
            ),
            (
                "profitability",
                lambda frame: (pd.to_numeric(frame["roe"], errors="coerce") > settings.min_roe)
                & (
                    pd.to_numeric(frame["gross_margin"], errors="coerce")
                    > settings.min_gross_margin
                )
                & (pd.to_numeric(frame["net_margin"], errors="coerce") > settings.min_net_margin),
            ),
            (
                "leverage",
                lambda frame: pd.to_numeric(frame["debt_asset_ratio"], errors="coerce")
                < settings.max_debt_asset_ratio,
            ),
            (
                "cash_flow_quality",
                lambda frame: pd.to_numeric(frame["ocf_to_net_profit"], errors="coerce")
                > settings.min_ocf_to_net_profit,
            ),
            (
                "growth",
                lambda frame: frame["has_growth_history"].astype(bool)
                & (
                    pd.to_numeric(frame["revenue_cagr"], errors="coerce")
                    > settings.min_revenue_cagr
                )
                & (
                    pd.to_numeric(frame["net_profit_cagr"], errors="coerce")
                    > settings.min_net_profit_cagr
                ),
            ),
        ],
    )


def _quality_metrics(financials: pd.DataFrame, settings: QualityFilterSettings) -> pd.DataFrame:
    numeric_columns = [
        "roe",
        "gross_margin",
        "net_margin",
        "debt_asset_ratio",
        "operating_cash_flow",
        "net_profit",
        "revenue",
    ]
    frame = financials.copy()
    for column in numeric_columns:
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame["fiscal_year"] = pd.to_numeric(frame["fiscal_year"], errors="coerce")
    frame = frame.dropna(subset=["code", "fiscal_year"]).sort_values(["code", "fiscal_year"])

    latest_idx = frame.groupby("code")["fiscal_year"].idxmax()
    latest = frame.loc[latest_idx].copy()
    latest = latest.rename(
        columns={
            "fiscal_year": "latest_year",
            "revenue": "latest_revenue",
            "net_profit": "latest_net_profit",
        }
    )
    latest["base_year_cutoff"] = latest["latest_year"] - settings.growth_years

    base_pool = frame.merge(
        latest[["code", "base_year_cutoff"]],
        on="code",
        how="inner",
    )
    base_pool = base_pool.loc[base_pool["fiscal_year"] <= base_pool["base_year_cutoff"]]
    if base_pool.empty:
        base = pd.DataFrame(columns=["code", "base_year", "base_revenue", "base_net_profit"])
    else:
        base_idx = base_pool.groupby("code")["fiscal_year"].idxmax()
        base = base_pool.loc[base_idx, ["code", "fiscal_year", "revenue", "net_profit"]].rename(
            columns={
                "fiscal_year": "base_year",
                "revenue": "base_revenue",
                "net_profit": "base_net_profit",
            }
        )

    metrics = latest.merge(base, on="code", how="left")
    metrics["has_quality_financials"] = True
    metrics["ocf_to_net_profit"] = pd.NA
    ratio_valid = metrics["latest_net_profit"].ne(0) & metrics["latest_net_profit"].notna()
    metrics.loc[ratio_valid, "ocf_to_net_profit"] = (
        metrics.loc[ratio_valid, "operating_cash_flow"]
        / metrics.loc[ratio_valid, "latest_net_profit"]
    )
    metrics["elapsed_years"] = metrics["latest_year"] - metrics["base_year"]
    metrics["has_growth_history"] = metrics["elapsed_years"] >= settings.growth_years

    revenue_valid = (
        metrics["base_revenue"].gt(0)
        & metrics["latest_revenue"].gt(0)
        & metrics["elapsed_years"].gt(0)
    )
    profit_valid = (
        metrics["base_net_profit"].gt(0)
        & metrics["latest_net_profit"].gt(0)
        & metrics["elapsed_years"].gt(0)
    )
    metrics["revenue_cagr"] = pd.NA
    metrics["net_profit_cagr"] = pd.NA
    metrics.loc[revenue_valid, "revenue_cagr"] = (
        metrics.loc[revenue_valid, "latest_revenue"]
        / metrics.loc[revenue_valid, "base_revenue"]
    ) ** (1 / metrics.loc[revenue_valid, "elapsed_years"]) - 1
    metrics.loc[profit_valid, "net_profit_cagr"] = (
        metrics.loc[profit_valid, "latest_net_profit"]
        / metrics.loc[profit_valid, "base_net_profit"]
    ) ** (1 / metrics.loc[profit_valid, "elapsed_years"]) - 1

    return metrics[
        [
            "code",
            "has_quality_financials",
            "roe",
            "gross_margin",
            "net_margin",
            "debt_asset_ratio",
            "ocf_to_net_profit",
            "has_growth_history",
            "revenue_cagr",
            "net_profit_cagr",
        ]
    ].reset_index(drop=True)
