# DailyStock GitHub Actions Result

- Tag: `dailystock-20260602-200735`
- Run: [#17](https://github.com/chyizhiyu/DailyStock/actions/runs/26818660572)
- Source commit: `b02f513c2b17`
- Run attempt: `1`

# DailyStock Weekly Screen

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6288 | - | 875.088 |
| step2_hard_filters | 6288 | 2599 | risk_screen: 641, listing_age: 387, liquidity: 768, market_cap: 1450, performance_floor: 443 | 0.538 |
| step3_financial_quality | 2599 | 235 | profitability: 2156, leverage: 35, cash_flow_quality: 100, growth: 73 | 0.060 |
| step4_valuation | 235 | 48 | missing_valuation_data: 28, pe_valuation_percentile: 92, pb_valuation_percentile: 60, dividend_yield: 7 | 0.229 |
| step5_futu_executor | 48 | 48 | spread_too_wide: 42 | 0.007 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 1227 | 0 |
| step2_hard_filters | 2599 | 2462 | 0 | 1227 |
| step3_financial_quality | 235 | 2364 | 0 | 0 |
| step4_valuation | 48 | 187 | 0 | 0 |
| step5_futu_executor | 48 | 42 | 0 | 0 |

## Step 5 Decisions

- Actions: `SKIP: 42, WATCH: 6`
- Reasons: `spread_too_wide: 42, passed_depth_scan: 6`

## WATCH / BUY Candidates

| code | name | market | industry | action | decision_reason | pe_ttm | pb | roe | dividend_yield | fcf_yield | spread_bps | risk_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | WATCH | passed_depth_scan | 18.66 | 3.005 | 0.1666 | 0.02899 | 0.07057 | 10 | OK |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | WATCH | passed_depth_scan | 10.66 | 1.056 | 0.106 | 0.0328 | 0.173 | 14 | OK |
| 000848 | 承德露露 | CN | C 制造业 | WATCH | passed_depth_scan | 13.62 | 2.246 | 0.1778 | 0.05821 | 0.1215 | 18 | OK |
| 000893 | 亚钾国际 | CN | C 制造业 | WATCH | passed_depth_scan | 25.57 | 3.113 | 0.1328 | 0.009311 | 0.05276 | 22 | OK |
| 000915 | 华特达因 | CN | C 制造业 | WATCH | passed_depth_scan | 12.19 | 2.192 | 0.1829 | 0.07194 | 0.1952 | 26 | OK |
| 000975 | 山金国际 | CN | B 采矿业 | WATCH | passed_depth_scan | 21.52 | 3.934 | 0.2156 | 0.01703 | 0.07326 | 30 | OK |

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
| 300130 | 新国都 | CN | SKIP | spread_too_wide | 90 |
| 300470 | 中密控股 | CN | SKIP | spread_too_wide | 94 |
| 300533 | 冰川网络 | CN | SKIP | spread_too_wide | 98 |
| 300705 | 九典制药 | CN | SKIP | spread_too_wide | 102 |
| 301061 | 匠心家居 | CN | SKIP | spread_too_wide | 106 |
| 301219 | 腾远钴业 | CN | SKIP | spread_too_wide | 110 |
