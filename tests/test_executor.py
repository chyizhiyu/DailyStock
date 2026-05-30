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
    )

    assert result.orders == []
    assert result.execution_plan.iloc[0]["action"] == "WATCH"

