from __future__ import annotations

import os
from datetime import date, datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

DEFAULT_TIMEZONE = "Asia/Shanghai"


def parse_date(value: str | date | None) -> date:
    if value is None:
        return datetime.now(_configured_timezone()).date()
    if isinstance(value, date):
        return value
    return datetime.strptime(value, "%Y-%m-%d").date()


def is_friday(value: date) -> bool:
    return value.weekday() == 4


def _configured_timezone() -> ZoneInfo:
    timezone_name = (
        os.environ.get("DAILYSTOCK_TIMEZONE")
        or os.environ.get("TZ")
        or DEFAULT_TIMEZONE
    )
    try:
        return ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError:
        return ZoneInfo(DEFAULT_TIMEZONE)
