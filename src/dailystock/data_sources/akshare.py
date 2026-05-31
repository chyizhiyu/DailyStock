from __future__ import annotations

import logging
import os
import re
import threading
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from dailystock.config import project_root
from dailystock.data_sources.base import CodeList, DataProviderNotConfigured

logger = logging.getLogger(__name__)

CSI_ALL_SHARE = "000985"
DEFAULT_CACHE_DIR = project_root() / "data" / "cache" / "akshare"
DEFAULT_SEED_DIR = project_root() / "data" / "seed" / "akshare"
SINA_DAILY_LOCK = threading.Lock()
CN_BULK_FINANCIAL_LOOKBACK_YEARS = 6
CN_PER_STOCK_FINANCIAL_FALLBACK_LIMIT = 80
EMPTY_FINANCIAL_COLUMNS = [
    "code",
    "fiscal_year",
    "roe",
    "gross_margin",
    "net_margin",
    "debt_asset_ratio",
    "operating_cash_flow",
    "net_profit",
    "non_gaap_net_profit",
    "revenue",
]
EMPTY_VALUATION_COLUMNS = ["code", "date", "industry", "pe_ttm", "pb"]
EMPTY_DIVIDEND_COLUMNS = ["code", "date", "industry", "dividend_yield"]
EMPTY_FCF_COLUMNS = ["code", "date", "fcf_yield"]


