from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from pathlib import Path

import pandas as pd


class SampleDataProvider:
    """CSV-backed provider used for tests and first-run smoke checks."""

    def __init__(self, data_dir: str | Path) -> None:
        self.data_dir = Path(data_dir)

    def fetch_meta(self, as_of: date, markets: Sequence[str]) -> pd.DataFrame:
        frame = self._read_csv("meta.csv", date_columns=["listing_date"])
        return frame.loc[frame["market"].isin(list(markets))].reset_index(drop=True)

    def load_daily_bars(
        self,
        codes: Sequence[str] | None,
        as_of: date,
        lookback_days: int = 20,
    ) -> pd.DataFrame:
        frame = self._read_csv("daily_bars.csv", date_columns=["trade_date"])
        frame = self._filter_codes(frame, codes)
        frame = frame.loc[frame["trade_date"] <= pd.Timestamp(as_of)]
        return (
            frame.sort_values(["code", "trade_date"])
            .groupby("code", group_keys=False)
            .tail(lookback_days)
            .reset_index(drop=True)
        )

    def load_financials(self, codes: Sequence[str] | None, as_of: date) -> pd.DataFrame:
        frame = self._read_csv("financials.csv")
        frame = self._filter_codes(frame, codes)
        return frame.loc[frame["fiscal_year"] <= as_of.year].reset_index(drop=True)

    def load_valuation_history(
        self,
        codes: Sequence[str] | None,
        as_of: date,
        lookback_years: int = 5,
    ) -> pd.DataFrame:
        frame = self._read_csv("valuation_history.csv", date_columns=["date"])
        frame = self._filter_codes(frame, codes)
        end = pd.Timestamp(as_of)
        start = end - pd.DateOffset(years=lookback_years)
        return frame.loc[(frame["date"] >= start) & (frame["date"] <= end)].reset_index(drop=True)

    def load_dividends(self, codes: Sequence[str] | None, as_of: date) -> pd.DataFrame:
        frame = self._read_csv("dividends.csv", date_columns=["date"])
        frame = self._filter_codes(frame, codes)
        return frame.loc[frame["date"] <= pd.Timestamp(as_of)].reset_index(drop=True)

    def load_free_cash_flow(self, codes: Sequence[str] | None, as_of: date) -> pd.DataFrame:
        frame = self._read_csv("free_cash_flow.csv", date_columns=["date"])
        frame = self._filter_codes(frame, codes)
        return frame.loc[frame["date"] <= pd.Timestamp(as_of)].reset_index(drop=True)

    def _read_csv(self, filename: str, date_columns: Sequence[str] = ()) -> pd.DataFrame:
        path = self.data_dir / filename
        frame = pd.read_csv(path)
        for column in date_columns:
            if column in frame:
                frame[column] = pd.to_datetime(frame[column])
        return frame

    @staticmethod
    def _filter_codes(frame: pd.DataFrame, codes: Sequence[str] | None) -> pd.DataFrame:
        if codes is None:
            return frame
        return frame.loc[frame["code"].isin(list(codes))].reset_index(drop=True)

