from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any

import pandas as pd
from pydantic import BaseModel, Field

from dailystock.models.market import MarketCode


class PipelineRequest(BaseModel):
    as_of: date = Field(default_factory=date.today)
    markets: list[MarketCode] = Field(default_factory=lambda: ["CN", "HK"])
    dry_run: bool = True


class StepSummary(BaseModel):
    name: str
    input_count: int
    output_count: int
    elapsed_seconds: float
    rejection_counts: dict[str, int] = Field(default_factory=dict)
    output_market_counts: dict[str, int] = Field(default_factory=dict)
    rejected_market_counts: dict[str, int] = Field(default_factory=dict)
    rejection_market_counts: dict[str, dict[str, int]] = Field(default_factory=dict)
    artifacts: list[str] = Field(default_factory=list)


class PipelineResult(BaseModel):
    request: PipelineRequest
    final_candidates: list[dict[str, Any]]
    steps: list[StepSummary]
    execution_plan: list[dict[str, Any]] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)


@dataclass(slots=True)
class FilterFrameResult:
    candidates: pd.DataFrame
    rejected: pd.DataFrame = field(default_factory=pd.DataFrame)
    rejection_counts: dict[str, int] = field(default_factory=dict)


@dataclass(slots=True)
class ExecutionFrameResult:
    scanned: pd.DataFrame
    execution_plan: pd.DataFrame
    orders: list[dict[str, Any]] = field(default_factory=list)
