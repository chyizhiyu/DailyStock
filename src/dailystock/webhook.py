from __future__ import annotations

from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel, Field

from dailystock.models.market import MarketCode
from dailystock.models.screening import PipelineRequest
from dailystock.pipeline import DailyStockPipeline

app = FastAPI(title="DailyStock", version="0.1.0")


class OpenClawWebhookRequest(BaseModel):
    as_of: date = Field(default_factory=date.today)
    markets: list[MarketCode] = Field(default_factory=lambda: ["CN", "HK"])
    dry_run: bool = True


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/webhook/openclaw")
def openclaw_webhook(payload: OpenClawWebhookRequest) -> dict[str, object]:
    request = PipelineRequest(
        as_of=payload.as_of,
        markets=payload.markets,
        dry_run=payload.dry_run,
    )
    result = DailyStockPipeline().run(request)
    return result.model_dump(mode="json")
