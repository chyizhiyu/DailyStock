# DailyStock GitHub Actions Result

- Tag: `-`
- Run: [#29](https://github.com/chyizhiyu/DailyStock/actions/runs/27012760697)
- Source commit: `f2ee2a764ab7`
- Run attempt: `1`

# DailyStock Weekly Screen

- As of: `2026-06-05`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6287 | - | 711.362 |
| step2_hard_filters | 6287 | 2620 | risk_screen: 640, listing_age: 288, liquidity: 817, market_cap: 1480, performance_floor: 442 | 0.433 |
| step3_financial_quality | 2620 | 245 | profitability: 2168, leverage: 35, cash_flow_quality: 101, growth: 71 | 0.046 |
| step4_valuation | 245 | 53 | missing_valuation_data: 21, pe_valuation_percentile: 100, pb_valuation_percentile: 62, dividend_yield: 8, fcf_yield: 1 | 0.185 |
| step5_futu_executor | 53 | 53 | spread_too_wide: 47 | 0.005 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 1226 | 0 |
| step2_hard_filters | 2620 | 2441 | 0 | 1226 |
| step3_financial_quality | 245 | 2375 | 0 | 0 |
| step4_valuation | 53 | 192 | 0 | 0 |
| step5_futu_executor | 53 | 47 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 639 |
| step2_hard_filters | listing_age | 182 | 106 |
| step2_hard_filters | liquidity | 336 | 481 |
| step2_hard_filters | market_cap | 1480 | 0 |
| step2_hard_filters | performance_floor | 442 | 0 |
| step3_financial_quality | profitability | 2168 | 0 |
| step3_financial_quality | leverage | 35 | 0 |
| step3_financial_quality | cash_flow_quality | 101 | 0 |
| step3_financial_quality | growth | 71 | 0 |
| step4_valuation | missing_valuation_data | 21 | 0 |
| step4_valuation | pe_valuation_percentile | 100 | 0 |
| step4_valuation | pb_valuation_percentile | 62 | 0 |
| step4_valuation | dividend_yield | 8 | 0 |
| step4_valuation | fcf_yield | 1 | 0 |
| step5_futu_executor | spread_too_wide | 47 | 0 |

## Step 5 Decisions

- Actions: `SKIP: 47, WATCH: 6`
- Reasons: `spread_too_wide: 47, passed_depth_scan: 6`

## WATCH / BUY Candidates

| code | name | market | industry | action | decision_reason | pe_ttm | pb | roe | dividend_yield | fcf_yield | spread_bps | risk_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | WATCH | passed_depth_scan | 18.37 | 2.959 | 0.1666 | 0.02899 | 0.07167 | 10 | OK |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | WATCH | passed_depth_scan | 10.21 | 1.012 | 0.106 | 0.03424 | 0.1805 | 14 | OK |
| 000791 | 甘肃能源 | CN | D 水电煤气 | WATCH | passed_depth_scan | 14.55 | 1.919 | 0.144 | 0.02561 | 0.1726 | 18 | OK |
| 000848 | 承德露露 | CN | C 制造业 | WATCH | passed_depth_scan | 13.22 | 2.18 | 0.1778 | 0.05821 | 0.1251 | 22 | OK |
| 000915 | 华特达因 | CN | C 制造业 | WATCH | passed_depth_scan | 11.96 | 2.151 | 0.1829 | 0.07331 | 0.1989 | 26 | OK |
| 000975 | 山金国际 | CN | B 采矿业 | WATCH | passed_depth_scan | 20.4 | 3.729 | 0.2156 | 0.01703 | 0.07729 | 30 | OK |

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
| 002967 | 广电计量 | CN | SKIP | spread_too_wide | 82 |
| 300009 | 安科生物 | CN | SKIP | spread_too_wide | 86 |
| 300043 | 星辉娱乐 | CN | SKIP | spread_too_wide | 90 |
| 300360 | 炬华科技 | CN | SKIP | spread_too_wide | 94 |
| 300470 | 中密控股 | CN | SKIP | spread_too_wide | 98 |
| 300533 | 冰川网络 | CN | SKIP | spread_too_wide | 102 |
| 300705 | 九典制药 | CN | SKIP | spread_too_wide | 106 |
| 301004 | 嘉益股份 | CN | SKIP | spread_too_wide | 110 |
