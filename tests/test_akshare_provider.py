from __future__ import annotations

from datetime import date

import pandas as pd

from dailystock.data_sources.akshare import AkShareDataProvider
from dailystock.data_sources.akshare_seed import SEED_SCHEMAS, export_akshare_seed_files

AS_OF = date(2026, 5, 29)


def test_akshare_provider_normalizes_vendor_shapes(tmp_path) -> None:
    provider = AkShareDataProvider(cache_dir=tmp_path, ak_module=_FakeAkShare(), max_workers=1)
    provider._fetch_a_spot_full_from_eastmoney = _fake_a_spot  # noqa: SLF001
    provider._fetch_hk_spot_full_from_eastmoney = _fake_hk_spot  # noqa: SLF001

    meta = provider.fetch_meta(AS_OF, ["CN", "HK"])

    assert set(meta["code"]) == {"600000", "00700"}
    assert meta.set_index("code").loc["600000", "industry"] == "SW_480301"
    assert meta.set_index("code").loc["00700", "industry"] == "HS_IT"
    assert meta.set_index("code").loc["600000", "total_market_cap"] == 600_000_000_000

    bars = provider.load_daily_bars(meta["code"].tolist(), AS_OF, lookback_days=30)
    assert bars.groupby("code")["trade_date"].nunique().to_dict() == {
        "600000": 20,
        "00700": 20,
    }

    financials = provider.load_financials(meta["code"].tolist(), AS_OF)
    latest = financials.sort_values("fiscal_year").groupby("code").tail(1).set_index("code")
    assert latest.loc["600000", "roe"] == 0.12
    assert latest.loc["00700", "gross_margin"] == 0.45

    valuation = provider.load_valuation_history(None, AS_OF, lookback_years=5)
    assert {"code", "date", "industry", "pe_ttm", "pb"}.issubset(valuation.columns)
    assert set(valuation["code"]) == {"600000", "00700"}

    dividends = provider.load_dividends(meta["code"].tolist(), AS_OF)
    assert set(dividends["code"]) == {"600000", "00700"}
    assert dividends["dividend_yield"].notna().all()

    fcf = provider.load_free_cash_flow(meta["code"].tolist(), AS_OF)
    assert set(fcf["code"]) == {"600000", "00700"}
    assert fcf["fcf_yield"].notna().all()


def test_akshare_provider_hk_sina_fallback_ignores_empty_cache(tmp_path) -> None:
    provider = AkShareDataProvider(
        cache_dir=tmp_path / "cache",
        seed_dir=tmp_path / "seed",
        ak_module=_FakeSinaHongKongAkShare(),
        max_workers=1,
    )
    provider._cache_path("hk_spot_full", AS_OF.strftime("%Y%m%d")).write_text(  # noqa: SLF001
        "code,name_spot,latest_price,amount,pe_ttm,pb,total_market_cap,free_float_market_cap\n",
        encoding="utf-8",
    )
    provider._cache_path("hk_hsci_constituents", AS_OF.strftime("%Y%m%d")).write_text(  # noqa: SLF001
        "code,name,industry\n",
        encoding="utf-8",
    )
    provider._fetch_hk_spot_full_from_eastmoney = _raise_hk_spot_failure  # noqa: SLF001
    provider._load_hk_metrics_snapshot = lambda as_of: pd.DataFrame(  # noqa: ARG005, SLF001
        {
            "code": ["00700"],
            "name_spot": ["腾讯控股"],
            "latest_price": [pd.NA],
            "amount": [pd.NA],
            "pe_ttm": [14.8],
            "pb": [3.05],
            "total_market_cap": [3_895_000_000_000],
            "free_float_market_cap": [3_895_000_000_000],
        }
    )

    meta = provider.fetch_meta(AS_OF, ["HK"])

    assert len(meta) == 1
    row = meta.iloc[0]
    assert row["code"] == "00700"
    assert row["market"] == "HK"
    assert row["amount"] == 1_000_000_000
    assert row["total_market_cap"] == 3_895_000_000_000
    assert row["pe_ttm"] == 14.8


