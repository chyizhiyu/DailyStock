from __future__ import annotations

import hmac
import os
from datetime import date
from typing import Annotated

from fastapi import FastAPI, Header, HTTPException, status
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
def openclaw_webhook(
    payload: OpenClawWebhookRequest,
    x_openclaw_token: Annotated[
        str | None,
        Header(alias="X-OpenClaw-Token"),
    ] = None,
) -> dict[str, object]:
    _verify_openclaw_token(x_openclaw_token)
    request = PipelineRequest(
        as_of=payload.as_of,
        markets=payload.markets,
        dry_run=payload.dry_run,
    )
    result = DailyStockPipeline().run(request)
    return result.model_dump(mode="json")


def _verify_openclaw_token(provided_token: str | None) -> None:
    expected_token = os.getenv("DAILYSTOCK_WEBHOOK_SECRET", "").strip()
    if not expected_token or not provided_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Missing or invalid OpenClaw token.",
        )
    if not hmac.compare_digest(provided_token, expected_token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Missing or invalid OpenClaw token.",
        )
