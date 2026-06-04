# DailyStock GitHub Actions Result

- Tag: `-`
- Run: [#27](https://github.com/chyizhiyu/DailyStock/actions/runs/26940244668)
- Source commit: `f2ee2a764ab7`
- Run attempt: `1`

# DailyStock Weekly Screen

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7835 | - | 248.731 |
| step2_hard_filters | 7835 | 2772 | risk_screen: 1449, listing_age: 571, liquidity: 1000, market_cap: 1584, performance_floor: 459 | 0.858 |
| step3_financial_quality | 2772 | 260 | profitability: 2281, leverage: 42, cash_flow_quality: 105, growth: 84 | 0.072 |
| step4_valuation | 260 | 45 | missing_valuation_data: 29, pe_valuation_percentile: 115, pb_valuation_percentile: 63, dividend_yield: 8 | 0.291 |
| step5_futu_executor | 45 | 45 | spread_too_wide: 39 | 0.008 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 2774 | 0 |
| step2_hard_filters | 2548 | 2513 | 224 | 2550 |
| step3_financial_quality | 230 | 2318 | 30 | 194 |
| step4_valuation | 45 | 185 | 0 | 30 |
| step5_futu_executor | 45 | 39 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1448 |
| step2_hard_filters | listing_age | 283 | 288 |
| step2_hard_filters | liquidity | 426 | 574 |
| step2_hard_filters | market_cap | 1364 | 220 |
| step2_hard_filters | performance_floor | 439 | 20 |
| step3_financial_quality | profitability | 2114 | 167 |
| step3_financial_quality | leverage | 34 | 8 |
| step3_financial_quality | cash_flow_quality | 98 | 7 |
| step3_financial_quality | growth | 72 | 12 |
| step4_valuation | missing_valuation_data | 26 | 3 |
| step4_valuation | pe_valuation_percentile | 90 | 25 |
| step4_valuation | pb_valuation_percentile | 61 | 2 |
| step4_valuation | dividend_yield | 8 | 0 |
| step5_futu_executor | spread_too_wide | 39 | 0 |

## Step 5 Decisions

- Actions: `SKIP: 39, WATCH: 6`
- Reasons: `spread_too_wide: 39, passed_depth_scan: 6`

## WATCH / BUY Candidates

| code | name | market | industry | action | decision_reason | pe_ttm | pb | roe | dividend_yield | fcf_yield | spread_bps | risk_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | WATCH | passed_depth_scan | 18 | 2.9 | 0.1666 | 0.02899 | 0.07314 | 10 | OK |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | WATCH | passed_depth_scan | 10.29 | 1.02 | 0.106 | 0.03399 | 0.1792 | 14 | OK |
| 000848 | 承德露露 | CN | C 制造业 | WATCH | passed_depth_scan | 13.18 | 2.174 | 0.1778 | 0.05821 | 0.1255 | 18 | OK |
| 000893 | 亚钾国际 | CN | C 制造业 | WATCH | passed_depth_scan | 24.52 | 2.986 | 0.1328 | 0.009311 | 0.055 | 22 | OK |
| 000915 | 华特达因 | CN | C 制造业 | WATCH | passed_depth_scan | 11.85 | 2.131 | 0.1829 | 0.07402 | 0.2008 | 26 | OK |
| 000975 | 山金国际 | CN | B 采矿业 | WATCH | passed_depth_scan | 20.75 | 3.792 | 0.2156 | 0.01703 | 0.076 | 30 | OK |

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
| 301303 | 真兰仪表 | CN | SKIP | spread_too_wide | 110 |
