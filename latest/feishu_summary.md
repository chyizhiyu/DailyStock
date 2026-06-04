# DailyStock GitHub Actions Result

- Tag: `-`
- Run: [#25](https://github.com/chyizhiyu/DailyStock/actions/runs/26936397071)
- Source commit: `6b78bb02ede5`
- Run attempt: `1`

# DailyStock Weekly Screen

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7835 | - | 281.611 |
| step2_hard_filters | 7835 | 2794 | risk_screen: 1452, listing_age: 525, liquidity: 1034, market_cap: 1572, performance_floor: 458 | 0.623 |
| step3_financial_quality | 2794 | 286 | profitability: 2296, leverage: 42, cash_flow_quality: 106, growth: 64 | 0.064 |
| step4_valuation | 286 | 52 | missing_valuation_data: 29, pe_valuation_percentile: 126, pb_valuation_percentile: 67, dividend_yield: 12 | 0.278 |
| step5_futu_executor | 52 | 52 | spread_too_wide: 46 | 0.007 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 2774 | 0 |
| step2_hard_filters | 2580 | 2481 | 214 | 2560 |
| step3_financial_quality | 256 | 2324 | 30 | 184 |
| step4_valuation | 52 | 204 | 0 | 30 |
| step5_futu_executor | 52 | 46 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1451 |
| step2_hard_filters | listing_age | 237 | 288 |
| step2_hard_filters | liquidity | 432 | 602 |
| step2_hard_filters | market_cap | 1371 | 201 |
| step2_hard_filters | performance_floor | 440 | 18 |
| step3_financial_quality | profitability | 2136 | 160 |
| step3_financial_quality | leverage | 34 | 8 |
| step3_financial_quality | cash_flow_quality | 99 | 7 |
| step3_financial_quality | growth | 55 | 9 |
| step4_valuation | missing_valuation_data | 26 | 3 |
| step4_valuation | pe_valuation_percentile | 101 | 25 |
| step4_valuation | pb_valuation_percentile | 65 | 2 |
| step4_valuation | dividend_yield | 12 | 0 |
| step5_futu_executor | spread_too_wide | 46 | 0 |

## Step 5 Decisions

- Actions: `SKIP: 46, WATCH: 6`
- Reasons: `spread_too_wide: 46, passed_depth_scan: 6`

## WATCH / BUY Candidates

| code | name | market | industry | action | decision_reason | pe_ttm | pb | roe | dividend_yield | fcf_yield | spread_bps | risk_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000513 | 丽珠集团 | CN | C 制造业 | WATCH | passed_depth_scan | 13.37 | 1.857 | 0.1467 | 0.04712 | 0.1167 | 10 | OK |
| 000538 | 云南白药 | CN | C 制造业 | WATCH | passed_depth_scan | 16.82 | 2.06 | 0.1302 | 0.02898 | 0.05304 | 14 | OK |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | WATCH | passed_depth_scan | 10.29 | 1.02 | 0.106 | 0.03399 | 0.1792 | 18 | OK |
| 000739 | 普洛药业 | CN | C 制造业 | WATCH | passed_depth_scan | 20.78 | 2.834 | 0.1322 | 0.01265 | 0.06563 | 22 | OK |
| 000786 | 北新建材 | CN | C 制造业 | WATCH | passed_depth_scan | 12.87 | 1.347 | 0.1111 | 0.031 | 0.1117 | 26 | OK |
| 000848 | 承德露露 | CN | C 制造业 | WATCH | passed_depth_scan | 13.18 | 2.174 | 0.1778 | 0.05821 | 0.1255 | 30 | OK |

## Blocked / Skipped

| code | name | market | action | decision_reason | spread_bps |
| --- | --- | --- | --- | --- | --- |
| 000915 | 华特达因 | CN | SKIP | spread_too_wide | 34 |
| 000975 | 山金国际 | CN | SKIP | spread_too_wide | 38 |
| 000999 | 华润三九 | CN | SKIP | spread_too_wide | 42 |
| 001286 | 陕西能源 | CN | SKIP | spread_too_wide | 46 |
| 002001 | 新和成 | CN | SKIP | spread_too_wide | 50 |
| 002003 | 伟星股份 | CN | SKIP | spread_too_wide | 54 |
| 002128 | 电投能源 | CN | SKIP | spread_too_wide | 58 |
| 002170 | 芭田股份 | CN | SKIP | spread_too_wide | 62 |
| 002223 | 鱼跃医疗 | CN | SKIP | spread_too_wide | 66 |
| 002236 | 大华股份 | CN | SKIP | spread_too_wide | 70 |
| 002262 | 恩华药业 | CN | SKIP | spread_too_wide | 74 |
| 002444 | 巨星科技 | CN | SKIP | spread_too_wide | 78 |
| 002555 | 三七互娱 | CN | SKIP | spread_too_wide | 82 |
| 002603 | 以岭药业 | CN | SKIP | spread_too_wide | 86 |
| 002605 | 姚记科技 | CN | SKIP | spread_too_wide | 90 |
| 002734 | 利民股份 | CN | SKIP | spread_too_wide | 94 |
| 002773 | 康弘药业 | CN | SKIP | spread_too_wide | 98 |
| 002831 | 裕同科技 | CN | SKIP | spread_too_wide | 102 |
| 002833 | 弘亚数控 | CN | SKIP | spread_too_wide | 106 |
| 300009 | 安科生物 | CN | SKIP | spread_too_wide | 110 |
