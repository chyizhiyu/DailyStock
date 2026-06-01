# DailyStock Weekly Screen

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6288 | - | 225.826 |
| step2_hard_filters | 6288 | 0 | risk_screen: 642, listing_age: 388, liquidity: 5258 | 0.041 |
| step3_financial_quality | 0 | 0 | - | 0.013 |
| step4_valuation | 0 | 0 | - | 0.009 |
| step5_futu_executor | 0 | 0 | - | 0.001 |

## Step 5 Decisions

_No execution plan was produced._

## WATCH / BUY Candidates

_No candidates survived the funnel._
