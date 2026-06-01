from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import pandas as pd

from dailystock.data_sources.akshare import (
    EMPTY_DIVIDEND_COLUMNS,
    EMPTY_FCF_COLUMNS,
    EMPTY_FINANCIAL_COLUMNS,
    EMPTY_VALUATION_COLUMNS,
    AkShareDataProvider,
)

SEED_SCHEMAS: dict[str, list[str]] = {
    "cn_constituents.csv": ["code", "name", "exchange", "industry"],
    "a_spot.csv": [
        "code",
        "name_spot",
        "latest_price",
        "amount",
        "pe_ttm",
        "pb",
        "total_market_cap",
        "free_float_market_cap",
    ],
    "a_listing_info.csv": ["code", "listing_date", "industry_listing"],
    "sw_industry.csv": ["code", "industry_sw"],
    "hk_hsci_constituents.csv": ["code", "name", "industry"],
    "hk_spot_full.csv": [
        "code",
        "name_spot",
        "latest_price",
        "amount",
        "pe_ttm",
        "pb",
        "total_market_cap",
        "free_float_market_cap",
    ],
    "hk_listing_info.csv": ["code", "listing_date", "industry_listing"],
    "daily_bars.csv": ["code", "trade_date", "amount"],
    "financials.csv": EMPTY_FINANCIAL_COLUMNS,
    "valuation_history.csv": EMPTY_VALUATION_COLUMNS,
    "dividends.csv": EMPTY_DIVIDEND_COLUMNS,
    "free_cash_flow.csv": EMPTY_FCF_COLUMNS,
}


@dataclass(frozen=True)
class AkShareSeedExportResult:
    output_dir: Path
    row_counts: dict[str, int]
    codes: list[str]


def export_akshare_seed_files(
    provider: AkShareDataProvider,
    as_of: date,
    markets: Sequence[str],
    output_dir: str | Path,
    *,
    daily_lookback_days: int = 30,
    valuation_lookback_years: int = 5,
    max_codes: int | None = None,
) -> AkShareSeedExportResult:
    """Export canonical AkShare seed CSVs for CI/offline screening.

    This intentionally uses the provider's normalized boundary methods so the
    generated files match the exact schemas consumed by the GitHub Actions
    offline fallback path.
    """

    requested = {market.strip().upper() for market in markets if market.strip()}
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    meta = provider.fetch_meta(as_of, sorted(requested))
    if max_codes is not None:
        meta = meta.head(max_codes)
    codes = meta["code"].astype(str).tolist() if "code" in meta else []

    frames: dict[str, pd.DataFrame] = {}
    if "CN" in requested:
        frames["cn_constituents.csv"] = provider._load_cn_constituents(as_of)
        frames["a_spot.csv"] = provider._load_a_spot(as_of)
        frames["a_listing_info.csv"] = provider._load_a_listing_info(as_of)
        frames["sw_industry.csv"] = provider._load_sw_industry_map(as_of)
    if "HK" in requested:
        hk_spot = provider._load_hk_spot(as_of)
        frames["hk_spot_full.csv"] = hk_spot
        frames["hk_hsci_constituents.csv"] = provider._load_hk_hsci_constituents(as_of, hk_spot)
        frames["hk_listing_info.csv"] = provider._load_hk_listing_info(as_of)

    daily_bars = provider.load_daily_bars(
        codes,
        as_of=as_of,
        lookback_days=daily_lookback_days,
    )
    frames["daily_bars.csv"] = daily_bars
    if "a_spot.csv" in frames:
        frames["a_spot.csv"] = _enrich_spot_with_daily_snapshot(frames["a_spot.csv"], daily_bars)
    frames["financials.csv"] = provider.load_financials(codes, as_of=as_of)
    frames["valuation_history.csv"] = provider.load_valuation_history(
        codes,
        as_of=as_of,
        lookback_years=valuation_lookback_years,
    )
    frames["dividends.csv"] = provider.load_dividends(codes, as_of=as_of)
    frames["free_cash_flow.csv"] = provider.load_free_cash_flow(codes, as_of=as_of)

    row_counts: dict[str, int] = {}
    for filename, columns in SEED_SCHEMAS.items():
        frame = frames.get(filename, pd.DataFrame(columns=columns))
        frame = _ensure_seed_columns(frame, columns)
        frame.to_csv(target_dir / filename, index=False)
        row_counts[filename] = len(frame)

    return AkShareSeedExportResult(output_dir=target_dir, row_counts=row_counts, codes=codes)


def _ensure_seed_columns(frame: pd.DataFrame, columns: Sequence[str]) -> pd.DataFrame:
    out = frame.copy()
    for column in columns:
        if column not in out:
            out[column] = pd.NA
    return out[list(columns)]


def _enrich_spot_with_daily_snapshot(spot: pd.DataFrame, daily_bars: pd.DataFrame) -> pd.DataFrame:
    if spot.empty or daily_bars.empty:
        return spot
    required = {"code", "trade_date", "amount", "close", "outstanding_share"}
    if not required.issubset(daily_bars.columns):
        return spot

    latest = (
        daily_bars.dropna(subset=["code", "trade_date"])
        .sort_values(["code", "trade_date"])
        .groupby("code", as_index=False)
        .tail(1)
    )
    latest = latest[["code", "amount", "close", "outstanding_share"]].copy()
    latest["snapshot_market_cap"] = latest["close"] * latest["outstanding_share"]

    enriched = spot.merge(latest, on="code", how="left", suffixes=("", "_daily"))
    for target, source in [
        ("latest_price", "close"),
        ("amount", "amount_daily"),
        ("total_market_cap", "snapshot_market_cap"),
        ("free_float_market_cap", "snapshot_market_cap"),
    ]:
        enriched[target] = enriched[target].combine_first(enriched[source])
    return enriched.drop(
        columns=["amount_daily", "close", "outstanding_share", "snapshot_market_cap"]
    )
