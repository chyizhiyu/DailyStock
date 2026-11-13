# DailyStock Funnel Dashboard

- As of: `2026-11-13`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7929 | - | 342.551 |
| step2_hard_filters | 7929 | 188 | risk_screen: 1498, listing_age: 496, liquidity: 1391, market_cap: 4343, performance_floor: 13 | 0.111 |
| step3_financial_quality | 188 | 22 | profitability: 148, leverage: 6, cash_flow_quality: 4, growth: 8 | 0.023 |
| step4_valuation | 22 | 0 | missing_valuation_data: 2, pe_valuation_percentile: 17, pb_valuation_percentile: 3 | 0.034 |
| step5_futu_executor | 0 | 0 | - | 0.001 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5117 | 0 | 2812 | 0 |
| step2_hard_filters | 0 | 5117 | 188 | 2624 |
| step3_financial_quality | 0 | 0 | 22 | 166 |
| step4_valuation | 0 | 0 | 0 | 22 |
| step5_futu_executor | 0 | 0 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 0 | 1498 |
| step2_hard_filters | listing_age | 194 | 302 |
| step2_hard_filters | liquidity | 770 | 621 |
| step2_hard_filters | market_cap | 4153 | 190 |
| step2_hard_filters | performance_floor | 0 | 13 |
| step3_financial_quality | profitability | 0 | 148 |
| step3_financial_quality | leverage | 0 | 6 |
| step3_financial_quality | cash_flow_quality | 0 | 4 |
| step3_financial_quality | growth | 0 | 8 |
| step4_valuation | missing_valuation_data | 0 | 2 |
| step4_valuation | pe_valuation_percentile | 0 | 17 |
| step4_valuation | pb_valuation_percentile | 0 | 3 |

## Final Candidates

_No candidates survived the valuation funnel._

## Execution Plan

_No execution plan was produced._
