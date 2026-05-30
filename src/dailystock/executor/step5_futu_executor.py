from __future__ import annotations

import pandas as pd

from dailystock.executor.futu_client import FutuClient
from dailystock.models.screening import ExecutionFrameResult


def run_futu_executor(
    candidates: pd.DataFrame,
    client: FutuClient,
    dry_run: bool,
    max_spread_bps: float,
) -> ExecutionFrameResult:
    scanned = client.scan_order_book(candidates)
    if candidates.empty:
        return ExecutionFrameResult(scanned=scanned, execution_plan=pd.DataFrame(), orders=[])

    plan = candidates.merge(scanned, on="code", how="left")
    decisions = [
        _decision(
            tradable=bool(row.get("tradable", False)),
            spread_bps=float(row.get("spread_bps", float("inf"))),
            volume_signal=str(row.get("volume_signal", "")),
            max_spread_bps=max_spread_bps,
        )
        for _, row in plan.iterrows()
    ]
    plan["action"] = [decision[0] for decision in decisions]
    plan["decision_reason"] = [decision[1] for decision in decisions]
    plan["dry_run"] = dry_run

    orders: list[dict[str, object]] = []
    if not dry_run and client.settings.enable_live_trading:
        for order in _orders_from_plan(plan):
            orders.append(client.place_order(order))

    return ExecutionFrameResult(scanned=scanned, execution_plan=plan, orders=orders)


def _decision(
    tradable: bool,
    spread_bps: float,
    volume_signal: str,
    max_spread_bps: float,
) -> tuple[str, str]:
    if not tradable:
        return "SKIP", "not_tradable"
    if spread_bps > max_spread_bps:
        return "SKIP", "spread_too_wide"
    if volume_signal == "accumulation":
        return "BUY", "volume_accumulation"
    return "WATCH", "passed_depth_scan"


def _orders_from_plan(plan: pd.DataFrame) -> list[dict[str, object]]:
    orders: list[dict[str, object]] = []
    for _, row in plan.loc[plan["action"].eq("BUY")].iterrows():
        orders.append(
            {
                "code": row["code"],
                "side": "BUY",
                "order_type": "MARKET",
                "quantity": 0,
                "reason": row["decision_reason"],
            }
        )
    return orders

