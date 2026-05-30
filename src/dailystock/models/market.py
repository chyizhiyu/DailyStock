from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel

MarketCode = Literal["CN", "HK"]


class StockMeta(BaseModel):
    code: str
    name: str
    market: MarketCode
    exchange: str
    industry: str
    is_st: bool = False
    listing_date: date
    total_market_cap: float
    free_float_market_cap: float | None = None
    is_suspended: bool = False
    is_penny_stock: bool = False
    is_biotech_w: bool = False
    is_profitable_biotech: bool = True


class DailyBar(BaseModel):
    code: str
    trade_date: date
    amount: float