class AkShareDataProvider:
    """AkShare-backed market data adapter.

    The pipeline consumes a small canonical schema. This provider keeps all
    AkShare/vendor-specific names and code formats at the boundary, then
    normalizes them before the local pandas filters run.
    """

    def __init__(
        self,
        cache_dir: str | Path | None = None,
        seed_dir: str | Path | None = None,
        ak_module: object | None = None,
        max_workers: int = 8,
        offline: bool | None = None,
        use_seed: bool = True,
    ) -> None:
        self.ak = ak_module or self._import_akshare()
        self.cache_dir = Path(cache_dir or DEFAULT_CACHE_DIR)
        self.seed_dir = Path(seed_dir or DEFAULT_SEED_DIR)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.max_workers = max(1, max_workers)
        self.use_seed = use_seed
        self.offline = (
            _truthy(os.environ.get("DAILYSTOCK_AKSHARE_OFFLINE"))
            if offline is None
            else offline
        )
        self._last_meta = pd.DataFrame()
        self._last_financials = pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)

    def fetch_meta(self, as_of: date, markets: Sequence[str]) -> pd.DataFrame:
        frames: list[pd.DataFrame] = []
        requested = {market.upper() for market in markets}
        if "CN" in requested:
            frames.append(self._fetch_cn_meta(as_of))
        if "HK" in requested:
            frames.append(self._fetch_hk_meta(as_of))
        if not frames:
            return pd.DataFrame()

        meta = pd.concat(frames, ignore_index=True)
        meta = meta.dropna(subset=["code"]).drop_duplicates(["market", "code"])
        meta["industry"] = meta["industry"].fillna(meta["market"].map(_unknown_industry))
        meta["listing_date"] = pd.to_datetime(
            meta["listing_date"].fillna("1900-01-01"),
            errors="coerce",
        ).fillna(pd.Timestamp("1900-01-01"))
        meta["total_market_cap"] = _numeric(meta["total_market_cap"])
        for column in [
            "is_st",
            "is_suspended",
            "is_penny_stock",
            "is_biotech_w",
            "is_profitable_biotech",
        ]:
            if column not in meta:
                meta[column] = False
            meta[column] = meta[column].fillna(False).astype(bool)
        self._last_meta = meta.reset_index(drop=True)
        return self._last_meta.copy()

    def load_daily_bars(
        self,
        codes: CodeList,
        as_of: date,
        lookback_days: int = 20,
    ) -> pd.DataFrame:
        code_list = self._resolve_codes(codes)
        start = as_of - timedelta(days=lookback_days)
        seed = self._load_seed_daily_bars(code_list, start=start, end=as_of)
        if self.offline:
            return seed
        present = set(seed["code"].astype(str)) if not seed.empty else set()
        missing_codes = [code for code in code_list if code not in present]
        frames = self._map_codes(
            missing_codes,
            lambda code: self._load_daily_bar_one(code, start=start, end=as_of),
        )
        if not seed.empty:
            frames.append(seed)
        if not frames:
            return pd.DataFrame(columns=["code", "trade_date", "amount"])
        return pd.concat(frames, ignore_index=True).sort_values(["code", "trade_date"])

    def load_financials(self, codes: CodeList, as_of: date) -> pd.DataFrame:
        code_list = self._resolve_codes(codes)
        seed = self._load_seed_financials(code_list, as_of)
        present = set(seed["code"].astype(str)) if not seed.empty else set()
        missing_codes = [code for code in code_list if code not in present]
        frames: list[pd.DataFrame] = []
        if not self.offline:
            cn_codes = [code for code in missing_codes if self._market_for_code(code) == "CN"]
            other_codes = [code for code in missing_codes if self._market_for_code(code) != "CN"]
            cn_bulk = self._load_cn_financials_bulk(cn_codes, as_of)
            if not cn_bulk.empty:
                frames.append(cn_bulk)
            bulk_present = set(cn_bulk["code"].astype(str)) if not cn_bulk.empty else set()
            cn_missing_after_bulk = [code for code in cn_codes if code not in bulk_present]
            fallback_limit = _per_stock_financial_fallback_limit()
            if cn_missing_after_bulk and len(cn_missing_after_bulk) <= fallback_limit:
                frames.extend(
                    self._map_codes(
                        cn_missing_after_bulk,
                        lambda code: self._load_financial_one(code, as_of),
                    )
                )
            elif cn_missing_after_bulk:
                logger.warning(
                    "Skipping %s CN per-stock financial fallbacks; bulk tables returned %s/%s "
                    "codes and DAILYSTOCK_AKSHARE_PER_STOCK_FINANCIAL_LIMIT=%s.",
                    len(cn_missing_after_bulk),
                    len(bulk_present),
                    len(cn_codes),
                    fallback_limit,
                )
            frames.extend(
                self._map_codes(
                    other_codes,
                    lambda code: self._load_financial_one(code, as_of),
                )
            )
        if not seed.empty:
            frames.append(seed)
        if not frames:
            financials = pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)
        else:
            financials = pd.concat(frames, ignore_index=True)
            financials = _ensure_columns(financials, EMPTY_FINANCIAL_COLUMNS)
            financials["fiscal_year"] = pd.to_numeric(financials["fiscal_year"], errors="coerce")
            financials = financials.loc[financials["fiscal_year"] <= as_of.year]
        self._last_financials = financials.reset_index(drop=True)
        return self._last_financials.copy()

    def load_valuation_history(
        self,
        codes: CodeList,
        as_of: date,
        lookback_years: int = 5,
    ) -> pd.DataFrame:
        start = pd.Timestamp(as_of) - pd.DateOffset(years=lookback_years)
        seed = self._load_seed_valuation_history(codes, as_of, lookback_years)
        cache_path = self._cache_path(
            "industry_valuation_history",
            start.strftime("%Y%m%d"),
            as_of.strftime("%Y%m%d"),
        )
        if codes is None and seed.empty and not self.offline:
            cached = self._read_cache(cache_path)
            if cached is not None:
                return _ensure_columns(cached, EMPTY_VALUATION_COLUMNS)

        code_list = self._resolve_codes(codes)
        present = set(seed["code"].astype(str)) if not seed.empty else set()
        missing_codes = [code for code in code_list if code not in present]
        frames: list[pd.DataFrame] = [seed] if not seed.empty else []
        if codes is not None and not self.offline:
            frames.extend(
                self._map_codes(
                    missing_codes,
                    lambda code: self._load_stock_valuation_history_one(
                        code,
                        as_of=as_of,
                        lookback_years=lookback_years,
                    ),
                )
            )

        current_snapshot = self._current_valuation_cross_section(as_of)
        if codes is not None:
            needed_industries = set(
                self._industry_for_code(code)
                for code in code_list
                if self._industry_for_code(code) is not None
            )
            current_snapshot = current_snapshot.loc[
                current_snapshot["industry"].isin(needed_industries)
            ]
        frames.append(current_snapshot)

        history = (
            pd.concat(frames, ignore_index=True)
            if frames
            else pd.DataFrame(columns=EMPTY_VALUATION_COLUMNS)
        )
        history = _ensure_columns(history, EMPTY_VALUATION_COLUMNS)
        history["date"] = pd.to_datetime(history["date"], errors="coerce")
        history["pe_ttm"] = _numeric(history["pe_ttm"])
        history["pb"] = _numeric(history["pb"])
        history = history.dropna(subset=["code", "date", "industry"])
        if codes is None:
            self._write_cache(cache_path, history)
        return history.reset_index(drop=True)

    def load_dividends(self, codes: CodeList, as_of: date) -> pd.DataFrame:
        code_list = self._resolve_codes(codes)
        seed = self._load_seed_dividends(code_list, as_of)
        present = set(seed["code"].astype(str)) if not seed.empty else set()
        missing_codes = [code for code in code_list if code not in present]
        frames = [] if self.offline else self._map_codes(
            missing_codes,
            lambda code: self._load_dividend_one(code, as_of),
        )
        if not seed.empty:
            frames.append(seed)
        if not frames:
            return pd.DataFrame(columns=EMPTY_DIVIDEND_COLUMNS)
        dividends = pd.concat(frames, ignore_index=True)
        dividends = _ensure_columns(dividends, EMPTY_DIVIDEND_COLUMNS)
        dividends["date"] = pd.to_datetime(dividends["date"], errors="coerce")
        dividends["dividend_yield"] = _percent_or_decimal(dividends["dividend_yield"])
        return dividends.dropna(subset=["code", "date"]).reset_index(drop=True)

    def load_free_cash_flow(self, codes: CodeList, as_of: date) -> pd.DataFrame:
        code_list = self._resolve_codes(codes)
        seed = self._load_seed_free_cash_flow(code_list, as_of)
        present = set(seed["code"].astype(str)) if not seed.empty else set()
        if self.offline or (code_list and set(code_list).issubset(present)):
            return seed
        financials = self._last_financials
        if financials.empty or not set(code_list).issubset(set(financials["code"].astype(str))):
            financials = self.load_financials(code_list, as_of)
        if financials.empty:
            return pd.DataFrame(columns=EMPTY_FCF_COLUMNS)

        latest = financials.sort_values(["code", "fiscal_year"]).groupby("code").tail(1)
        cap_map = self._last_meta.set_index("code")["total_market_cap"].to_dict()
        fcf = latest[["code", "operating_cash_flow"]].copy()
        fcf["date"] = pd.Timestamp(as_of)
        fcf["market_cap"] = _numeric(fcf["code"].map(cap_map))
        fcf["fcf_yield"] = _numeric(fcf["operating_cash_flow"]) / fcf["market_cap"]
        return fcf[["code", "date", "fcf_yield"]].reset_index(drop=True)

    @staticmethod
    def _import_akshare() -> object:
        try:
            import akshare as ak  # type: ignore[import-not-found]
        except ImportError as exc:
            raise DataProviderNotConfigured(
                "AkShare is required because config/default.yaml now uses data_source=akshare. "
                "Install project dependencies or run `pip install akshare tenacity requests`."
            ) from exc
        return ak

    def _load_seed_daily_bars(
        self,
        codes: Sequence[str],
        start: date,
        end: date,
    ) -> pd.DataFrame:
        seed = self._read_seed("daily_bars.csv")
        if seed is None:
            return pd.DataFrame(columns=["code", "trade_date", "amount"])
        frame = _ensure_columns(seed, ["code", "trade_date", "amount"])
        frame["code"] = frame["code"].map(self._normalize_known_code)
        frame["trade_date"] = pd.to_datetime(frame["trade_date"], errors="coerce")
        frame["amount"] = _numeric(frame["amount"])
        frame = frame.loc[
            frame["code"].isin(codes)
            & (frame["trade_date"] > pd.Timestamp(start))
            & (frame["trade_date"] <= pd.Timestamp(end))
        ]
        return frame.dropna(subset=["code", "trade_date"]).reset_index(drop=True)

    def _load_seed_financials(self, codes: Sequence[str], as_of: date) -> pd.DataFrame:
        seed = self._read_seed("financials.csv")
        if seed is None:
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)
        frame = _ensure_columns(seed, EMPTY_FINANCIAL_COLUMNS)
        frame["code"] = frame["code"].map(self._normalize_known_code)
        frame["fiscal_year"] = pd.to_numeric(frame["fiscal_year"], errors="coerce")
        for column in EMPTY_FINANCIAL_COLUMNS:
            if column not in {"code", "fiscal_year"}:
                frame[column] = _numeric(frame[column])
        return frame.loc[
            frame["code"].isin(codes) & (frame["fiscal_year"] <= as_of.year)
        ].reset_index(drop=True)

    def _load_seed_valuation_history(
        self,
        codes: CodeList,
        as_of: date,
        lookback_years: int,
    ) -> pd.DataFrame:
        seed = self._read_seed("valuation_history.csv")
        if seed is None:
            return pd.DataFrame(columns=EMPTY_VALUATION_COLUMNS)
        frame = _ensure_columns(seed, EMPTY_VALUATION_COLUMNS)
        frame["code"] = frame["code"].map(self._normalize_known_code)
        frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
        frame["pe_ttm"] = _numeric(frame["pe_ttm"])
        frame["pb"] = _numeric(frame["pb"])
        start = pd.Timestamp(as_of) - pd.DateOffset(years=lookback_years)
        frame = frame.loc[(frame["date"] >= start) & (frame["date"] <= pd.Timestamp(as_of))]
        if codes is not None:
            frame = frame.loc[frame["code"].isin(self._resolve_codes(codes))]
        return frame.dropna(subset=["code", "date", "industry"]).reset_index(drop=True)

    def _load_seed_dividends(self, codes: Sequence[str], as_of: date) -> pd.DataFrame:
        seed = self._read_seed("dividends.csv")
        if seed is None:
            return pd.DataFrame(columns=EMPTY_DIVIDEND_COLUMNS)
        frame = _ensure_columns(seed, EMPTY_DIVIDEND_COLUMNS)
        frame["code"] = frame["code"].map(self._normalize_known_code)
        frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
        frame["dividend_yield"] = _percent_or_decimal(frame["dividend_yield"])
        return frame.loc[
            frame["code"].isin(codes) & (frame["date"] <= pd.Timestamp(as_of))
        ].reset_index(drop=True)

    def _load_seed_free_cash_flow(self, codes: Sequence[str], as_of: date) -> pd.DataFrame:
        seed = self._read_seed("free_cash_flow.csv")
        if seed is None:
            return pd.DataFrame(columns=EMPTY_FCF_COLUMNS)
        frame = _ensure_columns(seed, EMPTY_FCF_COLUMNS)
        frame["code"] = frame["code"].map(self._normalize_known_code)
        frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
        frame["fcf_yield"] = _percent_or_decimal(frame["fcf_yield"])
        return frame.loc[
            frame["code"].isin(codes) & (frame["date"] <= pd.Timestamp(as_of))
        ].reset_index(drop=True)

    def _fetch_cn_meta(self, as_of: date) -> pd.DataFrame:
        constituents = self._load_cn_constituents(as_of)
        spot = self._load_a_spot(as_of)
        listing = self._load_a_listing_info(as_of)
        sw_industry = self._load_sw_industry_map(as_of)

        if constituents.empty and not spot.empty:
            constituents = spot[["code", "name_spot"]].rename(columns={"name_spot": "name"})
            constituents["exchange"] = constituents["code"].map(_cn_exchange)
            constituents["industry"] = pd.NA
        if constituents.empty:
            return pd.DataFrame(columns=_meta_columns())

        frame = constituents.merge(spot, on="code", how="left", suffixes=("", "_spot"))
        frame["name"] = frame["name"].combine_first(frame.get("name_spot"))
        frame = frame.merge(listing, on="code", how="left", suffixes=("", "_listing"))
        frame = frame.merge(sw_industry, on="code", how="left", suffixes=("", "_sw"))
        constituent_industry = frame.get("industry")
        frame["industry"] = (
            frame["industry_sw"]
            .combine_first(frame.get("industry_listing"))
            .combine_first(constituent_industry)
        )
        frame["industry"] = frame["industry"].fillna(_unknown_industry("CN"))
        frame["listing_date"] = frame["listing_date"].fillna("1900-01-01")
        frame["exchange"] = frame["exchange"].fillna(frame["code"].map(_cn_exchange))
        frame["market"] = "CN"
        frame["is_st"] = frame["name"].fillna("").astype(str).str.contains(r"\*?ST", case=False)
        frame["is_suspended"] = False
        frame["is_penny_stock"] = False
        frame["is_biotech_w"] = False
        frame["is_profitable_biotech"] = True
        return _ensure_columns(frame, _meta_columns())

    def _fetch_hk_meta(self, as_of: date) -> pd.DataFrame:
        spot = self._load_hk_spot(as_of)
        constituents = self._load_hk_hsci_constituents(as_of, spot)
        listing = self._load_hk_listing_info(as_of)
        frame = constituents.merge(spot, on="code", how="left", suffixes=("", "_spot"))
        frame["name"] = frame["name"].combine_first(frame.get("name_spot"))
        frame = frame.merge(listing, on="code", how="left", suffixes=("", "_listing"))
        frame["market"] = "HK"
        frame["exchange"] = "HKEX"
        frame["industry"] = frame["industry"].fillna(_unknown_industry("HK"))
        frame["listing_date"] = frame["listing_date"].fillna("1900-01-01")
        name = frame["name"].fillna("").astype(str).str.upper()
        code = frame["code"].fillna("").astype(str).str.upper()
        frame["is_st"] = False
        frame["is_suspended"] = _numeric(frame.get("latest_price")).isna() | _numeric(
            frame.get("amount")
        ).le(0)
        frame["is_penny_stock"] = _numeric(frame.get("latest_price")).lt(1)
        frame["is_biotech_w"] = (
            code.str.contains(r"(?:^|[-_.])W$", regex=True)
            | name.str.contains(r"(?:^|[\s\-_.(\[])(?:W|SS)(?:[\s\-_.),\]]|$)", regex=True)
        )
        frame["is_profitable_biotech"] = False
        return _ensure_columns(frame, _meta_columns())

    def _load_cn_constituents(self, as_of: date) -> pd.DataFrame:
        seed = self._read_seed("cn_constituents.csv")
        if seed is not None:
            return self._normalize_cn_constituents(seed)
        if self.offline:
            logger.warning("Offline mode enabled and cn_constituents.csv seed is missing.")
            return pd.DataFrame(columns=["code", "name", "exchange", "industry"])

        cache_path = self._cache_path("cn_constituents", CSI_ALL_SHARE, as_of.strftime("%Y%m%d"))
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached

        try:
            raw = self._call("index_stock_cons_weight_csindex", symbol=CSI_ALL_SHARE)
        except Exception as exc:
            logger.warning(
                "AkShare index_stock_cons_weight_csindex failed, falling back to "
                "index_stock_cons_csindex: %s",
                exc,
            )
            try:
                raw = self._call("index_stock_cons_csindex", symbol=CSI_ALL_SHARE)
            except Exception as fallback_exc:
                logger.warning("Failed to fetch CN constituents from AkShare: %s", fallback_exc)
                return pd.DataFrame(columns=["code", "name", "exchange", "industry"])

        frame = self._normalize_cn_constituents(raw)
        self._write_cache(cache_path, frame)
        return frame

    def _normalize_cn_constituents(self, raw: pd.DataFrame) -> pd.DataFrame:
        code = _coalesce(raw, ["code", "成分券代码", "证券代码", "品种代码", "代码"]).map(
            _normalize_cn_code
        )
        frame = pd.DataFrame(
            {
                "code": code,
                "name": _coalesce(raw, ["name", "成分券名称", "证券简称", "名称", "简称"]),
                "exchange": _coalesce(raw, ["exchange", "交易所"]).map(
                    _normalize_cn_exchange_name
                ),
                "industry": _coalesce(raw, ["industry", "行业", "行业分类"]).replace("", pd.NA),
            }
        ).dropna(subset=["code"])
        return frame

    def _load_a_spot(self, as_of: date) -> pd.DataFrame:
        seed = self._read_seed("a_spot.csv")
        if seed is not None:
            return self._normalize_a_spot(seed)
        if self.offline:
            logger.warning("Offline mode enabled and a_spot.csv seed is missing.")
            return pd.DataFrame(columns=_a_spot_columns())

        cache_path = self._cache_path("a_spot", as_of.strftime("%Y%m%d"))
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached

        try:
            raw = self._call("stock_zh_a_spot_em")
        except Exception as exc:
            logger.warning("AkShare stock_zh_a_spot_em failed, trying Sina fallback: %s", exc)
            try:
                raw = self._call("stock_zh_a_spot")
            except Exception as fallback_exc:
                logger.warning("Failed to fetch A-share spot snapshot: %s", fallback_exc)
                return pd.DataFrame(columns=_a_spot_columns())

        frame = self._normalize_a_spot(raw)
        self._write_cache(cache_path, frame)
        return frame

    def _normalize_a_spot(self, raw: pd.DataFrame) -> pd.DataFrame:
        frame = pd.DataFrame(
            {
                "code": _coalesce(raw, ["code", "代码"]).map(_normalize_cn_code),
                "name_spot": _coalesce(raw, ["name_spot", "名称", "简称"]),
                "latest_price": _numeric(_coalesce(raw, ["latest_price", "最新价"])),
                "amount": _numeric(_coalesce(raw, ["amount", "成交额"])),
                "pe_ttm": _numeric(_coalesce(raw, ["pe_ttm", "市盈率-TTM", "市盈率-动态", "per"])),
                "pb": _numeric(_coalesce(raw, ["pb", "市净率", "市净率-MRQ"])),
                "total_market_cap": _numeric(
                    _coalesce(raw, ["total_market_cap", "总市值", "mktcap"])
                ),
                "free_float_market_cap": _numeric(
                    _coalesce(raw, ["free_float_market_cap", "流通市值", "nmc"])
                ),
            }
        ).dropna(subset=["code"])
        return frame

    def _load_hk_spot(self, as_of: date) -> pd.DataFrame:
        seed = self._read_seed("hk_spot_full.csv")
        if seed is not None:
            return self._normalize_hk_spot(seed)
        if self.offline:
            logger.warning("Offline mode enabled and hk_spot_full.csv seed is missing.")
            return pd.DataFrame(columns=_a_spot_columns())

        cache_path = self._cache_path("hk_spot_full", as_of.strftime("%Y%m%d"))
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached

        try:
            frame = self._fetch_hk_spot_full_from_eastmoney()
        except Exception as exc:
            logger.warning("Full HK spot snapshot failed, falling back to AkShare columns: %s", exc)
            try:
                raw = self._call("stock_hk_spot_em")
                frame = self._normalize_hk_spot(raw)
            except Exception as fallback_exc:
                logger.warning("Failed to fetch HK spot snapshot: %s", fallback_exc)
                frame = pd.DataFrame(columns=_a_spot_columns())
        self._write_cache(cache_path, frame)
        return frame

    def _normalize_hk_spot(self, raw: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "code": _coalesce(raw, ["code", "代码"]).map(_normalize_hk_code),
                "name_spot": _coalesce(raw, ["name_spot", "名称", "中文名称"]),
                "latest_price": _numeric(_coalesce(raw, ["latest_price", "最新价"])),
                "amount": _numeric(_coalesce(raw, ["amount", "成交额"])),
                "pe_ttm": _numeric(_coalesce(raw, ["pe_ttm", "市盈率-TTM", "市盈率-动态"])),
                "pb": _numeric(_coalesce(raw, ["pb", "市净率", "市净率-MRQ"])),
                "total_market_cap": _numeric(_coalesce(raw, ["total_market_cap", "总市值"])),
                "free_float_market_cap": _numeric(
                    _coalesce(raw, ["free_float_market_cap", "流通市值"])
                ),
            }
        ).dropna(subset=["code"])

    def _fetch_hk_spot_full_from_eastmoney(self) -> pd.DataFrame:
        url = "https://72.push2.eastmoney.com/api/qt/clist/get"
        params = {
            "pn": "1",
            "pz": "200",
            "po": "1",
            "np": "1",
            "ut": "bd1d9ddb04089700cf9c27f6f7426281",
            "fltt": "2",
            "invt": "2",
            "fid": "f12",
            "fs": "m:128 t:3,m:128 t:4,m:128 t:1,m:128 t:2",
            "fields": "f2,f5,f6,f9,f12,f14,f18,f20,f21,f23",
        }
        raw = self._eastmoney_paginated(url, params)
        return pd.DataFrame(
            {
                "code": raw["f12"].map(_normalize_hk_code),
                "name_spot": raw["f14"],
                "latest_price": _numeric(raw["f2"]),
                "amount": _numeric(raw["f6"]),
                "pe_ttm": _numeric(raw["f9"]),
                "pb": _numeric(raw["f23"]),
                "total_market_cap": _numeric(raw["f20"]),
                "free_float_market_cap": _numeric(raw["f21"]),
            }
        ).dropna(subset=["code"])

    def _load_a_listing_info(self, as_of: date) -> pd.DataFrame:
        seed = self._read_seed("a_listing_info.csv")
        if seed is not None:
            return self._normalize_a_listing_info(seed)
        if self.offline:
            logger.warning("Offline mode enabled and a_listing_info.csv seed is missing.")
            return pd.DataFrame(columns=["code", "listing_date", "industry_listing"])

        cache_path = self._cache_path("a_listing_info", as_of.strftime("%Y%m%d"))
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached

        frames: list[pd.DataFrame] = []
        for symbol in ["主板A股", "科创板"]:
            try:
                raw = self._call("stock_info_sh_name_code", symbol=symbol)
            except Exception as exc:
                logger.warning("Failed to fetch SSE listing info %s: %s", symbol, exc)
                continue
            frames.append(
                pd.DataFrame(
                    {
                        "code": _coalesce(raw, ["证券代码"]).map(_normalize_cn_code),
                        "listing_date": _coalesce(raw, ["上市日期"]),
                        "industry_listing": pd.NA,
                    }
                )
            )

        try:
            raw = self._call("stock_info_sz_name_code", symbol="A股列表")
            frames.append(
                pd.DataFrame(
                    {
                        "code": _coalesce(raw, ["A股代码"]).map(_normalize_cn_code),
                        "listing_date": _coalesce(raw, ["A股上市日期"]),
                        "industry_listing": _coalesce(raw, ["所属行业"]),
                    }
                )
            )
        except Exception as exc:
            logger.warning("Failed to fetch SZSE listing info: %s", exc)

        try:
            raw = self._call("stock_info_bj_name_code")
            frames.append(
                pd.DataFrame(
                    {
                        "code": _coalesce(raw, ["证券代码"]).map(_normalize_cn_code),
                        "listing_date": _coalesce(raw, ["上市日期"]),
                        "industry_listing": _coalesce(raw, ["所属行业"]),
                    }
                )
            )
        except Exception as exc:
            logger.warning("Failed to fetch BSE listing info: %s", exc)

        frame = (
            pd.concat(frames, ignore_index=True)
            if frames
            else pd.DataFrame(columns=["code", "listing_date", "industry_listing"])
        )
        frame["listing_date"] = pd.to_datetime(frame["listing_date"], errors="coerce")
        frame = frame.dropna(subset=["code"]).drop_duplicates("code")
        self._write_cache(cache_path, frame)
        return frame

    def _normalize_a_listing_info(self, raw: pd.DataFrame) -> pd.DataFrame:
        frame = pd.DataFrame(
            {
                "code": _coalesce(raw, ["code", "证券代码", "A股代码"]).map(_normalize_cn_code),
                "listing_date": _coalesce(raw, ["listing_date", "上市日期", "A股上市日期"]),
                "industry_listing": _coalesce(raw, ["industry_listing", "所属行业"]),
            }
        )
        frame["listing_date"] = pd.to_datetime(frame["listing_date"], errors="coerce")
        return frame.dropna(subset=["code"]).drop_duplicates("code")

    def _load_sw_industry_map(self, as_of: date) -> pd.DataFrame:
        seed = self._read_seed("sw_industry.csv")
        if seed is not None:
            frame = _ensure_columns(seed, ["code", "industry_sw"])
            frame["code"] = frame["code"].map(_normalize_cn_code)
            return frame.dropna(subset=["code"]).drop_duplicates("code")
        if self.offline:
            logger.warning("Offline mode enabled and sw_industry.csv seed is missing.")
            return pd.DataFrame(columns=["code", "industry_sw"])

        cache_path = self._cache_path("sw_industry", as_of.strftime("%Y%m%d"))
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached

        try:
            raw = self._call("stock_industry_clf_hist_sw")
        except Exception as exc:
            logger.warning("Failed to fetch SW industry classification: %s", exc)
            return pd.DataFrame(columns=["code", "industry_sw"])

        frame = pd.DataFrame(
            {
                "code": _coalesce(raw, ["symbol", "股票代码"]).map(_normalize_cn_code),
                "start_date": pd.to_datetime(_coalesce(raw, ["start_date", "计入日期"])),
                "industry_sw": "SW_" + _coalesce(raw, ["industry_code", "行业代码"]).astype(str),
            }
        )
        frame = frame.loc[frame["start_date"] <= pd.Timestamp(as_of)]
        frame = frame.sort_values(["code", "start_date"]).groupby("code", as_index=False).tail(1)
        frame = frame[["code", "industry_sw"]].drop_duplicates("code")
        self._write_cache(cache_path, frame)
        return frame

    def _load_hk_hsci_constituents(self, as_of: date, spot: pd.DataFrame) -> pd.DataFrame:
        seed = self._read_seed("hk_hsci_constituents.csv")
        if seed is not None:
            return self._normalize_hk_constituents(seed)
        if self.offline:
            logger.warning("Offline mode enabled and hk_hsci_constituents.csv seed is missing.")
            if spot.empty:
                return pd.DataFrame(columns=["code", "name", "industry"])
            frame = spot[["code", "name_spot"]].rename(columns={"name_spot": "name"}).copy()
            frame["industry"] = _unknown_industry("HK")
            return frame

        cache_path = self._cache_path("hk_hsci_constituents", as_of.strftime("%Y%m%d"))
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached

        candidates = [
            ("stock_hk_index_cons_em", {"symbol": "恒生综合指数"}),
            ("stock_hk_index_cons_em", {"symbol": "HSCI"}),
            ("stock_hk_index_components_em", {"symbol": "恒生综合指数"}),
            ("stock_hk_index_cons_sina", {"symbol": "恒生综合指数"}),
        ]
        for function_name, kwargs in candidates:
            if not hasattr(self.ak, function_name):
                continue
            try:
                raw = self._call(function_name, **kwargs)
            except Exception as exc:
                logger.debug("HK HSCI constituent function %s failed: %s", function_name, exc)
                continue
            frame = self._normalize_hk_constituents(raw)
            if not frame.empty:
                self._write_cache(cache_path, frame)
                return frame

        logger.warning(
            "AkShare does not expose a stable HSCI constituent function in this environment; "
            "using full HK spot universe as the HK screening pool."
        )
        frame = spot[["code", "name_spot"]].rename(columns={"name_spot": "name"}).copy()
        frame["industry"] = _unknown_industry("HK")
        self._write_cache(cache_path, frame)
        return frame

    def _normalize_hk_constituents(self, raw: pd.DataFrame) -> pd.DataFrame:
        if raw.empty:
            return pd.DataFrame(columns=["code", "name", "industry"])
        frame = pd.DataFrame(
            {
                "code": _coalesce(raw, ["code", "代码", "成分券代码", "证券代码"]).map(
                    _normalize_hk_code
                ),
                "name": _coalesce(raw, ["name", "名称", "成分券名称", "证券简称", "中文名称"]),
                "industry": _coalesce(raw, ["industry", "行业", "恒生行业", "行业分类"]).replace(
                    "",
                    pd.NA,
                ),
            }
        )
        return frame.dropna(subset=["code"]).drop_duplicates("code")

    def _load_hk_listing_info(self, as_of: date) -> pd.DataFrame:
        seed = self._read_seed("hk_listing_info.csv")
        if seed is not None:
            return self._normalize_hk_listing_info(seed)
        if self.offline:
            logger.warning("Offline mode enabled and hk_listing_info.csv seed is missing.")
            return pd.DataFrame(columns=["code", "listing_date"])

        cache_path = self._cache_path("hk_listing_info", as_of.strftime("%Y%m%d"))
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached

        try:
            raw = self._call("stock_ipo_hk_ths")
        except Exception as exc:
            logger.warning("Failed to fetch HK IPO listing info: %s", exc)
            return pd.DataFrame(columns=["code", "listing_date"])

        frame = pd.DataFrame(
            {
                "code": _coalesce(raw, ["代码", "股票代码"]).map(_normalize_hk_code),
                "listing_date": _coalesce(raw, ["上市日期", "挂牌日期", "上市日"]),
            }
        )
        frame["listing_date"] = pd.to_datetime(frame["listing_date"], errors="coerce")
        frame = frame.dropna(subset=["code"]).drop_duplicates("code")
        self._write_cache(cache_path, frame)
        return frame

    def _normalize_hk_listing_info(self, raw: pd.DataFrame) -> pd.DataFrame:
        frame = pd.DataFrame(
            {
                "code": _coalesce(raw, ["code", "代码", "股票代码"]).map(_normalize_hk_code),
                "listing_date": _coalesce(raw, ["listing_date", "上市日期", "挂牌日期", "上市日"]),
            }
        )
        frame["listing_date"] = pd.to_datetime(frame["listing_date"], errors="coerce")
        return frame.dropna(subset=["code"]).drop_duplicates("code")

    def _load_daily_bar_one(self, code: str, start: date, end: date) -> pd.DataFrame:
        market = self._market_for_code(code)
        cache_path = self._cache_path(
            "daily",
            market,
            code,
            start.strftime("%Y%m%d"),
            end.strftime("%Y%m%d"),
        )
        cached = self._read_cache(cache_path)
        if cached is not None:
            for column in ["code", "trade_date", "amount"]:
                if column not in cached:
                    cached[column] = pd.NA
            return cached

        try:
            if market == "HK":
                try:
                    raw = self._call(
                        "stock_hk_hist",
                        symbol=_normalize_hk_code(code),
                        period="daily",
                        start_date=start.strftime("%Y%m%d"),
                        end_date=end.strftime("%Y%m%d"),
                        adjust="",
                    )
                except Exception as exc:
                    logger.debug(
                        "Eastmoney HK daily bars failed for %s, trying Sina daily: %s",
                        code,
                        exc,
                    )
                    with SINA_DAILY_LOCK:
                        raw = self._call(
                            "stock_hk_daily",
                            symbol=_normalize_hk_code(code),
                            adjust="",
                        )
                    raw_date = pd.to_datetime(_coalesce(raw, ["date", "日期"]), errors="coerce")
                    raw = raw.loc[
                        (raw_date >= pd.Timestamp(start)) & (raw_date <= pd.Timestamp(end))
                    ]
            else:
                try:
                    raw = self._call(
                        "stock_zh_a_hist",
                        symbol=_normalize_cn_code(code),
                        period="daily",
                        start_date=start.strftime("%Y%m%d"),
                        end_date=end.strftime("%Y%m%d"),
                        adjust="",
                    )
                except Exception as exc:
                    logger.debug(
                        "Eastmoney daily bars failed for %s, trying Sina daily: %s",
                        code,
                        exc,
                    )
                    with SINA_DAILY_LOCK:
                        raw = self._call(
                            "stock_zh_a_daily",
                            symbol=_cn_sina_symbol(code),
                            adjust="",
                        )
                    raw_date = pd.to_datetime(_coalesce(raw, ["date", "日期"]), errors="coerce")
                    raw = raw.loc[
                        (raw_date >= pd.Timestamp(start)) & (raw_date <= pd.Timestamp(end))
                    ]
        except Exception as exc:
            logger.warning("Failed to fetch daily bars for %s: %s", code, exc)
            return pd.DataFrame(columns=["code", "trade_date", "amount"])

        frame = pd.DataFrame(
            {
                "code": code,
                "trade_date": pd.to_datetime(_coalesce(raw, ["日期", "date"])),
                "amount": _numeric(_coalesce(raw, ["成交额", "amount"])),
                "close": _numeric(_coalesce(raw, ["收盘", "close"])),
                "outstanding_share": _numeric(_coalesce(raw, ["outstanding_share"])),
            }
        ).dropna(subset=["trade_date"])
        self._write_cache(cache_path, frame)
        return frame

    def _load_financial_one(self, code: str, as_of: date) -> pd.DataFrame:
        market = self._market_for_code(code)
        cache_path = self._cache_path("financials", market, code, as_of.year)
        cached = self._read_cache(cache_path)
        if cached is not None:
            return _ensure_columns(cached, EMPTY_FINANCIAL_COLUMNS)

        try:
            if market == "HK":
                frame = self._fetch_hk_financials(code, as_of)
            else:
                frame = self._fetch_cn_financials(code, as_of)
        except Exception as exc:
            logger.warning("Failed to fetch financials for %s: %s", code, exc)
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)

        frame = _ensure_columns(frame, EMPTY_FINANCIAL_COLUMNS)
        frame = frame.dropna(subset=["code", "fiscal_year"])
        self._write_cache(cache_path, frame)
        return frame

    def _load_cn_financials_bulk(self, codes: Sequence[str], as_of: date) -> pd.DataFrame:
        if not codes:
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)

        latest_year = as_of.year - 1
        start_year = max(1990, latest_year - CN_BULK_FINANCIAL_LOOKBACK_YEARS)
        cache_path = self._cache_path("cn_financials_bulk", start_year, latest_year, as_of.year)
        cached = self._read_cache(cache_path)
        if cached is not None:
            financials = _ensure_columns(cached, EMPTY_FINANCIAL_COLUMNS)
            return financials.loc[financials["code"].astype(str).isin(set(codes))].reset_index(
                drop=True
            )

        frames: list[pd.DataFrame] = []
        for fiscal_year in range(start_year, latest_year + 1):
            year_frame = self._load_cn_financials_bulk_year(fiscal_year, as_of)
            if not year_frame.empty:
                frames.append(year_frame)

        if not frames:
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)

        financials = pd.concat(frames, ignore_index=True)
        financials = _ensure_columns(financials, EMPTY_FINANCIAL_COLUMNS)
        financials = financials.sort_values(["code", "fiscal_year"]).drop_duplicates(
            ["code", "fiscal_year"],
            keep="last",
        )
        self._write_cache(cache_path, financials)
        return financials.loc[financials["code"].astype(str).isin(set(codes))].reset_index(
            drop=True
        )

    def _load_cn_financials_bulk_year(self, fiscal_year: int, as_of: date) -> pd.DataFrame:
        date_key = f"{fiscal_year}1231"
        yjbb = self._load_cn_annual_table("yjbb", "stock_yjbb_em", date_key)
        if yjbb.empty:
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)

        metrics = _normalize_cn_yjbb_table(yjbb, fiscal_year, as_of)
        if metrics.empty:
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)

        cash = _normalize_cn_xjll_table(
            self._load_cn_annual_table("xjll", "stock_xjll_em", date_key),
            fiscal_year,
            as_of,
        )
        debt = _normalize_cn_zcfz_table(
            self._load_cn_annual_table("zcfz", "stock_zcfz_em", date_key),
            fiscal_year,
            as_of,
        )
        frame = metrics.merge(cash, on=["code", "fiscal_year"], how="left")
        frame = frame.merge(debt, on=["code", "fiscal_year"], how="left")
        frame["debt_asset_ratio"] = frame["debt_asset_ratio"].combine_first(
            frame["debt_asset_ratio_from_yjbb"]
        )
        frame["non_gaap_net_profit"] = frame["net_profit"]
        return _ensure_columns(frame, EMPTY_FINANCIAL_COLUMNS).reset_index(drop=True)

    def _load_cn_annual_table(
        self,
        table_name: str,
        function_name: str,
        date_key: str,
    ) -> pd.DataFrame:
        cache_path = self._cache_path("cn_annual", table_name, date_key)
        cached = self._read_cache(cache_path)
        if cached is not None:
            return cached
        try:
            frame = self._call(function_name, date=date_key)
        except Exception as exc:
            logger.warning(
                "Failed to fetch CN annual %s table for %s: %s",
                table_name,
                date_key,
                exc,
            )
            return pd.DataFrame()
        self._write_cache(cache_path, frame)
        return frame

    def _fetch_cn_financials(self, code: str, as_of: date) -> pd.DataFrame:
        start_year = str(max(1900, as_of.year - 6))
        raw = self._call("stock_financial_analysis_indicator", symbol=code, start_year=start_year)
        frame = self._normalize_cn_financial_indicator(code, raw)
        amounts = self._fetch_cn_financial_amounts(code)
        if not amounts.empty:
            frame = frame.merge(
                amounts,
                on=["code", "fiscal_year"],
                how="outer",
                suffixes=("", "_a"),
            )
            for column in ["operating_cash_flow", "net_profit", "non_gaap_net_profit", "revenue"]:
                frame[column] = frame[column].combine_first(frame.get(f"{column}_a"))
        return frame

    def _normalize_cn_financial_indicator(self, code: str, raw: pd.DataFrame) -> pd.DataFrame:
        if raw.empty:
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)
        report_date = pd.to_datetime(_coalesce(raw, ["日期", "报告期", "REPORT_DATE"]))
        frame = pd.DataFrame(
            {
                "code": code,
                "report_date": report_date,
                "fiscal_year": report_date.dt.year,
                "roe": _percent_or_decimal(
                    _coalesce(raw, ["净资产收益率(%)", "净资产收益率", "加权净资产收益率(%)"])
                ),
                "gross_margin": _percent_or_decimal(
                    _coalesce(raw, ["销售毛利率(%)", "毛利率(%)", "销售毛利率"])
                ),
                "net_margin": _percent_or_decimal(
                    _coalesce(raw, ["销售净利率(%)", "净利率(%)", "销售净利率"])
                ),
                "debt_asset_ratio": _percent_or_decimal(
                    _coalesce(raw, ["资产负债率(%)", "资产负债率"])
                ),
                "operating_cash_flow": _numeric(
                    _coalesce(raw, ["经营现金净流量(元)", "经营活动产生的现金流量净额"])
                ),
                "net_profit": _numeric(
                    _coalesce(raw, ["净利润(元)", "净利润", "归属于母公司所有者的净利润"])
                ),
                "non_gaap_net_profit": _numeric(
                    _coalesce(raw, ["扣除非经常性损益后的净利润", "扣非净利润", "净利润(元)"])
                ),
                "revenue": _numeric(_coalesce(raw, ["主营业务收入(元)", "营业总收入", "营业收入"])),
            }
        )
        frame = _annual_rows(frame)
        return frame[EMPTY_FINANCIAL_COLUMNS]

    def _fetch_cn_financial_amounts(self, code: str) -> pd.DataFrame:
        frames: list[pd.DataFrame] = []
        try:
            raw = self._call("stock_financial_benefit_ths", symbol=code, indicator="按年度")
            frames.append(
                _normalize_financial_amount_table(
                    code,
                    raw,
                    {
                        "revenue": ["营业总收入", "营业收入", "主营业务收入"],
                        "net_profit": ["净利润", "归母净利润"],
                        "non_gaap_net_profit": ["扣非净利润", "扣除非经常性损益后的净利润"],
                    },
                )
            )
        except Exception as exc:
            logger.debug("Failed to fetch CN income statement for %s: %s", code, exc)
        try:
            raw = self._call("stock_financial_cash_ths", symbol=code, indicator="按年度")
            frames.append(
                _normalize_financial_amount_table(
                    code,
                    raw,
                    {
                        "operating_cash_flow": [
                            "经营活动产生的现金流量净额",
                            "经营性现金流量净额",
                            "经营现金流量净额",
                        ],
                    },
                )
            )
        except Exception as exc:
            logger.debug("Failed to fetch CN cash-flow statement for %s: %s", code, exc)
        if not frames:
            return pd.DataFrame()
        out = frames[0]
        for frame in frames[1:]:
            out = out.merge(frame, on=["code", "fiscal_year"], how="outer")
        return out

    def _fetch_hk_financials(self, code: str, as_of: date) -> pd.DataFrame:
        raw = self._call("stock_financial_hk_analysis_indicator_em", symbol=code, indicator="年度")
        if raw.empty:
            return pd.DataFrame(columns=EMPTY_FINANCIAL_COLUMNS)
        report_date = pd.to_datetime(_coalesce(raw, ["REPORT_DATE", "报告日期"]))
        shares = self._hk_issued_shares(code)
        frame = pd.DataFrame(
            {
                "code": code,
                "report_date": report_date,
                "fiscal_year": report_date.dt.year,
                "roe": _percent_or_decimal(_coalesce(raw, ["ROE_AVG", "ROE_YEARLY"])),
                "gross_margin": _percent_or_decimal(_coalesce(raw, ["GROSS_PROFIT_RATIO"])),
                "net_margin": _percent_or_decimal(_coalesce(raw, ["NET_PROFIT_RATIO"])),
                "debt_asset_ratio": _percent_or_decimal(_coalesce(raw, ["DEBT_ASSET_RATIO"])),
                "operating_cash_flow": _numeric(_coalesce(raw, ["PER_NETCASH_OPERATE"]))
                * shares,
                "net_profit": _numeric(_coalesce(raw, ["HOLDER_PROFIT"])),
                "non_gaap_net_profit": _numeric(_coalesce(raw, ["HOLDER_PROFIT"])),
                "revenue": _numeric(_coalesce(raw, ["OPERATE_INCOME"])),
            }
        )
        frame = _annual_rows(frame)
        return frame[EMPTY_FINANCIAL_COLUMNS]

    def _hk_issued_shares(self, code: str) -> float:
        try:
            raw = self._call("stock_hk_financial_indicator_em", symbol=code)
        except Exception:
            return 1.0
        shares = _numeric(_coalesce(raw, ["已发行股本(股)", "ISSUED_COMMON_SHARES"]))
        return float(shares.dropna().iloc[0]) if not shares.dropna().empty else 1.0

    def _load_stock_valuation_history_one(
        self,
        code: str,
        as_of: date,
        lookback_years: int,
    ) -> pd.DataFrame:
        market = self._market_for_code(code)
        cache_path = self._cache_path("valuation", market, code, lookback_years, as_of.year)
        cached = self._read_cache(cache_path)
        if cached is not None:
            return _ensure_columns(cached, EMPTY_VALUATION_COLUMNS)

        try:
            period = "近五年" if market == "CN" else "全部"
            fn_name = "stock_zh_valuation_baidu" if market == "CN" else "stock_hk_valuation_baidu"
            pe = self._call(fn_name, symbol=code, indicator="市盈率(TTM)", period=period)
            pb = self._call(fn_name, symbol=code, indicator="市净率", period=period)
        except Exception as exc:
            logger.debug("Failed to fetch valuation history for %s: %s", code, exc)
            return pd.DataFrame(columns=EMPTY_VALUATION_COLUMNS)

        pe_frame = pe.rename(columns={"value": "pe_ttm"})[["date", "pe_ttm"]]
        pb_frame = pb.rename(columns={"value": "pb"})[["date", "pb"]]
        frame = pe_frame.merge(pb_frame, on="date", how="outer")
        frame["code"] = code
        frame["industry"] = self._industry_for_code(code) or _unknown_industry(market)
        frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
        start = pd.Timestamp(as_of) - pd.DateOffset(years=lookback_years)
        frame = frame.loc[(frame["date"] >= start) & (frame["date"] <= pd.Timestamp(as_of))]
        frame = frame[EMPTY_VALUATION_COLUMNS]
        self._write_cache(cache_path, frame)
        return frame

    def _current_valuation_cross_section(self, as_of: date) -> pd.DataFrame:
        if self._last_meta.empty:
            return pd.DataFrame(columns=EMPTY_VALUATION_COLUMNS)
        frame = self._last_meta.copy()
        for column in ["pe_ttm", "pb"]:
            if column not in frame:
                frame[column] = pd.NA
        return pd.DataFrame(
            {
                "code": frame["code"],
                "date": pd.Timestamp(as_of),
                "industry": frame["industry"],
                "pe_ttm": _numeric(frame["pe_ttm"]),
                "pb": _numeric(frame["pb"]),
            }
        ).dropna(subset=["pe_ttm", "pb"], how="all")

    def _load_dividend_one(self, code: str, as_of: date) -> pd.DataFrame:
        market = self._market_for_code(code)
        cache_path = self._cache_path("dividend", market, code, as_of.year)
        cached = self._read_cache(cache_path)
        if cached is not None:
            return _ensure_columns(cached, EMPTY_DIVIDEND_COLUMNS)

        try:
            if market == "HK":
                frame = self._fetch_hk_dividend(code, as_of)
            else:
                frame = self._fetch_cn_dividend(code, as_of)
        except Exception as exc:
            logger.debug("Failed to fetch dividend yield for %s: %s", code, exc)
            frame = pd.DataFrame(columns=EMPTY_DIVIDEND_COLUMNS)
        self._write_cache(cache_path, frame)
        return frame

    def _fetch_cn_dividend(self, code: str, as_of: date) -> pd.DataFrame:
        raw = self._call("stock_fhps_detail_em", symbol=code)
        if raw.empty:
            return pd.DataFrame(columns=EMPTY_DIVIDEND_COLUMNS)
        date_series = pd.to_datetime(_coalesce(raw, ["除权除息日", "最新公告日期", "报告期"]))
        frame = pd.DataFrame(
            {
                "code": code,
                "date": date_series,
                "industry": self._industry_for_code(code) or _unknown_industry("CN"),
                "dividend_yield": _percent_or_decimal(_coalesce(raw, ["现金分红-股息率"])),
            }
        )
        frame = frame.loc[frame["date"] <= pd.Timestamp(as_of)]
        return frame.sort_values("date").tail(1)

    def _fetch_hk_dividend(self, code: str, as_of: date) -> pd.DataFrame:
        raw = self._call("stock_hk_financial_indicator_em", symbol=code)
        yield_series = _percent_or_decimal(_coalesce(raw, ["股息率TTM(%)", "DIVIDEND_RATE"]))
        dividend_yield = yield_series.dropna().iloc[0] if not yield_series.dropna().empty else pd.NA
        return pd.DataFrame(
            {
                "code": [code],
                "date": [pd.Timestamp(as_of)],
                "industry": [self._industry_for_code(code) or _unknown_industry("HK")],
                "dividend_yield": [dividend_yield],
            }
        )

    def _resolve_codes(self, codes: CodeList) -> list[str]:
        if codes is not None:
            return [self._normalize_known_code(code) for code in codes]
        if not self._last_meta.empty:
            return self._last_meta["code"].astype(str).tolist()
        return []

    def _normalize_known_code(self, code: str) -> str:
        text = str(code)
        market = self._market_for_code(text)
        return _normalize_hk_code(text) if market == "HK" else _normalize_cn_code(text)

    def _market_for_code(self, code: str) -> str:
        if not self._last_meta.empty:
            match = self._last_meta.loc[self._last_meta["code"].astype(str) == str(code)]
            if not match.empty:
                return str(match.iloc[0]["market"]).upper()
        digits = re.sub(r"\D", "", str(code))
        return "HK" if len(digits) == 5 else "CN"

    def _industry_for_code(self, code: str) -> str | None:
        if self._last_meta.empty:
            return None
        match = self._last_meta.loc[self._last_meta["code"].astype(str) == str(code)]
        if match.empty:
            return None
        value = match.iloc[0].get("industry")
        return str(value) if pd.notna(value) else None

    def _map_codes(
        self,
        codes: Sequence[str],
        function: Callable[[str], pd.DataFrame],
    ) -> list[pd.DataFrame]:
        if not codes:
            return []
        workers = min(self.max_workers, len(codes))
        frames: list[pd.DataFrame] = []
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(function, code): code for code in codes}
            for future in as_completed(futures):
                code = futures[future]
                try:
                    frame = future.result()
                except Exception as exc:
                    logger.warning("AkShare task failed for %s: %s", code, exc)
                    continue
                if not frame.empty:
                    frames.append(frame)
        return frames

    def _call(self, function_name: str, **kwargs: Any) -> pd.DataFrame:
        function = getattr(self.ak, function_name)
        result = _call_with_retry(function, **kwargs)
        return result if isinstance(result, pd.DataFrame) else pd.DataFrame(result)

    def _eastmoney_paginated(self, url: str, params: dict[str, str]) -> pd.DataFrame:
        page = 1
        page_size = int(params.get("pz", "200"))
        frames: list[pd.DataFrame] = []
        while True:
            page_params = params | {"pn": str(page), "pz": str(page_size)}
            payload = _get_json_with_retry(url, page_params)
            data = payload.get("data") or {}
            rows = data.get("diff") or []
            if not rows:
                break
            frames.append(pd.DataFrame(rows))
            total = int(data.get("total") or len(rows))
            if page * page_size >= total:
                break
            page += 1
        if not frames:
            return pd.DataFrame()
        return pd.concat(frames, ignore_index=True)

    def _cache_path(self, *parts: object) -> Path:
        key = "_".join(_slug(str(part)) for part in parts)
        return self.cache_dir / f"{key}.csv"

    def _read_seed(self, filename: str) -> pd.DataFrame | None:
        if not self.use_seed:
            return None
        path = self.seed_dir / filename
        if not path.exists() or path.stat().st_size == 0:
            return None
        logger.info("Using AkShare seed file: %s", path)
        return pd.read_csv(path, dtype=str, low_memory=False)

    @staticmethod
    def _read_cache(path: Path) -> pd.DataFrame | None:
        if not path.exists() or path.stat().st_size == 0:
            return None
        return pd.read_csv(path, dtype=str, low_memory=False)

    @staticmethod
    def _write_cache(path: Path, frame: pd.DataFrame) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(path, index=False)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type(Exception),
    reraise=True,
)
def _call_with_retry(function: Callable[..., Any], **kwargs: Any) -> Any:
    return function(**kwargs)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type((requests.RequestException, ValueError)),
    reraise=True,
)
def _get_json_with_retry(url: str, params: dict[str, str]) -> dict[str, Any]:
    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("Expected JSON object from Eastmoney")
    return payload


