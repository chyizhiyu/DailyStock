# DailyStock Funnel Dashboard

- As of: `2026-11-20`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7927 | - | 200.033 |
| step2_hard_filters | 7927 | 221 | risk_screen: 1516, listing_age: 486, liquidity: 5497, market_cap: 189, performance_floor: 18 | 0.100 |
| step3_financial_quality | 221 | 26 | profitability: 176, leverage: 5, cash_flow_quality: 3, growth: 11 | 0.024 |
| step4_valuation | 26 | 0 | pe_valuation_percentile: 26 | 0.034 |
| step5_futu_executor | 0 | 0 | - | 0.001 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5117 | 0 | 2810 | 0 |
| step2_hard_filters | 0 | 5117 | 221 | 2589 |
| step3_financial_quality | 0 | 0 | 26 | 195 |
| step4_valuation | 0 | 0 | 0 | 26 |
| step5_futu_executor | 0 | 0 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 0 | 1516 |
| step2_hard_filters | listing_age | 190 | 296 |
| step2_hard_filters | liquidity | 4927 | 570 |
| step2_hard_filters | market_cap | 0 | 189 |
| step2_hard_filters | performance_floor | 0 | 18 |
| step3_financial_quality | profitability | 0 | 176 |
| step3_financial_quality | leverage | 0 | 5 |
| step3_financial_quality | cash_flow_quality | 0 | 3 |
| step3_financial_quality | growth | 0 | 11 |
| step4_valuation | pe_valuation_percentile | 0 | 26 |

## Final Candidates

_No candidates survived the valuation funnel._

## Execution Plan

_No execution plan was produced._
