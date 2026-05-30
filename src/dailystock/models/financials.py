from __future__ import annotations

from datetime import date

from pydantic import BaseModel


class FinancialStatement(BaseModel):
    code: str
    fiscal_year: int
    roe: float
    gross_margin: float
    net_margin: float
    debt_asset_ratio: float
    operating_cash_flow: float
    net_profit: float
    non_gaap_net_profit: float
    revenue: float


class ValuationRecord(BaseModel):
    code: str
    date: date
    market: str
    industry: str
    pe_ttm: float
    pb: float


class DividendRecord(BaseModel):
    code: str
    date: date
    industry: str
    dividend_yield: float


class FreeCashFlowRecord(BaseModel):
    code: str
    date: date
    fcf_yield: float

