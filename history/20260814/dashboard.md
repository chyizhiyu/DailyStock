# DailyStock Funnel Dashboard

- As of: `2026-08-14`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7927 | - | 369.545 |
| step2_hard_filters | 7927 | 2733 | risk_screen: 1464, listing_age: 455, liquidity: 1347, market_cap: 1509, performance_floor: 419 | 0.588 |
| step3_financial_quality | 2733 | 263 | profitability: 2239, leverage: 47, cash_flow_quality: 103, growth: 81 | 0.066 |
| step4_valuation | 263 | 56 | missing_valuation_data: 7, pe_valuation_percentile: 125, pb_valuation_percentile: 66, dividend_yield: 9 | 0.249 |
| step5_futu_executor | 56 | 56 | spread_too_wide: 50 | 0.007 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5126 | 0 | 2801 | 0 |
| step2_hard_filters | 2509 | 2617 | 224 | 2577 |
| step3_financial_quality | 239 | 2270 | 24 | 200 |
| step4_valuation | 56 | 183 | 0 | 24 |
| step5_futu_executor | 56 | 50 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 1461 |
| step2_hard_filters | listing_age | 163 | 292 |
| step2_hard_filters | liquidity | 712 | 635 |
| step2_hard_filters | market_cap | 1340 | 169 |
| step2_hard_filters | performance_floor | 399 | 20 |
| step3_financial_quality | profitability | 2062 | 177 |
| step3_financial_quality | leverage | 39 | 8 |
| step3_financial_quality | cash_flow_quality | 98 | 5 |
| step3_financial_quality | growth | 71 | 10 |
| step4_valuation | missing_valuation_data | 5 | 2 |
| step4_valuation | pe_valuation_percentile | 105 | 20 |
| step4_valuation | pb_valuation_percentile | 64 | 2 |
| step4_valuation | dividend_yield | 9 | 0 |
| step5_futu_executor | spread_too_wide | 50 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.58 | 0.2241 | 1.049 | 0.2414 | 0.03439 | 0.1742 |
| 000600 | 建投能源 | CN | D 水电煤气 | 0.1658 | 7.921 | 0.1207 | 1.189 | 0.3793 | 0.01864 | 0.3651 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 21.29 | 0.3697 | 2.272 | 0.3782 | 0.01675 | 0.0761 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.31 | 0.2468 | 2.033 | 0.3046 | 0.07065 | 0.2105 |
| 000920 | 沃顿科技 | CN | C 制造业 | 0.1139 | 24.98 | 0.4212 | 2.759 | 0.4874 | 0.01148 | 0.05394 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 24.07 | 0.3667 | 4.4 | 0.4667 | 0.01703 | 0.0655 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.99 | 0.2532 | 1.769 | 0.2201 | 0.02437 | 0.1341 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 13.18 | 0.2586 | 1.438 | 0.431 | 0.03755 | 0.2275 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 17.93 | 0.3204 | 2.508 | 0.4328 | 0.04053 | 0.09678 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 15.27 | 0.291 | 1.985 | 0.2894 | 0.02778 | 0.06459 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.11 | 0.1667 | 2.117 | 0.3 | 0.0331 | 0.1095 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 18.42 | 0.3293 | 2.593 | 0.4485 | 0.009532 | 0.04889 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.79 | 0.2516 | 2.667 | 0.4638 | 0.04338 | 0.1364 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.91 | 0.3655 | 2.664 | 0.4622 | 0.01974 | 0.04834 |
| 002275 | 桂林三金 | CN | C 制造业 | 0.1389 | 18.01 | 0.322 | 2.356 | 0.4028 | 0.02244 | 0.09041 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 17.25 | 0.3078 | 2.335 | 0.3981 | 0.02012 | 0.06197 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14.13 | 0.2784 | 1.855 | 0.2463 | 0.01326 | 0.06511 |
| 002545 | 东方铁塔 | CN | C 制造业 | 0.1297 | 17.69 | 0.3151 | 2.088 | 0.3188 | 0.01913 | 0.1119 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 25.34 | 0.4249 | 1.986 | 0.2904 | 0.01238 | 0.04645 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 24.37 | 0.4112 | 2.393 | 0.4118 | 0.01458 | 0.0842 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.11 | 0.3246 | 2.627 | 0.4527 | 0.03077 | 0.07923 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.54 | 0.2595 | 2.265 | 0.3771 | 0.05394 | 0.08061 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 23.07 | 0.4179 | 2.279 | 0.3433 | 0.009588 | 0.08489 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 20.6 | 0.437 | 2.119 | 0.1681 | 0.007937 | 0.06892 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 24.91 | 0.3571 | 3.515 | 0.5 | 0.0111 | 0.07374 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 20.08 | 0.4286 | 3.354 | 0.4916 | 0.01185 | 0.08997 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 23.2 | 0.3992 | 2.419 | 0.4165 | 0.014 | 0.03712 |
| 300286 | 安科瑞 | CN | C 制造业 | 0.1025 | 23.98 | 0.4049 | 2.244 | 0.3703 | 0.01405 | 0.04309 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.87 | 0.2447 | 1.447 | 0.1308 | 0.02034 | 0.08246 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 15.17 | 0.2894 | 1.988 | 0.2915 | 0.01626 | 0.0692 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.432 | 0.3782 | 3.303 | 0.4748 | 0.03779 | 0.1344 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.77 | 0.2437 | 2.349 | 0.4002 | 0.02579 | 0.1442 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 13.15 | 0.2647 | 2.379 | 0.4081 | 0.03303 | 0.1025 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 11.11 | 0.2463 | 2.688 | 0.4711 | 0.03286 | 0.07018 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 12.84 | 0.2631 | 1.877 | 0.2558 | 0.01274 | 0.05036 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 17.2 | 0.3072 | 1.688 | 0.1964 | 0.01989 | 0.05545 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.48 | 0.3528 | 2.066 | 0.4289 | 0.03634 | 0.1283 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 20.21 | 0.4491 | 1.895 | 0.3849 | 0.02544 | 0.08087 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.03 | 0.2752 | 1.371 | 0.2298 | 0.02256 | 0.08964 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.13 | 0.3298 | 1.474 | 0.2656 | 0.06203 | 0.1579 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 9.943 | 0.2734 | 1.052 | 0.1261 | 0.03224 | 0.1744 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.63 | 0.3748 | 2.21 | 0.4601 | 0.04277 | 0.06406 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.59 | 0.3009 | 1.433 | 0.2486 | 0.02672 | 0.1437 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 12.71 | 0.3243 | 1.855 | 0.3739 | 0.01689 | 0.1346 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.29 | 0.4032 | 2.191 | 0.455 | 0.02841 | 0.05968 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 9.56 | 0.2706 | 1.482 | 0.2697 | 0.05378 | 0.173 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 16.81 | 0.3954 | 2.017 | 0.417 | 0.0245 | 0.07738 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 10.73 | 0.2881 | 1.198 | 0.1739 | 0.02239 | 0.09837 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.03 | 0.2743 | 1.142 | 0.155 | 0.0464 | 0.1644 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.06 | 0.3275 | 1.734 | 0.344 | 0.01977 | 0.08844 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 17.03 | 0.4 | 2.108 | 0.4394 | 0.01694 | 0.05921 |
| 603202 | 天有为 | CN | SW_UNKNOWN | 0.1623 | 8.31 | 0.2601 | 1.217 | 0.1794 | 0.02271 | 0.1276 |
| 603402 | 陕西旅游 | CN | SW_UNKNOWN | 0.2774 | 9.642 | 0.2716 | 2.181 | 0.4528 | 0.02117 | 0.08238 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.92 | 0.3078 | 2.087 | 0.4344 | 0.03102 | 0.1008 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 18 | 0.4119 | 2.1 | 0.4372 | 0.03908 | 0.06973 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.56 | 0.2862 | 1.94 | 0.3968 | 0.05941 | 0.129 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.124 | 2.126 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000600 | WATCH | passed_depth_scan | 1.483 | 1.485 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.574 | 3.58 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000920 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 7.134 | 7.156 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 4.105 | 4.119 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.945 | 3.96 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.17 | 1.175 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.207 | 1.213 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.386 | 8.428 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.366 | 2.379 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.077 | 1.083 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.224 | 2.238 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002275 | SKIP | spread_too_wide | 0.997 | 1.003 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.173 | 1.182 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.534 | 3.561 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002545 | SKIP | spread_too_wide | 2.125 | 2.142 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.874 | 1.89 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.116 | 1.127 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.648 | 1.665 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 8.057 | 8.143 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.086 | 1.099 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300286 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.994 | 1.006 | 126 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.993 | 1.007 | 134 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.993 | 1.007 | 138 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.057 | 1.072 | 142 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 1.839 | 1.866 | 146 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.993 | 1.008 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.738 | 2.781 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.065 | 9.209 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.648 | 1.675 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.815 | 2.862 | 166 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 2.905 | 2.955 | 170 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 7.106 | 7.231 | 174 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.397 | 1.422 | 178 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 153.9 | 156.7 | 182 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.997 | 1.015 | 186 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.422 | 1.449 | 190 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 96.05 | 97.94 | 194 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 5.585 | 5.697 | 198 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.033 | 1.054 | 202 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.373 | 1.402 | 206 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.99 | 1.01 | 210 | normal | True | 0 | 0 | OK |  | True |
| 603202 | SKIP | spread_too_wide | 0.989 | 1.011 | 214 | normal | True | 0 | 0 | OK |  | True |
| 603402 | SKIP | spread_too_wide | 0.989 | 1.011 | 218 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.162 | 3.233 | 222 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.902 | 1.946 | 226 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.126 | 2.175 | 230 | normal | True | 0 | 0 | OK |  | True |