def test_akshare_provider_uses_seed_files_in_offline_mode(tmp_path) -> None:
    seed_dir = tmp_path / "seed"
    seed_dir.mkdir()
    pd.DataFrame(
        {
            "code": ["600000"],
            "name": ["浦发银行"],
            "exchange": ["SSE"],
            "industry": ["SW_Bank"],
        }
    ).to_csv(seed_dir / "cn_constituents.csv", index=False)
    pd.DataFrame(
        {
            "code": ["600000"],
            "name_spot": ["浦发银行"],
            "latest_price": [10],
            "amount": [90_000_000],
            "pe_ttm": [8],
            "pb": [0.8],
            "total_market_cap": [600_000_000_000],
            "free_float_market_cap": [500_000_000_000],
        }
    ).to_csv(seed_dir / "a_spot.csv", index=False)
    pd.DataFrame(
        {
            "code": ["600000"],
            "listing_date": ["1999-11-10"],
            "industry_listing": ["银行"],
        }
    ).to_csv(seed_dir / "a_listing_info.csv", index=False)
    pd.DataFrame({"code": ["600000"], "industry_sw": ["SW_Bank"]}).to_csv(
        seed_dir / "sw_industry.csv",
        index=False,
    )
    pd.DataFrame(
        {
            "code": ["00700"],
            "name_spot": ["腾讯控股"],
            "latest_price": [300],
            "amount": [2_000_000_000],
            "pe_ttm": [15],
            "pb": [3],
            "total_market_cap": [3_000_000_000_000],
            "free_float_market_cap": [2_500_000_000_000],
        }
    ).to_csv(seed_dir / "hk_spot_full.csv", index=False)
    pd.DataFrame({"code": ["00700"], "listing_date": ["2004-06-16"]}).to_csv(
        seed_dir / "hk_listing_info.csv",
        index=False,
    )
    _fake_hist(amount=90_000_000).assign(code="600000").rename(
        columns={"日期": "trade_date", "成交额": "amount"}
    )[["code", "trade_date", "amount"]].to_csv(seed_dir / "daily_bars.csv", index=False)
    pd.DataFrame(
        {
            "code": ["600000", "600000"],
            "fiscal_year": [2019, 2024],
            "roe": [0.11, 0.12],
            "gross_margin": [0.31, 0.32],
            "net_margin": [0.09, 0.1],
            "debt_asset_ratio": [0.5, 0.49],
            "operating_cash_flow": [10_000_000_000, 15_000_000_000],
            "net_profit": [8_000_000_000, 10_000_000_000],
            "non_gaap_net_profit": [7_000_000_000, 9_000_000_000],
            "revenue": [100_000_000_000, 130_000_000_000],
        }
    ).to_csv(seed_dir / "financials.csv", index=False)
    pd.DataFrame(
        {
            "code": ["600000"],
            "date": ["2026-05-29"],
            "industry": ["SW_Bank"],
            "pe_ttm": [8],
            "pb": [0.8],
        }
    ).to_csv(seed_dir / "valuation_history.csv", index=False)
    pd.DataFrame(
        {
            "code": ["600000"],
            "date": ["2026-05-29"],
            "industry": ["SW_Bank"],
            "dividend_yield": [0.04],
        }
    ).to_csv(seed_dir / "dividends.csv", index=False)
    pd.DataFrame(
        {"code": ["600000"], "date": ["2026-05-29"], "fcf_yield": [0.05]}
    ).to_csv(seed_dir / "free_cash_flow.csv", index=False)

    provider = AkShareDataProvider(
        cache_dir=tmp_path / "cache",
        seed_dir=seed_dir,
        ak_module=_ExplodingAkShare(),
        max_workers=1,
        offline=True,
    )

    meta = provider.fetch_meta(AS_OF, ["CN", "HK"])
    assert set(meta["code"]) == {"600000", "00700"}
    assert meta.loc[meta["code"].eq("600000"), "industry"].iloc[0] == "SW_Bank"
    assert meta.loc[meta["code"].eq("00700"), "market"].iloc[0] == "HK"
    assert provider.load_daily_bars(["600000"], AS_OF, lookback_days=30).shape[0] == 20
    assert provider.load_financials(["600000"], AS_OF)["fiscal_year"].max() == 2024
    assert provider.load_valuation_history(None, AS_OF)["pe_ttm"].iloc[0] == 8
    assert provider.load_dividends(["600000"], AS_OF)["dividend_yield"].iloc[0] == 0.04
    assert provider.load_free_cash_flow(["600000"], AS_OF)["fcf_yield"].iloc[0] == 0.05


