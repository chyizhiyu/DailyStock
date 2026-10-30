# DailyStock Funnel Dashboard

- As of: `2026-10-30`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7934 | - | 280.438 |
| step2_hard_filters | 7934 | 194 | risk_screen: 1505, listing_age: 503, liquidity: 1004, market_cap: 4713, performance_floor: 15 | 0.073 |
| step3_financial_quality | 194 | 24 | profitability: 151, leverage: 5, cash_flow_quality: 4, growth: 10 | 0.015 |
| step4_valuation | 24 | 0 | missing_valuation_data: 2, pe_valuation_percentile: 20, pb_valuation_percentile: 2 | 0.023 |
| step5_futu_executor | 0 | 0 | - | 0.000 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5121 | 0 | 2813 | 0 |
| step2_hard_filters | 0 | 5121 | 194 | 2619 |
| step3_financial_quality | 0 | 0 | 24 | 170 |
| step4_valuation | 0 | 0 | 0 | 24 |
| step5_futu_executor | 0 | 0 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 2 | 1503 |
| step2_hard_filters | listing_age | 204 | 299 |
| step2_hard_filters | liquidity | 401 | 603 |
| step2_hard_filters | market_cap | 4514 | 199 |
| step2_hard_filters | performance_floor | 0 | 15 |
| step3_financial_quality | profitability | 0 | 151 |
| step3_financial_quality | leverage | 0 | 5 |
| step3_financial_quality | cash_flow_quality | 0 | 4 |
| step3_financial_quality | growth | 0 | 10 |
| step4_valuation | missing_valuation_data | 0 | 2 |
| step4_valuation | pe_valuation_percentile | 0 | 20 |
| step4_valuation | pb_valuation_percentile | 0 | 2 |

## Final Candidates

_No candidates survived the valuation funnel._

## Execution Plan

_No execution plan was produced._
