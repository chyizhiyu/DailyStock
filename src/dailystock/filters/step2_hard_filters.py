from __future__ import annotations

from datetime import date

import pandas as pd

from dailystock.config import HardFilterSettings
from dailystock.models.screening import FilterFrameResult
from dailystock.utils.validation import bool_series, require_columns, split_by_rules


def run_hard_filters(
    meta: pd.DataFrame,
    daily_bars: pd.DataFrame,
    financials: pd.DataFrame,
    as_of: date,
    settings: HardFilterSettings,
) -> FilterFrameResult:
    require_columns(daily_bars, ["code", "trade_date", "amount"], "daily_bars")
    require_columns(
        financials,
        ["code", "fiscal_year", "operating_cash_flow", "non_gaap_net_profit"],
        "financials",
    )

    enriched = meta.copy()
    enriched["listing_date"] = pd.to_datetime(enriched["listing_date"])
    enriched = enriched.merge(_avg_turnover(daily_bars, as_of), on="code", how="left")
    enriched = enriched.merge(_hard_financial_flags(financials, settings), on="code", how="left")
    enriched["effective_trade_days_30d"] = enriched["effective_trade_days_30d"].fillna(0)
    enriched["has_financial_history"] = enriched["has_financial_history"].fillna(False)
    enriched["consecutive_losses"] = enriched["consecutive_losses"].fillna(True)
    enriched["long_negative_ocf"] = enriched["long_negative_ocf"].fillna(True)

    cutoff = pd.Timestamp(as_of) - pd.DateOffset(years=settings.min_listing_years)

    return split_by_rules(
        enriched,
        [
            ("risk_screen", _risk_screen),
            ("listing_age", lambda frame: frame["listing_date"] <= cutoff),
            ("liquidity", lambda frame: _turnover_ok(frame, settings)),
            (
                "market_cap",
                lambda frame: pd.to_numeric(frame["total_market_cap"], errors="coerce")
                >= settings.min_total_market_cap,
            ),
            ("missing_financials", lambda frame: frame["has_financial_history"].astype(bool)),
            (
                "performance_floor",
                lambda frame: ~frame["consecutive_losses"].astype(bool)
                & ~frame["long_negative_ocf"].astype(bool),
            ),
        ],
    )


def _avg_turnover(daily_bars: pd.DataFrame, as_of: date) -> pd.DataFrame:
    bars = daily_bars.copy()
    bars["trade_date"] = pd.to_datetime(bars["trade_date"])
    bars["amount"] = pd.to_numeric(bars["amount"], errors="coerce")
    end = pd.Timestamp(as_of)
    start = end - pd.Timedelta(days=30)
    bars = bars.loc[(bars["trade_date"] > start) & (bars["trade_date"] <= end)]
    return (
        bars.groupby("code", as_index=False)
        .agg(
            avg_turnover_20d=("amount", "mean"),
            effective_trade_days_30d=("trade_date", "nunique"),
        )
    )


def _hard_financial_flags(
    financials: pd.DataFrame,
    settings: HardFilterSettings,
) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    frame = financials.copy()
    frame["operating_cash_flow"] = pd.to_numeric(frame["operating_cash_flow"], errors="coerce")
    frame["non_gaap_net_profit"] = pd.to_numeric(frame["non_gaap_net_profit"], errors="coerce")

    for code, group in frame.sort_values("fiscal_year").groupby("code"):
        losses = group["non_gaap_net_profit"].tail(settings.consecutive_loss_years)
        ocf = group["operating_cash_flow"].tail(settings.negative_ocf_years)
        records.append(
            {
                "code": code,
                "has_financial_history": not group.empty,
                "consecutive_losses": len(losses) >= settings.consecutive_loss_years
                and bool((losses < 0).all()),
                "long_negative_ocf": len(ocf) >= settings.negative_ocf_years
                and bool((ocf < 0).all()),
            }
        )

    return pd.DataFrame.from_records(
        records,
        columns=["code", "has_financial_history", "consecutive_losses", "long_negative_ocf"],
    )


def _risk_screen(frame: pd.DataFrame) -> pd.Series:
    market = frame["market"].astype(str).str.upper()
    is_cn = market.eq("CN")
    is_hk = market.eq("HK")
    cn_ok = is_cn & ~bool_series(frame, "is_st")
    hk_ok = (
        is_hk
        & ~bool_series(frame, "is_suspended")
        & ~bool_series(frame, "is_penny_stock")
        & ~_hk_restricted_suffix(frame)
        & ~(bool_series(frame, "is_biotech_w") & ~bool_series(frame, "is_profitable_biotech", True))
    )
    return cn_ok | hk_ok


def _turnover_ok(frame: pd.DataFrame, settings: HardFilterSettings) -> pd.Series:
    thresholds = frame["market"].map(settings.min_avg_turnover).fillna(float("inf"))
    turnover = pd.to_numeric(frame["avg_turnover_20d"], errors="coerce")
    trade_days = pd.to_numeric(frame["effective_trade_days_30d"], errors="coerce").fillna(0)
    return (trade_days >= 20) & (turnover >= thresholds)


def _hk_restricted_suffix(frame: pd.DataFrame) -> pd.Series:
    code = frame.get("code", pd.Series("", index=frame.index)).fillna("").astype(str).str.upper()
    name = frame.get("name", pd.Series("", index=frame.index)).fillna("").astype(str).str.upper()
    code_restricted = code.str.endswith(("W", "SS")) | code.str.contains(
        r"[-_.](?:W|SS)$",
        regex=True,
    )
    name_restricted = name.str.contains(
        r"(?:^|[\s\-_.(\[])(?:W|SS)(?:[\s\-_.),\]]|$)",
        regex=True,
    )
    return code_restricted | name_restricted
