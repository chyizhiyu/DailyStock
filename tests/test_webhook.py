from __future__ import annotations

from fastapi.testclient import TestClient

from dailystock.models.screening import PipelineResult
from dailystock.webhook import app


def test_openclaw_webhook_invokes_pipeline_with_valid_token(monkeypatch) -> None:
    captured = {}
    monkeypatch.setenv("DAILYSTOCK_WEBHOOK_SECRET", "top-secret")

    class FakePipeline:
        def run(self, request):
            captured["request"] = request
            return PipelineResult(request=request, final_candidates=[], steps=[])

    monkeypatch.setattr("dailystock.webhook.DailyStockPipeline", FakePipeline)
    client = TestClient(app)

    response = client.post(
        "/webhook/openclaw",
        headers={"X-OpenClaw-Token": "top-secret"},
        json={"as_of": "2026-05-29", "markets": ["CN", "HK"], "dry_run": True},
    )

    assert response.status_code == 200
    assert response.json()["request"]["as_of"] == "2026-05-29"
    assert captured["request"].dry_run is True


def test_openclaw_webhook_rejects_missing_or_invalid_token(monkeypatch) -> None:
    monkeypatch.setenv("DAILYSTOCK_WEBHOOK_SECRET", "top-secret")
    client = TestClient(app)

    missing = client.post(
        "/webhook/openclaw",
        json={"as_of": "2026-05-29", "markets": ["CN", "HK"], "dry_run": True},
    )
    invalid = client.post(
        "/webhook/openclaw",
        headers={"X-OpenClaw-Token": "wrong"},
        json={"as_of": "2026-05-29", "markets": ["CN", "HK"], "dry_run": True},
    )

    assert missing.status_code == 403
    assert invalid.status_code == 403


def test_openclaw_webhook_rejects_unconfigured_secret(monkeypatch) -> None:
    monkeypatch.delenv("DAILYSTOCK_WEBHOOK_SECRET", raising=False)
    client = TestClient(app)

    response = client.post(
        "/webhook/openclaw",
        headers={"X-OpenClaw-Token": "top-secret"},
        json={"as_of": "2026-05-29", "markets": ["CN", "HK"], "dry_run": True},
    )

    assert response.status_code == 403
