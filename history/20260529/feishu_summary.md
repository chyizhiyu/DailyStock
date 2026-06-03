# DailyStock GitHub Actions Result

- Tag: `dailystock-20260603-144643`
- Run: [#23](https://github.com/chyizhiyu/DailyStock/actions/runs/26868451966)
- Source commit: `4231f7a65247`
- Run attempt: `1`

# DailyStock Weekly Screen

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7835 | - | 292.337 |
| step2_hard_filters | 7835 | 2852 | risk_screen: 1452, listing_age: 478, liquidity: 1025, market_cap: 1565, performance_floor: 463 | 0.383 |
| step3_financial_quality | 2852 | 273 | profitability: 2345, leverage: 44, cash_flow_quality: 108, growth: 82 | 0.035 |
| step4_valuation | 273 | 48 | missing_valuation_data: 30, pe_valuation_percentile: 127, pb_valuation_percentile: 60, dividend_yield: 7, fcf_yield: 1 | 0.129 |
| step5_futu_executor | 48 | 48 | spread_too_wide: 42 | 0.003 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 2774 | 0 |
| step2_hard_filters | 2636 | 2425 | 216 | 2558 |
| step3_financial_quality | 245 | 2391 | 28 | 188 |
| step4_valuation | 48 | 197 | 0 | 28 |
| step5_futu_executor | 48 | 42 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1451 |
| step2_hard_filters | listing_age | 187 | 291 |
| step2_hard_filters | liquidity | 422 | 603 |
| step2_hard_filters | market_cap | 1371 | 194 |
| step2_hard_filters | performance_floor | 444 | 19 |
| step3_financial_quality | profitability | 2181 | 164 |
| step3_financial_quality | leverage | 36 | 8 |
| step3_financial_quality | cash_flow_quality | 101 | 7 |
| step3_financial_quality | growth | 73 | 9 |
| step4_valuation | missing_valuation_data | 27 | 3 |
| step4_valuation | pe_valuation_percentile | 104 | 23 |
| step4_valuation | pb_valuation_percentile | 58 | 2 |
| step4_valuation | dividend_yield | 7 | 0 |
| step4_valuation | fcf_yield | 1 | 0 |
| step5_futu_executor | spread_too_wide | 42 | 0 |

## Step 5 Decisions

- Actions: `SKIP: 42, WATCH: 6`
- Reasons: `spread_too_wide: 42, passed_depth_scan: 6`

## WATCH / BUY Candidates

| code | name | market | industry | action | decision_reason | pe_ttm | pb | roe | dividend_yield | fcf_yield | spread_bps | risk_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | WATCH | passed_depth_scan | 18.21 | 2.933 | 0.1666 | 0.02899 | 0.07231 | 10 | OK |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | WATCH | passed_depth_scan | 10.54 | 1.045 | 0.106 | 0.0328 | 0.1749 | 14 | OK |
| 000848 | 承德露露 | CN | C 制造业 | WATCH | passed_depth_scan | 13.4 | 2.21 | 0.1778 | 0.05821 | 0.1234 | 18 | OK |
| 000893 | 亚钾国际 | CN | C 制造业 | WATCH | passed_depth_scan | 24.94 | 3.037 | 0.1328 | 0.009311 | 0.05409 | 22 | OK |
| 000915 | 华特达因 | CN | C 制造业 | WATCH | passed_depth_scan | 12.06 | 2.169 | 0.1829 | 0.07194 | 0.1973 | 26 | OK |
| 000975 | 山金国际 | CN | B 采矿业 | WATCH | passed_depth_scan | 21.25 | 3.884 | 0.2156 | 0.01703 | 0.0742 | 30 | OK |

## Blocked / Skipped

| code | name | market | action | decision_reason | spread_bps |
| --- | --- | --- | --- | --- | --- |
| 000999 | 华润三九 | CN | SKIP | spread_too_wide | 34 |
| 001286 | 陕西能源 | CN | SKIP | spread_too_wide | 38 |
| 002001 | 新和成 | CN | SKIP | spread_too_wide | 42 |
| 002003 | 伟星股份 | CN | SKIP | spread_too_wide | 46 |
| 002020 | 京新药业 | CN | SKIP | spread_too_wide | 50 |
| 002128 | 电投能源 | CN | SKIP | spread_too_wide | 54 |
| 002170 | 芭田股份 | CN | SKIP | spread_too_wide | 58 |
| 002262 | 恩华药业 | CN | SKIP | spread_too_wide | 62 |
| 002444 | 巨星科技 | CN | SKIP | spread_too_wide | 66 |
| 002632 | 道明光学 | CN | SKIP | spread_too_wide | 70 |
| 002831 | 裕同科技 | CN | SKIP | spread_too_wide | 74 |
| 002833 | 弘亚数控 | CN | SKIP | spread_too_wide | 78 |
| 300009 | 安科生物 | CN | SKIP | spread_too_wide | 82 |
| 300043 | 星辉娱乐 | CN | SKIP | spread_too_wide | 86 |
| 300470 | 中密控股 | CN | SKIP | spread_too_wide | 90 |
| 300533 | 冰川网络 | CN | SKIP | spread_too_wide | 94 |
| 300705 | 九典制药 | CN | SKIP | spread_too_wide | 98 |
| 301061 | 匠心家居 | CN | SKIP | spread_too_wide | 102 |
| 301219 | 腾远钴业 | CN | SKIP | spread_too_wide | 106 |
| 600007 | 中国国贸 | CN | SKIP | spread_too_wide | 110 |
