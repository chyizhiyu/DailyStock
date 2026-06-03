# DailyStock Funnel Dashboard

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

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 18.21 | 0.3134 | 2.933 | 0.4736 | 0.02899 | 0.07231 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.54 | 0.1379 | 1.045 | 0.1034 | 0.0328 | 0.1749 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.4 | 0.2611 | 2.21 | 0.3081 | 0.05821 | 0.1234 |
| 000893 | 亚钾国际 | CN | C 制造业 | 0.1328 | 24.94 | 0.3869 | 3.037 | 0.4915 | 0.009311 | 0.05409 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 12.06 | 0.2495 | 2.169 | 0.2965 | 0.07194 | 0.1973 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 21.25 | 0.3103 | 3.884 | 0.4483 | 0.01703 | 0.0742 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.77 | 0.2479 | 1.736 | 0.1765 | 0.02437 | 0.1366 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 16.18 | 0.3103 | 1.765 | 0.4138 | 0.03125 | 0.1853 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.59 | 0.2643 | 2.627 | 0.4144 | 0.02609 | 0.09532 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 17.34 | 0.3007 | 2.427 | 0.3695 | 0.04053 | 0.1 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 14.04 | 0.2674 | 1.826 | 0.1998 | 0.02668 | 0.07024 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 12.62 | 0.1724 | 2.272 | 0.3448 | 0.0331 | 0.102 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 12.45 | 0.2532 | 2.816 | 0.4493 | 0.04338 | 0.1292 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 18.98 | 0.3224 | 2.417 | 0.3652 | 0.01974 | 0.05327 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 15.44 | 0.2828 | 2.026 | 0.2637 | 0.01243 | 0.05961 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 29.34 | 0.4313 | 2.881 | 0.4598 | 0.01458 | 0.06993 |
| 002831 | 裕同科技 | CN | C 制造业 | 0.1356 | 23.4 | 0.3689 | 3.056 | 0.4947 | 0.01623 | 0.07261 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 17.86 | 0.3081 | 2.562 | 0.4043 | 0.03077 | 0.08125 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 18.39 | 0.3161 | 2.849 | 0.454 | 0.03041 | 0.06387 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 19.33 | 0.4231 | 3.229 | 0.4017 | 0.01048 | 0.09347 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 16.58 | 0.2912 | 2.172 | 0.2997 | 0.01574 | 0.06333 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.689 | 0.3803 | 3.418 | 0.4444 | 0.03779 | 0.1299 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.99 | 0.2489 | 2.17 | 0.2986 | 0.03303 | 0.1124 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.33 | 0.24 | 2.655 | 0.4207 | 0.00878 | 0.06814 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 20.73 | 0.343 | 2.334 | 0.3388 | 0.01427 | 0.0405 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 17.78 | 0.3934 | 2.12 | 0.4106 | 0.04911 | 0.0739 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.5 | 0.342 | 2.068 | 0.3967 | 0.0375 | 0.1281 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 21.65 | 0.4476 | 2.028 | 0.3855 | 0.02049 | 0.07557 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.54 | 0.2753 | 1.441 | 0.2271 | 0.02235 | 0.08532 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 14.11 | 0.3369 | 1.496 | 0.2433 | 0.03763 | 0.1043 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.91 | 0.3119 | 1.449 | 0.2275 | 0.06203 | 0.1606 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 10.94 | 0.2822 | 1.158 | 0.1381 | 0.03102 | 0.1584 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 17.78 | 0.3934 | 2.515 | 0.488 | 0.03852 | 0.0563 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.12 | 0.3179 | 1.622 | 0.285 | 0.02562 | 0.127 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 14.07 | 0.335 | 2.054 | 0.3948 | 0.01412 | 0.1216 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.66 | 0.3906 | 2.238 | 0.4361 | 0.02878 | 0.05843 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 9.75 | 0.2683 | 1.512 | 0.2479 | 0.05317 | 0.1697 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.36 | 0.4022 | 2.203 | 0.4277 | 0.02135 | 0.07084 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 17.67 | 0.3911 | 1.911 | 0.3582 | 0.02021 | 0.07928 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.03 | 0.2702 | 1.142 | 0.1353 | 0.04624 | 0.1644 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 14.91 | 0.3489 | 1.98 | 0.3726 | 0.01508 | 0.07743 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 17.83 | 0.3943 | 2.207 | 0.4286 | 0.0166 | 0.05654 |
| 603202 | 天有为 | CN | SW_UNKNOWN | 0.1623 | 10.35 | 0.2729 | 1.515 | 0.2488 | 0.02276 | 0.1025 |
| 603391 | 力聚热能 | CN | SW_UNKNOWN | 0.1037 | 23.27 | 0.4699 | 2.315 | 0.4509 | 0.02329 | 0.06589 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.27 | 0.2854 | 1.977 | 0.3703 | 0.03102 | 0.1064 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.62 | 0.3772 | 1.938 | 0.3633 | 0.03205 | 0.07555 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 13.33 | 0.3216 | 2.173 | 0.4222 | 0.04695 | 0.1152 |
| 605338 | 巴比食品 | CN | SW_UNKNOWN | 0.1197 | 18.86 | 0.4096 | 2.16 | 0.4189 | 0.05124 | 0.06201 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 3.164 | 3.167 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.114 | 2.117 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000893 | WATCH | passed_depth_scan | 4.215 | 4.224 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 6.298 | 6.317 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 4.029 | 4.043 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 4.843 | 4.862 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.21 | 9.249 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.132 | 1.137 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.11 | 1.115 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.998 | 9.047 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.137 | 1.143 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.018 | 2.031 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.862 | 3.888 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002831 | SKIP | spread_too_wide | 3.756 | 3.783 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.346 | 1.357 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.152 | 1.164 | 102 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.292 | 2.316 | 106 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 2.12 | 2.143 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.747 | 2.779 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.72 | 9.835 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.735 | 1.757 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.443 | 6.524 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.772 | 2.809 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.203 | 3.247 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 8.102 | 8.214 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.583 | 1.606 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 170.7 | 173.2 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 1.02 | 1.035 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.452 | 1.475 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 105.1 | 106.8 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.216 | 2.252 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.035 | 1.052 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.571 | 1.598 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603202 | SKIP | spread_too_wide | 1.032 | 1.05 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603391 | SKIP | spread_too_wide | 0.991 | 1.009 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.001 | 3.057 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.759 | 1.793 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.385 | 2.432 | 194 | normal | True | 0 | 0 | OK |  | True |
| 605338 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
