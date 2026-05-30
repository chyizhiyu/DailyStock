from __future__ import annotations

from dailystock.data_sources.base import DataProviderNotConfigured


class AkShareDataProvider:
    """Future AkShare adapter.

    Keep this boundary thin: normalize AkShare outputs into the canonical columns
    used by the local filters, then let the shared pipeline do the screening.
    """

    def __init__(self, *_: object, **__: object) -> None:
        raise DataProviderNotConfigured(
            "AkShareDataProvider is a scaffold. Install the data extra and implement "
            "vendor-specific field mapping before using it in production."
        )

