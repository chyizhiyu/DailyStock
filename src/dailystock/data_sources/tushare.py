from __future__ import annotations

from dailystock.data_sources.base import DataProviderNotConfigured


class TushareDataProvider:
    """Future Tushare adapter for financial statements and index membership."""

    def __init__(self, *_: object, **__: object) -> None:
        raise DataProviderNotConfigured(
            "TushareDataProvider is a scaffold. Configure TUSHARE_TOKEN and implement "
            "the canonical DataProvider methods before enabling it."
        )

