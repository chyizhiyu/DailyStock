from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "send_feishu_summary.py"
SPEC = importlib.util.spec_from_file_location("send_feishu_summary", SCRIPT_PATH)
assert SPEC and SPEC.loader
feishu_sender = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(feishu_sender)


def _summary(tmp_path: Path) -> Path:
    path = tmp_path / "feishu_summary.md"
    path.write_text("# DailyStock\n\nOK", encoding="utf-8")
    return path


def _clear_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in [
        "FEISHU_WEBHOOK_URL",
        "DAILYSTOCK_FEISHU_WEBHOOK_URL",
        "FEISHU_APP_ID",
        "DAILYSTOCK_FEISHU_APP_ID",
        "FEISHU_APP_SECRET",
        "DAILYSTOCK_FEISHU_APP_SECRET",
        "FEISHU_RECEIVE_ID",
        "DAILYSTOCK_FEISHU_RECEIVE_ID",
        "FEISHU_RECEIVE_ID_TYPE",
        "DAILYSTOCK_FEISHU_RECEIVE_ID_TYPE",
    ]:
        monkeypatch.delenv(name, raising=False)


def test_feishu_sender_skips_when_unconfigured(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _clear_env(monkeypatch)

    result = feishu_sender.send_feishu_summary(_summary(tmp_path), dry_run=True)

    assert result["mode"] == "skipped"
    assert "No Feishu webhook or app credentials" in result["reason"]


def test_feishu_sender_prepares_app_api_payload_in_dry_run(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _clear_env(monkeypatch)
    monkeypatch.setenv("DAILYSTOCK_FEISHU_APP_ID", "cli_test")
    monkeypatch.setenv("DAILYSTOCK_FEISHU_APP_SECRET", "secret")
    monkeypatch.setenv("DAILYSTOCK_FEISHU_RECEIVE_ID", "ou_test")

    result = feishu_sender.send_feishu_summary(_summary(tmp_path), dry_run=True)

    assert result["mode"] == "app_api"
    assert result["receive_id_type"] == "open_id"
    assert result["payload"]["receive_id"] == "ou_test"
    assert result["payload"]["msg_type"] == "text"
    assert "DailyStock" in result["payload"]["content"]


def test_feishu_sender_raises_on_webhook_business_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _clear_env(monkeypatch)
    monkeypatch.setenv("DAILYSTOCK_FEISHU_WEBHOOK_URL", "https://example.invalid/webhook")

    class FakeResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict[str, object]:
            return {"code": 999, "msg": "bad token"}

    def fake_post(*args, **kwargs):  # noqa: ANN002, ANN003
        return FakeResponse()

    monkeypatch.setattr(feishu_sender.requests, "post", fake_post)

    with pytest.raises(RuntimeError, match="bad token"):
        feishu_sender.send_feishu_summary(_summary(tmp_path), dry_run=False)
