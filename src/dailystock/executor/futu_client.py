from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd

from dailystock.config import FutuSettings


@dataclass(slots=True)
class FutuClient:
    settings: FutuSettings
    dry_run: bool = True

    def scan_order_book(self, candidates: pd.DataFrame) -> pd.DataFrame:
        if self.dry_run:
            return self._dry_run_scan(candidates)
        raise NotImplementedError(
            "Live Futu scanning is intentionally left behind this adapter. Connect futu-api "
            "to OpenD here after credentials, quote permissions, and safety checks are ready."
        )

    def place_order(self, order: dict[str, Any]) -> dict[str, Any]:
        if self.dry_run:
            raise RuntimeError("Dry-run mode blocks order placement.")
        if not self.settings.enable_live_trading:
            raise RuntimeError("Live trading is disabled by configuration.")
        raise NotImplementedError("Wire futu-api order placement here after live-trading approval.")

    @staticmethod
    def _dry_run_scan(candidates: pd.DataFrame) -> pd.DataFrame:
        records: list[dict[str, Any]] = []
        for index, row in candidates.reset_index(drop=True).iterrows():
            mid = max(1.0, float(row.get("total_market_cap", 10_000_000_000)) / 10_000_000_000)
            spread_bps = 10 + index * 4
            bid = round(mid * (1 - spread_bps / 20_000), 3)
            ask = round(mid * (1 + spread_bps / 20_000), 3)
            records.append(
                {
                    "code": row["code"],
                    "bid": bid,
                    "ask": ask,
                    "spread_bps": spread_bps,
                    "volume_signal": "normal",
                    "tradable": True,
                    "source": "dry_run",
                }
            )
        return pd.DataFrame.from_records(records)

