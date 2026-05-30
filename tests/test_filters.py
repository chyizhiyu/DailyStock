from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from dailystock.config import load_settings
from dailystock.data_sources.sample import SampleDataProvider
from dailystock.filters.step1_fetch_meta import fetch_meta
from dailystock.filters.step2_hard_filters import run_hard_filters
from dailystock.filters.step3_financial_quality import run_financial_quality_filters
from dailystock.filters.step4_valuation import run_valuation_filters

AS_OF = date(2026, 5, 29)


def test_hard_filters_reject_known_risks() -> None:
    settings, provider = _settings_and_provider()
    meta = fetch_meta(provider, AS_OF, ["CN", "HK"])
    financials = provider.load_financials(meta["code"].tolist(), AS_OF)
    daily_bars = provider.load_daily_bars(meta["code"].tolist(), AS_OF)

    result = run_hard_filters(meta, daily_bars, financials, AS_OF, settings.hard_filters)

    assert set(result.candidates["code"]) == {"CN000001", "HK00001", "CN000007", "CN000008"}
    assert result.rejection_counts["risk_screen"] == 3
    assert result.rejection_counts["listing_age"] == 1
    assert result.rejection_counts["liquidity"] == 1
    assert result.rejection_counts["market_cap"] == 1
    assert result.rejection_counts["performance_floor"] == 1


def test_hard_filters_reject_hk_suffix_even_without_vendor_flag() -> None:
    settings, _ = _settings_and_provider()
    meta = _minimal_meta(code="HK12345", name="Example Bio-W", market="HK")
    result = run_hard_filters(
        meta,
        _daily_bars("HK12345", days=20, amount=60_000_000),
        _hard_financials("HK12345"),
        AS_OF,
        settings.hard_filters,
    )

    assert result.candidates.empty
    assert result.rejection_counts == {"risk_screen": 1}


def test_hard_filters_reject_liquidity_when_effective_days_under_20() -> None:
    settings, _ = _settings_and_provider()
    meta = _minimal_meta(code="HK12345", name="Harbor Quality", market="HK")
    result = run_hard_filters(
        meta,
        _daily_bars("HK12345", days=19, amount=60_000_000),
        _hard_financials("HK12345"),
        AS_OF,
        settings.hard_filters,
    )

    assert result.candidates.empty
    assert result.rejection_counts == {"liquidity": 1}


def test_financial_quality_keeps_profitable_cash_generators() -> None:
    settings, provider = _settings_and_provider()
    hard = _hard_result(settings, provider)
    financials = provider.load_financials(hard.candidates["code"].tolist(), AS_OF)

    result = run_financial_quality_filters(
        hard.candidates,
        financials,
        settings.quality_filters,
    )

    assert set(result.candidates["code"]) == {"CN000001", "HK00001", "CN000008"}
    assert result.rejection_counts == {"profitability": 1}


def test_valuation_keeps_industry_relative_value() -> None:
    settings, provider = _settings_and_provider()
    hard = _hard_result(settings, provider)
    financials = provider.load_financials(hard.candidates["code"].tolist(), AS_OF)
    quality = run_financial_quality_filters(hard.candidates, financials, settings.quality_filters)

    result = run_valuation_filters(
        quality.candidates,
        provider.load_valuation_history(None, AS_OF),
        provider.load_dividends(None, AS_OF),
        provider.load_free_cash_flow(None, AS_OF),
        settings.valuation_filters,
    )

    assert set(result.candidates["code"]) == {"CN000001", "HK00001"}
    assert result.rejection_counts == {"pe_valuation_percentile": 1}


def _hard_result(settings, provider):
    meta = fetch_meta(provider, AS_OF, ["CN", "HK"])
    return run_hard_filters(
        meta,
        provider.load_daily_bars(meta["code"].tolist(), AS_OF),
        provider.load_financials(meta["code"].tolist(), AS_OF),
        AS_OF,
        settings.hard_filters,
    )


def _settings_and_provider():
    settings = load_settings()
    data_dir = Path(__file__).resolve().parents[1] / "data" / "samples"
    return settings, SampleDataProvider(data_dir)


def _minimal_meta(code: str, name: str, market: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "code": code,
                "name": name,
                "market": market,
                "exchange": "HKEX" if market == "HK" else "SSE",
                "industry": "HS_Healthcare" if market == "HK" else "SW_Healthcare",
                "is_st": False,
                "listing_date": "2010-01-01",
                "total_market_cap": 10_000_000_000,
                "is_suspended": False,
                "is_penny_stock": False,
                "is_biotech_w": False,
                "is_profitable_biotech": True,
            }
        ]
    )


def _daily_bars(code: str, days: int, amount: float) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "code": code,
            "trade_date": pd.bdate_range(end=pd.Timestamp(AS_OF), periods=days),
            "amount": amount,
        }
    )


def _hard_financials(code: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "code": code,
                "fiscal_year": 2024,
                "operating_cash_flow": 100_000_000,
                "non_gaap_net_profit": 80_000_000,
            }
        ]
    )
