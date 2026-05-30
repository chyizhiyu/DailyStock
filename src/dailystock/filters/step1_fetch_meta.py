from __future__ import annotations

from collections.abc import Sequence
from datetime import date

import pandas as pd

from dailystock.data_sources.base import DataProvider
from dailystock.utils.validation import require_columns

META_COLUMNS = [
    "code",
    "name",
    "market",
    "exchange",
    "industry",
    "is_st",
    "listing_date",
    "total_market_cap",
]


def fetch_meta(provider: DataProvider, as_of: date, markets: Sequence[str]) -> pd.DataFrame:
    meta = provider.fetch_meta(as_of=as_of, markets=markets)
    require_columns(meta, META_COLUMNS, "meta")
    return meta.reset_index(drop=True)

