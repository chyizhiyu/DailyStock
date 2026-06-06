#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

import requests

MAX_TEXT_CHARS = int(os.environ.get("DAILYSTOCK_FEISHU_MAX_TEXT_CHARS", "5000"))
FEISHU_BASE_URL = os.environ.get("DAILYSTOCK_FEISHU_BASE_URL", "https://open.feishu.cn")


def _truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def _summary_text(summary_path: Path) -> str:
    if not summary_path.exists():
        raise FileNotFoundError(f"Missing Feishu summary: {summary_path}")
    return summary_path.read_text(encoding="utf-8")[:MAX_TEXT_CHARS]


def _check_feishu_response(data: dict[str, Any], context: str) -> None:
    code = data.get("code", 0)
    if code not in (0, None):
        message = data.get("msg") or data.get("message") or "unknown Feishu error"
        raise RuntimeError(f"{context} failed: code={code}, message={message}")


def _json_response(response: requests.Response, context: str) -> dict[str, Any]:
    response.raise_for_status()
    try:
        data = response.json()
    except ValueError:
        data = {}
    if isinstance(data, dict):
        _check_feishu_response(data, context)
        return data
    raise RuntimeError(f"{context} returned non-object JSON")


def _webhook_payload(text: str) -> dict[str, Any]:
    return {"msg_type": "text", "content": {"text": text}}


def _app_message_payload(text: str, receive_id: str) -> dict[str, Any]:
    return {
        "receive_id": receive_id,
        "msg_type": "text",
        "content": json.dumps({"text": text}, ensure_ascii=False),
    }


def _post_webhook(webhook_url: str, text: str, dry_run: bool) -> dict[str, Any]:
    payload = _webhook_payload(text)
    if dry_run:
        return {"mode": "webhook", "dry_run": True, "payload": payload}

    response = requests.post(
        webhook_url,
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=20,
    )
    data = _json_response(response, "Feishu webhook notification")
    return {"mode": "webhook", "dry_run": False, "response": data}


def _tenant_access_token(app_id: str, app_secret: str) -> str:
    response = requests.post(
        f"{FEISHU_BASE_URL}/open-apis/auth/v3/tenant_access_token/internal",
        headers={"Content-Type": "application/json"},
        json={"app_id": app_id, "app_secret": app_secret},
        timeout=20,
    )
    data = _json_response(response, "Feishu tenant token request")
    token = data.get("tenant_access_token")
    if not token:
        raise RuntimeError("Feishu tenant token request returned no tenant_access_token")
    return str(token)


def _post_app_message(
    *,
    app_id: str,
    app_secret: str,
    receive_id: str,
    receive_id_type: str,
    text: str,
    dry_run: bool,
) -> dict[str, Any]:
    payload = _app_message_payload(text, receive_id)
    if dry_run:
        return {
            "mode": "app_api",
            "dry_run": True,
            "receive_id_type": receive_id_type,
            "payload": payload,
        }

    token = _tenant_access_token(app_id, app_secret)
    response = requests.post(
        f"{FEISHU_BASE_URL}/open-apis/im/v1/messages",
        params={"receive_id_type": receive_id_type},
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=20,
    )
    data = _json_response(response, "Feishu app notification")
    return {
        "mode": "app_api",
        "dry_run": False,
        "receive_id_type": receive_id_type,
        "message_id": data.get("data", {}).get("message_id"),
    }


def send_feishu_summary(summary_path: Path, *, dry_run: bool | None = None) -> dict[str, Any]:
    text = _summary_text(summary_path)
    if dry_run is None:
        dry_run = _truthy(os.environ.get("DAILYSTOCK_FEISHU_DRY_RUN"))

    webhook_url = os.environ.get("FEISHU_WEBHOOK_URL") or os.environ.get(
        "DAILYSTOCK_FEISHU_WEBHOOK_URL"
    )
    app_id = os.environ.get("FEISHU_APP_ID") or os.environ.get("DAILYSTOCK_FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET") or os.environ.get(
        "DAILYSTOCK_FEISHU_APP_SECRET"
    )
    receive_id = os.environ.get("FEISHU_RECEIVE_ID") or os.environ.get(
        "DAILYSTOCK_FEISHU_RECEIVE_ID"
    )
    receive_id_type = (
        os.environ.get("FEISHU_RECEIVE_ID_TYPE")
        or os.environ.get("DAILYSTOCK_FEISHU_RECEIVE_ID_TYPE")
        or "open_id"
    )

    if webhook_url:
        return _post_webhook(webhook_url, text, dry_run)

    if app_id and app_secret and receive_id:
        return _post_app_message(
            app_id=app_id,
            app_secret=app_secret,
            receive_id=receive_id,
            receive_id_type=receive_id_type,
            text=text,
            dry_run=dry_run,
        )

    return {
        "mode": "skipped",
        "reason": (
            "No Feishu webhook or app credentials configured. Set "
            "DAILYSTOCK_FEISHU_WEBHOOK_URL, or set DAILYSTOCK_FEISHU_APP_ID, "
            "DAILYSTOCK_FEISHU_APP_SECRET and DAILYSTOCK_FEISHU_RECEIVE_ID."
        ),
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: scripts/send_feishu_summary.py <feishu_summary.md>", file=sys.stderr)
        return 2

    result = send_feishu_summary(Path(argv[1]))
    mode = result.get("mode")
    if mode == "skipped":
        print(result["reason"])
    elif result.get("dry_run"):
        print(f"Feishu notification dry-run prepared via {mode}.")
    else:
        print(f"Feishu notification sent via {mode}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
