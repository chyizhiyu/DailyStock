from __future__ import annotations

from fastapi.testclient import TestClient

from dailystock.models.screening import PipelineResult
from dailystock.webhook import app


def test_openclaw_webhook_invokes_pipeline(monkeypatch) -> None:
    captured = {}

    class FakePipeline:
        def run(self, request):
            captured["request"] = request
            return PipelineResult(request=request, final_candidates=[], steps=[])

    monkeypatch.setattr("dailystock.webhook.DailyStockPipeline", FakePipeline)
    client = TestClient(app)

    response = client.post(
        "/webhook/openclaw",
        json={"as_of": "2026-05-29", "markets": ["CN", "HK"], "dry_run": True},
    )

    assert response.status_code == 200
    assert response.json()["request"]["as_of"] == "2026-05-29"
    assert captured["request"].dry_run is True
