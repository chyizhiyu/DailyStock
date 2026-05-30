from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from typing import Protocol

import pandas as pd

CodeList = Sequence[str] | None


class DataProvider(Protocol):
    def fetch_meta(self, as_of: date, markets: Sequence[str]) -> pd.DataFrame:
        """Return stock metadata for the requested markets."""

    def load_daily_bars(
        self,
        codes: CodeList,
        as_of: date,
        lookback_days: int = 20,
    ) -> pd.DataFrame:
        """Return daily bars with turnover amount for local liquidity checks."""

    def load_financials(self, codes: CodeList, as_of: date) -> pd.DataFrame:
        """Return historical financial statements."""

    def load_valuation_history(
        self,
        codes: CodeList,
        as_of: date,
        lookback_years: int = 5,
    ) -> pd.DataFrame:
        """Return valuation time series for industry percentile checks."""

    def load_dividends(self, codes: CodeList, as_of: date) -> pd.DataFrame:
        """Return dividend-yield records."""

    def load_free_cash_flow(self, codes: CodeList, as_of: date) -> pd.DataFrame:
        """Return free-cash-flow yield records."""


class DataProviderNotConfigured(RuntimeError):
    """Raised when an optional provider has not been configured."""

