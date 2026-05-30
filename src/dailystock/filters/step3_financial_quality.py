from __future__ import annotations

import pandas as pd

from dailystock.config import QualityFilterSettings
from dailystock.models.screening import FilterFrameResult
from dailystock.utils.metrics import annualized_cagr, safe_ratio
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
    records: list[dict[str, object]] = []
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

    for code, group in frame.sort_values("fiscal_year").groupby("code"):
        latest = group.iloc[-1]
        latest_year = int(latest["fiscal_year"])
        base_candidates = group.loc[group["fiscal_year"] <= latest_year - settings.growth_years]
        base = base_candidates.iloc[-1] if not base_candidates.empty else group.iloc[0]
        elapsed_years = latest_year - int(base["fiscal_year"])

        records.append(
            {
                "code": code,
                "has_quality_financials": True,
                "roe": latest["roe"],
                "gross_margin": latest["gross_margin"],
                "net_margin": latest["net_margin"],
                "debt_asset_ratio": latest["debt_asset_ratio"],
                "ocf_to_net_profit": safe_ratio(
                    latest["operating_cash_flow"],
                    latest["net_profit"],
                ),
                "has_growth_history": elapsed_years >= settings.growth_years,
                "revenue_cagr": annualized_cagr(base["revenue"], latest["revenue"], elapsed_years),
                "net_profit_cagr": annualized_cagr(
                    base["net_profit"],
                    latest["net_profit"],
                    elapsed_years,
                ),
            }
        )

    return pd.DataFrame.from_records(
        records,
        columns=[
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
        ],
    )