def test_akshare_daily_bars_support_spot_proxy_mode(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("DAILYSTOCK_AKSHARE_DAILY_BAR_MODE", "spot-proxy")
    provider = AkShareDataProvider(
        cache_dir=tmp_path / "cache",
        seed_dir=tmp_path / "seed",
        ak_module=_ExplodingAkShare(),
        max_workers=1,
    )
    provider._last_meta = pd.DataFrame(  # noqa: SLF001
        {
            "code": ["600000", "00700"],
            "market": ["CN", "HK"],
            "amount": [90_000_000, 80_000_000],
        }
    )

    bars = provider.load_daily_bars(["600000", "00700"], AS_OF, lookback_days=30)

    assert bars.groupby("code")["trade_date"].nunique().to_dict() == {
        "600000": 20,
        "00700": 20,
    }
    assert bars.groupby("code")["amount"].mean().to_dict() == {
        "600000": 90_000_000,
        "00700": 80_000_000,
    }


def test_akshare_financials_skip_non_cn_bulk_fallback_when_over_limit(
    tmp_path,
    monkeypatch,
) -> None:
    monkeypatch.setenv("DAILYSTOCK_AKSHARE_PER_STOCK_FINANCIAL_LIMIT", "1")
    monkeypatch.setenv("DAILYSTOCK_AKSHARE_HK_FINANCIAL_LIMIT", "0")
    provider = AkShareDataProvider(
        cache_dir=tmp_path / "cache",
        seed_dir=tmp_path / "seed",
        ak_module=_ExplodingAkShare(),
        max_workers=1,
    )
    provider._last_meta = pd.DataFrame(  # noqa: SLF001
        {
            "code": ["00700", "00005"],
            "market": ["HK", "HK"],
        }
    )

    financials = provider.load_financials(["00700", "00005"], AS_OF)

    assert financials.empty


def test_akshare_seed_export_writes_canonical_csvs(tmp_path) -> None:
    seed_dir = tmp_path / "seed"
    provider = AkShareDataProvider(
        cache_dir=tmp_path / "cache",
        seed_dir=seed_dir,
        ak_module=_FakeAkShare(),
        max_workers=1,
        use_seed=False,
    )
    provider._fetch_a_spot_full_from_eastmoney = _fake_a_spot  # noqa: SLF001
    provider._fetch_hk_spot_full_from_eastmoney = _fake_hk_spot  # noqa: SLF001

    result = export_akshare_seed_files(
        provider=provider,
        as_of=AS_OF,
        markets=["CN", "HK"],
        output_dir=seed_dir,
    )

    assert set(result.codes) == {"600000", "00700"}
    for filename, columns in SEED_SCHEMAS.items():
        path = seed_dir / filename
        assert path.exists()
        assert pd.read_csv(path, nrows=0).columns.tolist() == columns
    assert result.row_counts["daily_bars.csv"] == 40
    assert result.row_counts["financials.csv"] == 4


class _FakeAkShare:
    @staticmethod
    def index_stock_cons_weight_csindex(symbol: str) -> pd.DataFrame:
        assert symbol == "000985"
        return pd.DataFrame(
            {
                "成分券代码": ["sh600000"],
                "成分券名称": ["浦发银行"],
                "交易所": ["上海证券交易所"],
            }
        )

    @staticmethod
    def stock_zh_a_spot_em() -> pd.DataFrame:
        return pd.DataFrame(
            {
                "代码": ["600000"],
                "名称": ["浦发银行"],
                "最新价": [10.0],
                "成交额": [88_000_000],
                "市盈率-动态": [8.5],
                "市净率": [0.8],
                "总市值": [600_000_000_000],
                "流通市值": [500_000_000_000],
            }
        )

    @staticmethod
    def stock_info_sh_name_code(symbol: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "证券代码": ["600000"],
                "上市日期": ["1999-11-10"],
            }
        )

    @staticmethod
    def stock_info_sz_name_code(symbol: str) -> pd.DataFrame:
        return pd.DataFrame(columns=["A股代码", "A股上市日期", "所属行业"])

    @staticmethod
    def stock_info_bj_name_code() -> pd.DataFrame:
        return pd.DataFrame(columns=["证券代码", "上市日期", "所属行业"])

    @staticmethod
    def stock_industry_clf_hist_sw() -> pd.DataFrame:
        return pd.DataFrame(
            {
                "symbol": ["600000"],
                "start_date": ["2021-07-30"],
                "industry_code": ["480301"],
            }
        )

    @staticmethod
    def stock_hk_index_cons_em(symbol: str) -> pd.DataFrame:
        return pd.DataFrame({"代码": ["00700"], "名称": ["腾讯控股"], "行业": ["HS_IT"]})

    @staticmethod
    def stock_ipo_hk_ths() -> pd.DataFrame:
        return pd.DataFrame({"代码": ["00700"], "上市日期": ["2004-06-16"]})

    @staticmethod
    def stock_zh_a_hist(
        symbol: str,
        period: str,
        start_date: str,
        end_date: str,
        adjust: str,
    ) -> pd.DataFrame:
        return _fake_hist(amount=90_000_000)

    @staticmethod
    def stock_hk_hist(
        symbol: str,
        period: str,
        start_date: str,
        end_date: str,
        adjust: str,
    ) -> pd.DataFrame:
        return _fake_hist(amount=80_000_000)

    @staticmethod
    def stock_financial_analysis_indicator(symbol: str, start_year: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "日期": ["2019-12-31", "2024-12-31"],
                "净资产收益率(%)": [11, 12],
                "销售毛利率(%)": [31, 32],
                "销售净利率(%)": [9, 10],
                "资产负债率(%)": [50, 49],
                "经营现金净流量(元)": [10_000_000_000, 15_000_000_000],
                "净利润(元)": [8_000_000_000, 10_000_000_000],
                "扣非净利润": [7_000_000_000, 9_000_000_000],
                "营业总收入": [100_000_000_000, 130_000_000_000],
            }
        )

    @staticmethod
    def stock_financial_hk_analysis_indicator_em(symbol: str, indicator: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "REPORT_DATE": ["2019-12-31", "2024-12-31"],
                "ROE_AVG": [20, 22],
                "GROSS_PROFIT_RATIO": [44, 45],
                "NET_PROFIT_RATIO": [24, 25],
                "DEBT_ASSET_RATIO": [42, 40],
                "PER_NETCASH_OPERATE": [3, 4],
                "HOLDER_PROFIT": [90_000_000_000, 110_000_000_000],
                "OPERATE_INCOME": [350_000_000_000, 600_000_000_000],
            }
        )

    @staticmethod
    def stock_hk_financial_indicator_em(symbol: str) -> pd.DataFrame:
        return pd.DataFrame({"已发行股本(股)": [9_500_000_000], "股息率TTM(%)": [1.2]})

    @staticmethod
    def stock_fhps_detail_em(symbol: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "除权除息日": ["2025-06-30"],
                "现金分红-股息率": [3.1],
            }
        )


