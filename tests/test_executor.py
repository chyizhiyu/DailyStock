from __future__ import annotations

import pandas as pd

from dailystock.config import FutuSettings
from dailystock.executor.futu_client import FutuClient
from dailystock.executor.step5_futu_executor import run_futu_executor


class ExplodingOrderClient(FutuClient):
    def place_order(self, order):  # pragma: no cover - this must never run
        raise AssertionError(f"place_order was called in dry-run mode: {order}")


def test_dry_run_executor_never_places_orders() -> None:
    candidates = pd.DataFrame(
        [
            {
                "code": "CN000001",
                "name": "Huaguang Consumer",
                "market": "CN",
                "total_market_cap": 20_000_000_000,
            }
        ]
    )
    client = ExplodingOrderClient(settings=FutuSettings(), dry_run=True)

    result = run_futu_executor(
        candidates,
        client=client,
        dry_run=True,
        max_spread_bps=30,
        max_order_notional=50_000,
        max_position_pct=0.05,
    )

    assert result.orders == []
    assert result.execution_plan.iloc[0]["action"] == "WATCH"


def test_executor_marks_notional_risk_even_in_dry_run() -> None:
    candidates = pd.DataFrame(
        [
            {
                "code": "CN000001",
                "name": "Huaguang Consumer",
                "market": "CN",
                "total_market_cap": 20_000_000_000,
                "target_notional": 60_000,
            }
        ]
    )
    client = ExplodingOrderClient(settings=FutuSettings(), dry_run=True)

    result = run_futu_executor(
        candidates,
        client=client,
        dry_run=True,
        max_spread_bps=30,
        max_order_notional=50_000,
        max_position_pct=0.05,
    )

    plan = result.execution_plan.iloc[0]
    assert result.orders == []
    assert plan["action"] == "BLOCKED"
    assert plan["risk_status"] == "BLOCKED"
    assert plan["risk_reason"] == "max_order_notional_exceeded"
    assert plan["planned_notional"] == 60_000
