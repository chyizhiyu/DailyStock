from __future__ import annotations

from datetime import date
from pathlib import Path

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

