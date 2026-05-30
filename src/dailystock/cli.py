from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from dailystock.config import load_settings
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


if __name__ == "__main__":
    app()
