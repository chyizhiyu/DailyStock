from __future__ import annotations

import os
from pathlib import Path

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseModel):
    timezone: str = "Asia/Shanghai"
    data_source: str = "sample"
    output_dir: str = "runs"
    sample_data_dir: str = "data/samples"


class HardFilterSettings(BaseModel):
    min_listing_years: int = 3
    min_avg_turnover: dict[str, float] = Field(
        default_factory=lambda: {"CN": 30_000_000, "HK": 30_000_000}
    )
    min_total_market_cap: float = 5_000_000_000
    consecutive_loss_years: int = 2
    negative_ocf_years: int = 3


class QualityFilterSettings(BaseModel):
    min_roe: float = 0.10
    min_gross_margin: float = 0.25
    min_net_margin: float = 0.08
    max_debt_asset_ratio: float = 0.60
    min_ocf_to_net_profit: float = 0.80
    growth_years: int = 5
    min_revenue_cagr: float = 0.03
    min_net_profit_cagr: float = 0.03


class ValuationFilterSettings(BaseModel):
    lookback_years: int = 5
    min_pe_percentile: float = 0.0
    max_pe_percentile: float = 0.5
    min_pb_percentile: float = 0.0
    max_pb_percentile: float = 0.5
    min_fcf_yield: float = 0.03


class FutuSettings(BaseModel):
    host: str = "127.0.0.1"
    port: int = 11111
    trading_env: str = "SIMULATE"
    dry_run: bool = True
    enable_live_trading: bool = False
    max_spread_bps: float = 30
    max_order_notional: float = 50_000
    max_position_pct: float = 0.05


class Settings(BaseModel):
    app: AppSettings = Field(default_factory=AppSettings)
    markets: list[str] = Field(default_factory=lambda: ["CN", "HK"])
    hard_filters: HardFilterSettings = Field(default_factory=HardFilterSettings)
    quality_filters: QualityFilterSettings = Field(default_factory=QualityFilterSettings)
    valuation_filters: ValuationFilterSettings = Field(default_factory=ValuationFilterSettings)
    futu: FutuSettings = Field(default_factory=FutuSettings)


class EnvSettings(BaseSettings):
    tushare_token: str | None = None
    futu_host: str | None = None
    futu_port: int | None = None
    futu_trading_env: str | None = None
    dailystock_live_trading_enabled: bool | None = None
    dailystock_webhook_secret: str | None = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_settings(config_path: str | Path | None = None) -> Settings:
    path = Path(config_path) if config_path else project_root() / "config" / "default.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    settings = Settings.model_validate(data or {})
    env = EnvSettings()

    if env.futu_host:
        settings.futu.host = env.futu_host
    if env.futu_port:
        settings.futu.port = env.futu_port
    if env.futu_trading_env:
        settings.futu.trading_env = env.futu_trading_env
    if env.dailystock_live_trading_enabled is not None:
        settings.futu.enable_live_trading = env.dailystock_live_trading_enabled

    os.environ.setdefault("TZ", settings.app.timezone)
    return settings