def _normalize_cn_code(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip().upper()
    matches = re.findall(r"\d{6}", text)
    if matches:
        return matches[-1]
    digits = re.sub(r"\D", "", text)
    return digits[-6:].zfill(6) if digits else ""


def _normalize_hk_code(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip().upper()
    matches = re.findall(r"\d{1,5}", text)
    if not matches:
        return ""
    return matches[-1][-5:].zfill(5)


def _normalize_cn_exchange_name(value: object) -> str | None:
    if pd.isna(value):
        return None
    text = str(value)
    if "上海" in text or "SSE" in text.upper():
        return "SSE"
    if "深圳" in text or "SZSE" in text.upper():
        return "SZSE"
    if "北京" in text or "BSE" in text.upper():
        return "BSE"
    return None


def _cn_exchange(code: str) -> str:
    if code.startswith(("6", "9")):
        return "SSE"
    if code.startswith(("8", "4")):
        return "BSE"
    return "SZSE"


def _cn_sina_symbol(code: str) -> str:
    normalized = _normalize_cn_code(code)
    exchange = _cn_exchange(normalized)
    prefix = "sh" if exchange == "SSE" else "bj" if exchange == "BSE" else "sz"
    return f"{prefix}{normalized}"


def _coalesce(frame: pd.DataFrame, columns: Sequence[str]) -> pd.Series:
    if frame is None or frame.empty:
        return pd.Series(dtype=object)
    available = [frame[column].astype(object) for column in columns if column in frame]
    if not available:
        return pd.Series(pd.NA, index=frame.index, dtype=object)
    series = available[0]
    for column in available[1:]:
        series = series.combine_first(column)
    return series


def _numeric(values: object) -> pd.Series:
    if isinstance(values, pd.Series):
        series = values
    else:
        series = pd.Series(values)
    text = series.astype(str).str.replace(",", "", regex=False).str.strip()
    multiplier = pd.Series(1.0, index=series.index)
    multiplier = multiplier.mask(text.str.contains("亿", na=False), 100_000_000.0)
    multiplier = multiplier.mask(text.str.contains("万", na=False), 10_000.0)
    numeric = pd.to_numeric(
        text.str.replace(r"[%亿万港元人民币元股]", "", regex=True),
        errors="coerce",
    )
    return numeric * multiplier


def _percent_or_decimal(values: object) -> pd.Series:
    numeric = _numeric(values)
    non_null = numeric.dropna().abs()
    if not non_null.empty and non_null.median() > 1:
        numeric = numeric / 100
    return numeric


def _annual_rows(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame
    out = frame.copy()
    out["report_date"] = pd.to_datetime(out["report_date"], errors="coerce")
    annual = out.loc[out["report_date"].dt.month.eq(12) & out["report_date"].dt.day.eq(31)]
    if annual.empty:
        annual = out.sort_values(["code", "report_date"]).groupby(["code", "fiscal_year"]).tail(1)
    annual = annual.sort_values(["code", "fiscal_year"]).drop_duplicates(["code", "fiscal_year"])
    return annual.drop(columns=["report_date"], errors="ignore")


def _normalize_cn_yjbb_table(
    raw: pd.DataFrame,
    fiscal_year: int,
    as_of: date,
) -> pd.DataFrame:
    if raw.empty:
        return pd.DataFrame()
    frame = pd.DataFrame(
        {
            "code": _coalesce(raw, ["股票代码", "代码", "SECURITY_CODE"]).map(_normalize_cn_code),
            "fiscal_year": fiscal_year,
            "roe": _percent_or_decimal(_coalesce(raw, ["净资产收益率", "ROE"])),
            "gross_margin": _percent_or_decimal(_coalesce(raw, ["销售毛利率", "毛利率"])),
            "revenue": _numeric(
                _coalesce(raw, ["营业总收入-营业总收入", "营业总收入", "OPERATE_INCOME"])
            ),
            "net_profit": _numeric(_coalesce(raw, ["净利润-净利润", "净利润", "PARENT_NETPROFIT"])),
            "operating_cash_flow_per_share": _numeric(
                _coalesce(raw, ["每股经营现金流量", "每股经营现金流"])
            ),
            "debt_asset_ratio_from_yjbb": _percent_or_decimal(
                _coalesce(raw, ["资产负债率", "资产负债率(%)"])
            ),
            "report_date": pd.to_datetime(
                _coalesce(raw, ["最新公告日期", "公告日期", "NOTICE_DATE"]),
                errors="coerce",
            ),
        }
    )
    frame = _filter_reported_rows(frame, as_of)
    frame["net_margin"] = pd.NA
    valid_revenue = frame["revenue"].notna() & frame["revenue"].ne(0)
    frame.loc[valid_revenue, "net_margin"] = (
        frame.loc[valid_revenue, "net_profit"] / frame.loc[valid_revenue, "revenue"]
    )
    return frame.drop(columns=["report_date"], errors="ignore")


def _normalize_cn_xjll_table(
    raw: pd.DataFrame,
    fiscal_year: int,
    as_of: date,
) -> pd.DataFrame:
    if raw.empty:
        return pd.DataFrame(columns=["code", "fiscal_year", "operating_cash_flow"])
    frame = pd.DataFrame(
        {
            "code": _coalesce(raw, ["股票代码", "代码", "SECURITY_CODE"]).map(_normalize_cn_code),
            "fiscal_year": fiscal_year,
            "operating_cash_flow": _numeric(
                _coalesce(raw, ["经营性现金流-现金流量净额", "经营活动产生的现金流量净额"])
            ),
            "report_date": pd.to_datetime(
                _coalesce(raw, ["公告日期", "最新公告日期", "NOTICE_DATE"]),
                errors="coerce",
            ),
        }
    )
    frame = _filter_reported_rows(frame, as_of)
    return frame[["code", "fiscal_year", "operating_cash_flow"]]


def _normalize_cn_zcfz_table(
    raw: pd.DataFrame,
    fiscal_year: int,
    as_of: date,
) -> pd.DataFrame:
    if raw.empty:
        return pd.DataFrame(columns=["code", "fiscal_year", "debt_asset_ratio"])
    frame = pd.DataFrame(
        {
            "code": _coalesce(raw, ["股票代码", "代码", "SECURITY_CODE"]).map(_normalize_cn_code),
            "fiscal_year": fiscal_year,
            "debt_asset_ratio": _percent_or_decimal(_coalesce(raw, ["资产负债率"])),
            "report_date": pd.to_datetime(
                _coalesce(raw, ["公告日期", "最新公告日期", "NOTICE_DATE"]),
                errors="coerce",
            ),
        }
    )
    frame = _filter_reported_rows(frame, as_of)
    return frame[["code", "fiscal_year", "debt_asset_ratio"]]


def _filter_reported_rows(frame: pd.DataFrame, as_of: date) -> pd.DataFrame:
    if frame.empty:
        return frame
    out = frame.dropna(subset=["code"]).copy()
    reported = out["report_date"].isna() | (out["report_date"] <= pd.Timestamp(as_of))
    out = out.loc[reported & out["code"].ne("")]
    return out.sort_values(["code", "report_date"]).drop_duplicates(
        ["code", "fiscal_year"],
        keep="last",
    )


def _normalize_financial_amount_table(
    code: str,
    raw: pd.DataFrame,
    mapping: dict[str, Sequence[str]],
) -> pd.DataFrame:
    if raw.empty:
        return pd.DataFrame()
    date_series = pd.to_datetime(_coalesce(raw, ["报告期", "report_date", "日期"]), errors="coerce")
    frame = pd.DataFrame({"code": code, "fiscal_year": date_series.dt.year})
    for target, candidates in mapping.items():
        frame[target] = _numeric(_coalesce(raw, candidates))
    frame = frame.dropna(subset=["fiscal_year"])
    return frame.sort_values("fiscal_year").drop_duplicates(["code", "fiscal_year"])


def _ensure_columns(frame: pd.DataFrame, columns: Sequence[str]) -> pd.DataFrame:
    out = frame.copy()
    for column in columns:
        if column not in out:
            out[column] = pd.NA
    return out[list(columns)]


def _meta_columns() -> list[str]:
    return [
        "code",
        "name",
        "market",
        "exchange",
        "industry",
        "is_st",
        "listing_date",
        "total_market_cap",
        "free_float_market_cap",
        "latest_price",
        "amount",
        "pe_ttm",
        "pb",
        "is_suspended",
        "is_penny_stock",
        "is_biotech_w",
        "is_profitable_biotech",
    ]


def _a_spot_columns() -> list[str]:
    return [
        "code",
        "name_spot",
        "latest_price",
        "amount",
        "pe_ttm",
        "pb",
        "total_market_cap",
        "free_float_market_cap",
    ]


def _unknown_industry(market: str) -> str:
    return "SW_UNKNOWN" if str(market).upper() == "CN" else "HS_UNKNOWN"


def _truthy(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def _per_stock_financial_fallback_limit() -> int:
    raw = os.environ.get("DAILYSTOCK_AKSHARE_PER_STOCK_FINANCIAL_LIMIT")
    if raw is None:
        return CN_PER_STOCK_FINANCIAL_FALLBACK_LIMIT
    try:
        return max(0, int(raw))
    except ValueError:
        logger.warning(
            "Invalid DAILYSTOCK_AKSHARE_PER_STOCK_FINANCIAL_LIMIT=%r; using %s.",
            raw,
            CN_PER_STOCK_FINANCIAL_FALLBACK_LIMIT,
        )
        return CN_PER_STOCK_FINANCIAL_FALLBACK_LIMIT


def _slug(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z_.-]+", "-", value).strip("-") or "cache"
