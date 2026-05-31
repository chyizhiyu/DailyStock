# AkShare Seed CSVs

This directory is intentionally tracked. Put manually prepared CSV snapshots here when GitHub
Actions cannot reach AkShare/Eastmoney reliably. `AkShareDataProvider` reads these files before
network/cache data. File names are stable and do not include dates.

Required canonical files for an offline full run:

| File | Required columns |
| --- | --- |
| `cn_constituents.csv` | `code,name,exchange,industry` |
| `a_spot.csv` | `code,name_spot,latest_price,amount,pe_ttm,pb,total_market_cap,free_float_market_cap` |
| `a_listing_info.csv` | `code,listing_date,industry_listing` |
| `sw_industry.csv` | `code,industry_sw` |
| `hk_hsci_constituents.csv` | `code,name,industry` |
| `hk_spot_full.csv` | `code,name_spot,latest_price,amount,pe_ttm,pb,total_market_cap,free_float_market_cap` |
| `hk_listing_info.csv` | `code,listing_date` |
| `daily_bars.csv` | `code,trade_date,amount` |
| `financials.csv` | `code,fiscal_year,roe,gross_margin,net_margin,debt_asset_ratio,operating_cash_flow,net_profit,non_gaap_net_profit,revenue` |
| `valuation_history.csv` | `code,date,industry,pe_ttm,pb` |
| `dividends.csv` | `code,date,industry,dividend_yield` |
| `free_cash_flow.csv` | `code,date,fcf_yield` |

Code format:

- A-share `code`: 6 digits, e.g. `600000`.
- Hong Kong `code`: 5 digits, e.g. `00700`.
- Dates: `YYYY-MM-DD`.
- Ratios: decimals preferred, e.g. `0.12` for 12%. Percent-style values such as `12` are accepted
  and normalized by the adapter for yield/ratio fields.

For GitHub Actions dry-run screening without network calls, upload these CSVs and set repository
variable or workflow environment `DAILYSTOCK_AKSHARE_OFFLINE=true`.
