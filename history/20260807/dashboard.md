# DailyStock Funnel Dashboard

- As of: `2026-08-07`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6212 | - | 171.906 |
| step2_hard_filters | 6212 | 2522 | risk_screen: 515, listing_age: 268, liquidity: 1012, market_cap: 1499, performance_floor: 396 | 0.757 |
| step3_financial_quality | 2522 | 242 | profitability: 2072, leverage: 36, cash_flow_quality: 101, growth: 71 | 0.065 |
| step4_valuation | 242 | 53 | missing_valuation_data: 6, pe_valuation_percentile: 108, pb_valuation_percentile: 65, dividend_yield: 10 | 0.273 |
| step5_futu_executor | 53 | 53 | spread_too_wide: 47 | 0.009 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5126 | 0 | 1086 | 0 |
| step2_hard_filters | 2522 | 2604 | 0 | 1086 |
| step3_financial_quality | 242 | 2280 | 0 | 0 |
| step4_valuation | 53 | 189 | 0 | 0 |
| step5_futu_executor | 53 | 47 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 512 |
| step2_hard_filters | listing_age | 169 | 99 |
| step2_hard_filters | liquidity | 537 | 475 |
| step2_hard_filters | market_cap | 1499 | 0 |
| step2_hard_filters | performance_floor | 396 | 0 |
| step3_financial_quality | profitability | 2072 | 0 |
| step3_financial_quality | leverage | 36 | 0 |
| step3_financial_quality | cash_flow_quality | 101 | 0 |
| step3_financial_quality | growth | 71 | 0 |
| step4_valuation | missing_valuation_data | 6 | 0 |
| step4_valuation | pe_valuation_percentile | 108 | 0 |
| step4_valuation | pb_valuation_percentile | 65 | 0 |
| step4_valuation | dividend_yield | 10 | 0 |
| step5_futu_executor | spread_too_wide | 47 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.58 | 0.2069 | 1.049 | 0.2241 | 0.03439 | 0.1742 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 21.23 | 0.3729 | 2.264 | 0.3845 | 0.01675 | 0.07634 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 14.65 | 0.2836 | 2.416 | 0.4202 | 0.05821 | 0.1129 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.32 | 0.2463 | 2.036 | 0.3104 | 0.07065 | 0.2102 |
| 000920 | 沃顿科技 | CN | C 制造业 | 0.1139 | 24.68 | 0.417 | 2.726 | 0.4853 | 0.01148 | 0.05459 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 24.61 | 0.3667 | 4.499 | 0.4667 | 0.01703 | 0.06406 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 12.2 | 0.2547 | 1.799 | 0.2358 | 0.02437 | 0.1318 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 13.09 | 0.2586 | 1.428 | 0.431 | 0.03755 | 0.229 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 18.56 | 0.3319 | 2.597 | 0.4585 | 0.04053 | 0.09346 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 15.63 | 0.292 | 2.032 | 0.3093 | 0.02778 | 0.06311 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.42 | 0.1667 | 2.177 | 0.3 | 0.0331 | 0.1065 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 18.73 | 0.3346 | 2.636 | 0.4664 | 0.009532 | 0.04809 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 12.25 | 0.2553 | 2.77 | 0.4958 | 0.04338 | 0.1313 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.8 | 0.3645 | 2.649 | 0.4701 | 0.01974 | 0.04861 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 17.59 | 0.3136 | 2.381 | 0.4118 | 0.02012 | 0.06079 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14.3 | 0.2789 | 1.876 | 0.2626 | 0.01326 | 0.06438 |
| 002545 | 东方铁塔 | CN | C 制造业 | 0.1297 | 19.05 | 0.3393 | 2.249 | 0.3787 | 0.01913 | 0.1039 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 23.86 | 0.4065 | 2.342 | 0.4039 | 0.01458 | 0.08601 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 17.92 | 0.3209 | 2.599 | 0.459 | 0.03077 | 0.08007 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 22.7 | 0.403 | 2.242 | 0.3731 | 0.009588 | 0.08627 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 20.85 | 0.4412 | 2.145 | 0.1639 | 0.007937 | 0.06811 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 25.23 | 0.3571 | 3.559 | 0.5 | 0.0111 | 0.07282 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 20.04 | 0.4328 | 3.347 | 0.4832 | 0.01185 | 0.09016 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 23.88 | 0.407 | 2.489 | 0.4333 | 0.014 | 0.03607 |
| 300286 | 安科瑞 | CN | C 制造业 | 0.1025 | 24.21 | 0.4102 | 2.266 | 0.386 | 0.01405 | 0.04268 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 11.19 | 0.2453 | 1.489 | 0.146 | 0.02034 | 0.08011 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 15.77 | 0.2931 | 2.066 | 0.3204 | 0.01626 | 0.06658 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.398 | 0.3782 | 3.288 | 0.4748 | 0.03779 | 0.135 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.8 | 0.2447 | 2.355 | 0.406 | 0.02579 | 0.1438 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.82 | 0.2521 | 2.14 | 0.3482 | 0.03303 | 0.114 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 9.518 | 0.2369 | 2.446 | 0.4249 | 0.00878 | 0.07397 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 13.28 | 0.2652 | 1.942 | 0.2883 | 0.01274 | 0.04868 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 17.27 | 0.3078 | 1.695 | 0.2038 | 0.01989 | 0.05522 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 15.38 | 0.3693 | 1.834 | 0.3752 | 0.05596 | 0.08545 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.46 | 0.3509 | 2.062 | 0.4353 | 0.03634 | 0.1285 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 21.42 | 0.4656 | 2.009 | 0.4202 | 0.02544 | 0.0763 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.26 | 0.2771 | 1.402 | 0.2445 | 0.02256 | 0.08766 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.44 | 0.3326 | 1.509 | 0.2803 | 0.06203 | 0.1543 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 9.943 | 0.2729 | 1.052 | 0.1252 | 0.03224 | 0.1744 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.94 | 0.378 | 2.254 | 0.4784 | 0.04277 | 0.06281 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.57 | 0.2986 | 1.43 | 0.2541 | 0.02672 | 0.144 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 12.19 | 0.3133 | 1.779 | 0.3601 | 0.01689 | 0.1404 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.38 | 0.4028 | 2.202 | 0.4656 | 0.02841 | 0.05938 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 9.569 | 0.2693 | 1.484 | 0.272 | 0.05378 | 0.1729 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 16.52 | 0.3872 | 1.982 | 0.4119 | 0.0245 | 0.07876 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.941 | 0.2725 | 1.133 | 0.1546 | 0.0464 | 0.1658 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.34 | 0.3289 | 1.771 | 0.3587 | 0.01977 | 0.08656 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 17.38 | 0.4032 | 2.152 | 0.4569 | 0.01694 | 0.058 |
| 603202 | 天有为 | CN | SW_UNKNOWN | 0.1623 | 8.426 | 0.2606 | 1.234 | 0.1881 | 0.02271 | 0.1259 |
| 603402 | 陕西旅游 | CN | SW_UNKNOWN | 0.2774 | 10.46 | 0.2821 | 2.31 | 0.4881 | 0.02117 | 0.07591 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.76 | 0.3018 | 2.06 | 0.4344 | 0.03102 | 0.1021 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 17.34 | 0.4014 | 2.023 | 0.4243 | 0.03908 | 0.0724 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 11.14 | 0.2899 | 1.816 | 0.3711 | 0.05941 | 0.1378 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.124 | 2.126 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.563 | 3.568 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000920 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 7.295 | 7.317 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 4.175 | 4.189 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.919 | 3.934 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.211 | 1.216 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.235 | 1.241 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.62 | 8.663 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.405 | 2.419 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.119 | 1.125 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.212 | 2.225 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.196 | 1.204 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.576 | 3.601 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002545 | SKIP | spread_too_wide | 2.289 | 2.306 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.099 | 1.108 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.668 | 1.684 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 8.164 | 8.241 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.119 | 1.13 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300286 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 126 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.06 | 1.073 | 130 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 1.904 | 1.929 | 134 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.993 | 1.007 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.83 | 1.856 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.734 | 2.774 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.611 | 9.757 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.686 | 1.712 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.883 | 2.929 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 2.907 | 2.954 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 7.251 | 7.373 | 166 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.394 | 1.418 | 170 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 147.6 | 150.2 | 174 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 1.002 | 1.02 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.423 | 1.45 | 182 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 94.42 | 96.19 | 186 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.025 | 1.044 | 190 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.404 | 1.431 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603202 | SKIP | spread_too_wide | 0.99 | 1.01 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603402 | SKIP | spread_too_wide | 0.99 | 1.01 | 206 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.124 | 3.19 | 210 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.833 | 1.873 | 214 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 1.991 | 2.035 | 218 | normal | True | 0 | 0 | OK |  | True |
