from __future__ import annotations

from dailystock.data_sources.base import DataProviderNotConfigured


class LocalDbDataProvider:
    """Future DuckDB/SQLite adapter for locally cached market and financial data."""

    def __init__(self, *_: object, **__: object) -> None:
        raise DataProviderNotConfigured(
            "LocalDbDataProvider is a scaffold. Point it at a local warehouse and "
            "normalize query results to the canonical DataProvider schema."
        )
