from __future__ import annotations

import logging

import pandas as pd

from dailystock.executor.futu_client import FutuClient
from dailystock.models.screening import ExecutionFrameResult

logger = logging.getLogger(__name__)


def run_futu_executor(
    candidates: pd.DataFrame,
    client: FutuClient,
    dry_run: bool,
    max_spread_bps: float,
    max_order_notional: float,
    max_position_pct: float,
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
    plan = apply_risk_controls(plan, max_order_notional, max_position_pct)

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


def apply_risk_controls(
    plan: pd.DataFrame,
    max_order_notional: float,
    max_position_pct: float,
) -> pd.DataFrame:
    guarded = plan.copy()
    guarded["planned_notional"] = _planned_notional(guarded)
    guarded["planned_position_pct"] = _planned_position_pct(guarded)
    guarded["risk_status"] = "OK"
    guarded["risk_reason"] = ""

    notional_blocked = guarded["planned_notional"] > max_order_notional
    position_blocked = guarded["planned_position_pct"] > max_position_pct

    if notional_blocked.any():
        guarded.loc[notional_blocked, "risk_status"] = "BLOCKED"
        guarded.loc[notional_blocked, "risk_reason"] = "max_order_notional_exceeded"
    if position_blocked.any():
        blocked_idx = guarded.index[position_blocked]
        already_blocked = guarded.loc[blocked_idx, "risk_reason"].astype(str).str.len() > 0
        append_idx = already_blocked[already_blocked].index
        replace_idx = already_blocked[~already_blocked].index
        guarded.loc[append_idx, "risk_reason"] += ";max_position_pct_exceeded"
        guarded.loc[replace_idx, "risk_reason"] = "max_position_pct_exceeded"
        guarded.loc[position_blocked, "risk_status"] = "BLOCKED"

    blocked = guarded["risk_status"].eq("BLOCKED")
    if blocked.any():
        logger.warning(
            "[Step 5 Risk Guard] Blocked %s order plans. Reasons: %s",
            int(blocked.sum()),
            guarded.loc[blocked, "risk_reason"].value_counts().to_dict(),
        )
        guarded.loc[blocked, "action"] = "BLOCKED"
        guarded.loc[blocked, "decision_reason"] = guarded.loc[blocked, "risk_reason"]

    return guarded


def _planned_notional(plan: pd.DataFrame) -> pd.Series:
    for column in ["planned_notional", "target_notional", "order_notional"]:
        if column in plan:
            return pd.to_numeric(plan[column], errors="coerce").fillna(0)
    if {"quantity", "ask"}.issubset(plan.columns):
        quantity = pd.to_numeric(plan["quantity"], errors="coerce").fillna(0)
        ask = pd.to_numeric(plan["ask"], errors="coerce").fillna(0)
        return quantity * ask
    return pd.Series(0.0, index=plan.index)


def _planned_position_pct(plan: pd.DataFrame) -> pd.Series:
    if "planned_position_pct" in plan:
        return pd.to_numeric(plan["planned_position_pct"], errors="coerce").fillna(0)
    if {"planned_notional", "account_equity"}.issubset(plan.columns):
        equity = pd.to_numeric(plan["account_equity"], errors="coerce").replace(0, pd.NA)
        return (pd.to_numeric(plan["planned_notional"], errors="coerce") / equity).fillna(0)
    return pd.Series(0.0, index=plan.index)


def _orders_from_plan(plan: pd.DataFrame) -> list[dict[str, object]]:
    orders: list[dict[str, object]] = []
    executable = plan.loc[plan["action"].eq("BUY") & plan["risk_status"].eq("OK")]
    for _, row in executable.iterrows():
        orders.append(
            {
                "code": row["code"],
                "side": "BUY",
                "order_type": "MARKET",
                "quantity": int(row.get("quantity", 0)),
                "planned_notional": float(row.get("planned_notional", 0)),
                "reason": row["decision_reason"],
            }
        )
    return orders
