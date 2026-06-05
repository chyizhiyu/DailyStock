# DailyStock GitHub Actions Result

- Tag: `dailystock-20260605-163514`
- Run: [#28](https://github.com/chyizhiyu/DailyStock/actions/runs/27004620985)
- Source commit: `f2ee2a764ab7`
- Run attempt: `1`

# DailyStock Weekly Screen

- As of: `2026-06-05`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6287 | - | 241.787 |
| step2_hard_filters | 6287 | 0 | risk_screen: 640, listing_age: 381, liquidity: 5266 | 0.037 |
| step3_financial_quality | 0 | 0 | - | 0.011 |
| step4_valuation | 0 | 0 | - | 0.008 |
| step5_futu_executor | 0 | 0 | - | 0.001 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 1226 | 0 |
| step2_hard_filters | 0 | 5061 | 0 | 1226 |
| step3_financial_quality | 0 | 0 | 0 | 0 |
| step4_valuation | 0 | 0 | 0 | 0 |
| step5_futu_executor | 0 | 0 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 639 |
| step2_hard_filters | listing_age | 275 | 106 |
| step2_hard_filters | liquidity | 4785 | 481 |

## Step 5 Decisions

_No execution plan was produced._

## WATCH / BUY Candidates

_No candidates survived the funnel._
