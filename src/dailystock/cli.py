from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from dailystock.config import load_settings, project_root
from dailystock.data_sources.akshare import AkShareDataProvider
from dailystock.data_sources.akshare_seed import export_akshare_seed_files
from dailystock.logging import configure_logging
from dailystock.models.screening import PipelineRequest
from dailystock.pipeline import DailyStockPipeline
from dailystock.utils.calendar import parse_date

app = typer.Typer(help="DailyStock weekly funnel screener.")


@app.callback()
def main() -> None:
    """DailyStock command group."""


@app.command()
def run(
    as_of: Annotated[
        str | None,
        typer.Option("--as-of", help="Run date in YYYY-MM-DD format."),
    ] = None,
    markets: Annotated[
        str,
        typer.Option("--markets", help="Comma-separated markets, e.g. CN,HK."),
    ] = "CN,HK",
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run/--live", help="Block or allow live order placement."),
    ] = True,
    config: Annotated[
        Path | None,
        typer.Option("--config", help="Path to YAML config."),
    ] = None,
) -> None:
    configure_logging()
    settings = load_settings(config)
    request = PipelineRequest(
        as_of=parse_date(as_of),
        markets=[market.strip().upper() for market in markets.split(",") if market.strip()],
        dry_run=dry_run,
    )
    result = DailyStockPipeline(settings=settings).run(request)
    dashboard_path = next(path for path in result.artifacts if path.endswith("dashboard.md"))
    result_path = next(path for path in result.artifacts if path.endswith("result.json"))
    typer.echo(f"DailyStock run complete: {len(result.final_candidates)} final candidates")
    typer.echo(f"Dashboard: {dashboard_path}")
    typer.echo(f"Result JSON: {result_path}")


@app.command()
def build_akshare_seed(
    as_of: Annotated[
        str | None,
        typer.Option("--as-of", help="Snapshot date in YYYY-MM-DD format."),
    ] = None,
    markets: Annotated[
        str,
        typer.Option("--markets", help="Comma-separated markets, e.g. CN,HK."),
    ] = "CN,HK",
    output_dir: Annotated[
        Path | None,
        typer.Option("--output-dir", help="Seed CSV output directory."),
    ] = None,
    config: Annotated[
        Path | None,
        typer.Option("--config", help="Path to YAML config."),
    ] = None,
    max_codes: Annotated[
        int | None,
        typer.Option("--max-codes", help="Limit stock count for smoke tests."),
    ] = None,
    max_workers: Annotated[
        int,
        typer.Option("--max-workers", help="Concurrent stock fetch workers; use 1 for stability."),
    ] = 1,
) -> None:
    configure_logging()
    settings = load_settings(config)
    snapshot_date = parse_date(as_of)
    market_list = [market.strip().upper() for market in markets.split(",") if market.strip()]
    seed_dir = _resolve_path(output_dir or settings.app.akshare_seed_dir)
    provider = AkShareDataProvider(
        cache_dir=_resolve_path(settings.app.akshare_cache_dir),
        seed_dir=seed_dir,
        max_workers=max_workers,
        use_seed=False,
    )
    result = export_akshare_seed_files(
        provider=provider,
        as_of=snapshot_date,
        markets=market_list,
        output_dir=seed_dir,
        daily_lookback_days=30,
        valuation_lookback_years=settings.valuation_filters.lookback_years,
        max_codes=max_codes,
    )

    typer.echo(f"AkShare seed CSVs exported: {result.output_dir}")
    typer.echo(f"Snapshot date: {snapshot_date.isoformat()}")
    typer.echo(f"Stocks: {len(result.codes)}")
    for filename, count in sorted(result.row_counts.items()):
        typer.echo(f"- {filename}: {count} rows")


def _resolve_path(path: str | Path) -> Path:
    value = Path(path)
    return value if value.is_absolute() else project_root() / value


if __name__ == "__main__":
    app()
