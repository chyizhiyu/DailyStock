# DailyStock Funnel Dashboard

- As of: `2026-11-06`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7925 | - | 258.760 |
| step2_hard_filters | 7925 | 191 | risk_screen: 1488, listing_age: 498, liquidity: 1237, market_cap: 4494, performance_floor: 17 | 0.062 |
| step3_financial_quality | 191 | 24 | profitability: 148, leverage: 6, cash_flow_quality: 4, growth: 9 | 0.014 |
| step4_valuation | 24 | 0 | missing_valuation_data: 2, pe_valuation_percentile: 19, pb_valuation_percentile: 3 | 0.018 |
| step5_futu_executor | 0 | 0 | - | 0.000 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5117 | 0 | 2808 | 0 |
| step2_hard_filters | 0 | 5117 | 191 | 2617 |
| step3_financial_quality | 0 | 0 | 24 | 167 |
| step4_valuation | 0 | 0 | 0 | 24 |
| step5_futu_executor | 0 | 0 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 0 | 1488 |
| step2_hard_filters | listing_age | 199 | 299 |
| step2_hard_filters | liquidity | 624 | 613 |
| step2_hard_filters | market_cap | 4294 | 200 |
| step2_hard_filters | performance_floor | 0 | 17 |
| step3_financial_quality | profitability | 0 | 148 |
| step3_financial_quality | leverage | 0 | 6 |
| step3_financial_quality | cash_flow_quality | 0 | 4 |
| step3_financial_quality | growth | 0 | 9 |
| step4_valuation | missing_valuation_data | 0 | 2 |
| step4_valuation | pe_valuation_percentile | 0 | 19 |
| step4_valuation | pb_valuation_percentile | 0 | 3 |

## Final Candidates

_No candidates survived the valuation funnel._

## Execution Plan

_No execution plan was produced._