def _fake_a_spot() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "code": ["600000"],
            "name_spot": ["浦发银行"],
            "latest_price": [10.0],
            "amount": [88_000_000],
            "pe_ttm": [8.5],
            "pb": [0.8],
            "total_market_cap": [600_000_000_000],
            "free_float_market_cap": [500_000_000_000],
        }
    )


def _fake_hk_spot() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "code": ["00700"],
            "name_spot": ["腾讯控股"],
            "latest_price": [400.0],
            "amount": [100_000_000],
            "pe_ttm": [18.0],
            "pb": [4.0],
            "total_market_cap": [3_800_000_000_000],
            "free_float_market_cap": [3_500_000_000_000],
        }
    )


def _raise_hk_spot_failure() -> pd.DataFrame:
    raise ConnectionError("HK push2 blocked")


def _fake_hist(amount: float) -> pd.DataFrame:
    dates = pd.bdate_range(end=pd.Timestamp(AS_OF), periods=20)
    return pd.DataFrame({"日期": dates, "成交额": amount})


class _FakeSinaHongKongAkShare:
    @staticmethod
    def stock_hk_spot() -> pd.DataFrame:
        return pd.DataFrame(
            {
                "代码": ["00700"],
                "中文名称": ["腾讯控股"],
                "最新价": [427.2],
                "成交额": [1_000_000_000],
            }
        )

    @staticmethod
    def stock_ipo_hk_ths() -> pd.DataFrame:
        return pd.DataFrame({"代码": ["00700"], "上市日期": ["2004-06-16"]})


class _ExplodingAkShare:
    def __getattr__(self, name: str):
        raise AssertionError(f"AkShare network method should not be called: {name}")
