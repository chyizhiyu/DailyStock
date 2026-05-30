from __future__ import annotations

from datetime import date, datetime


def parse_date(value: str | date | None) -> date:
    if value is None:
        return date.today()
    if isinstance(value, date):
        return value
    return datetime.strptime(value, "%Y-%m-%d").date()


def is_friday(value: date) -> bool:
    return value.weekday() == 4
