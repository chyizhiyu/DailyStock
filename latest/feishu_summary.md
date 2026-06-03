# DailyStock GitHub Actions Result

- Tag: `dailystock-20260603-122633`
- Run: [#20](https://github.com/chyizhiyu/DailyStock/actions/runs/26863657714)
- Source commit: `1020e726befc`
- Run attempt: `1`

# DailyStock Weekly Screen

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6288 | - | 177.727 |
| step2_hard_filters | 6288 | 2508 | risk_screen: 641, listing_age: 291, liquidity: 1563, market_cap: 862, performance_floor: 423 | 0.530 |
| step3_financial_quality | 2508 | 233 | profitability: 2081, leverage: 32, cash_flow_quality: 95, growth: 67 | 0.059 |
| step4_valuation | 233 | 44 | missing_valuation_data: 25, pe_valuation_percentile: 99, pb_valuation_percentile: 58, dividend_yield: 6, fcf_yield: 1 | 0.227 |
| step5_futu_executor | 44 | 44 | spread_too_wide: 38 | 0.006 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 1227 | 0 |
| step2_hard_filters | 2508 | 2553 | 0 | 1227 |
| step3_financial_quality | 233 | 2275 | 0 | 0 |
| step4_valuation | 44 | 189 | 0 | 0 |
| step5_futu_executor | 44 | 38 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 640 |
| step2_hard_filters | listing_age | 187 | 104 |
| step2_hard_filters | liquidity | 1080 | 483 |
| step2_hard_filters | market_cap | 862 | 0 |
| step2_hard_filters | performance_floor | 423 | 0 |
| step3_financial_quality | profitability | 2081 | 0 |
| step3_financial_quality | leverage | 32 | 0 |
| step3_financial_quality | cash_flow_quality | 95 | 0 |
| step3_financial_quality | growth | 67 | 0 |
| step4_valuation | missing_valuation_data | 25 | 0 |
| step4_valuation | pe_valuation_percentile | 99 | 0 |
| step4_valuation | pb_valuation_percentile | 58 | 0 |
| step4_valuation | dividend_yield | 6 | 0 |
| step4_valuation | fcf_yield | 1 | 0 |
| step5_futu_executor | spread_too_wide | 38 | 0 |

## Step 5 Decisions

- Actions: `SKIP: 38, WATCH: 6`
- Reasons: `spread_too_wide: 38, passed_depth_scan: 6`

## WATCH / BUY Candidates

| code | name | market | industry | action | decision_reason | pe_ttm | pb | roe | dividend_yield | fcf_yield | spread_bps | risk_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | WATCH | passed_depth_scan | 18.26 | 2.942 | 0.1666 | 0.02899 | 0.07209 | 10 | OK |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | WATCH | passed_depth_scan | 10.46 | 1.037 | 0.106 | 0.0328 | 0.1762 | 14 | OK |
| 000848 | 承德露露 | CN | C 制造业 | WATCH | passed_depth_scan | 13.37 | 2.204 | 0.1778 | 0.05821 | 0.1237 | 18 | OK |
| 000893 | 亚钾国际 | CN | C 制造业 | WATCH | passed_depth_scan | 24.85 | 3.025 | 0.1328 | 0.009311 | 0.05429 | 22 | OK |
| 000915 | 华特达因 | CN | C 制造业 | WATCH | passed_depth_scan | 12.04 | 2.165 | 0.1829 | 0.07194 | 0.1977 | 26 | OK |
| 000975 | 山金国际 | CN | B 采矿业 | WATCH | passed_depth_scan | 21.51 | 3.932 | 0.2156 | 0.01703 | 0.0733 | 30 | OK |

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
| 300533 | 冰川网络 | CN | SKIP | spread_too_wide | 90 |
| 300705 | 九典制药 | CN | SKIP | spread_too_wide | 94 |
| 301061 | 匠心家居 | CN | SKIP | spread_too_wide | 98 |
| 301219 | 腾远钴业 | CN | SKIP | spread_too_wide | 102 |
| 600007 | 中国国贸 | CN | SKIP | spread_too_wide | 106 |
| 600012 | 皖通高速 | CN | SKIP | spread_too_wide | 110 |
