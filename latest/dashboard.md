# DailyStock Funnel Dashboard

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6288 | - | 265.114 |
| step2_hard_filters | 6288 | 2661 | risk_screen: 641, listing_age: 291, liquidity: 779, market_cap: 1468, performance_floor: 448 | 0.788 |
| step3_financial_quality | 2661 | 248 | profitability: 2202, leverage: 36, cash_flow_quality: 102, growth: 73 | 0.063 |
| step4_valuation | 248 | 51 | missing_valuation_data: 28, pe_valuation_percentile: 102, pb_valuation_percentile: 60, dividend_yield: 7 | 0.281 |
| step5_futu_executor | 51 | 51 | spread_too_wide: 45 | 0.009 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 18.66 | 0.314 | 3.005 | 0.4815 | 0.02899 | 0.07057 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.66 | 0.1379 | 1.056 | 0.1034 | 0.0328 | 0.173 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.62 | 0.2611 | 2.246 | 0.3134 | 0.05821 | 0.1215 |
| 000893 | 亚钾国际 | CN | C 制造业 | 0.1328 | 25.57 | 0.3922 | 3.113 | 0.4974 | 0.009311 | 0.05276 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 12.19 | 0.2489 | 2.192 | 0.2976 | 0.07194 | 0.1952 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 21.52 | 0.3103 | 3.934 | 0.4483 | 0.01703 | 0.07326 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.93 | 0.2479 | 1.76 | 0.1771 | 0.02437 | 0.1348 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 16.4 | 0.3276 | 1.79 | 0.431 | 0.03125 | 0.1827 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.69 | 0.2627 | 2.646 | 0.4149 | 0.02609 | 0.09463 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 17.07 | 0.2955 | 2.388 | 0.3525 | 0.04053 | 0.1016 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 14.26 | 0.269 | 1.854 | 0.203 | 0.02668 | 0.06917 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 12.97 | 0.1724 | 1.773 | 0.2414 | 0.0331 | 0.1308 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 12.55 | 0.2521 | 2.84 | 0.4445 | 0.04338 | 0.1281 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 19.3 | 0.3235 | 2.457 | 0.3689 | 0.01974 | 0.0524 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 15.32 | 0.2807 | 2.01 | 0.2542 | 0.01243 | 0.0601 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 29.66 | 0.4345 | 2.911 | 0.4609 | 0.01458 | 0.06919 |
| 002831 | 裕同科技 | CN | C 制造业 | 0.1356 | 23.43 | 0.3689 | 3.061 | 0.4905 | 0.01623 | 0.07251 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 17.93 | 0.3066 | 2.572 | 0.3996 | 0.03077 | 0.08093 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 18.8 | 0.3166 | 2.913 | 0.4619 | 0.03041 | 0.06248 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 19.88 | 0.4231 | 3.319 | 0.4145 | 0.01048 | 0.09092 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 28.68 | 0.4244 | 2.989 | 0.4789 | 0.01261 | 0.03004 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 16.97 | 0.2933 | 2.223 | 0.3071 | 0.01574 | 0.06187 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.762 | 0.3803 | 3.45 | 0.4402 | 0.03779 | 0.1287 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 12.53 | 0.2516 | 2.268 | 0.3224 | 0.03303 | 0.1075 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.45 | 0.24 | 2.686 | 0.4207 | 0.00878 | 0.06736 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 20.61 | 0.3362 | 2.32 | 0.3351 | 0.01427 | 0.04075 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 18.31 | 0.3999 | 2.183 | 0.4212 | 0.04911 | 0.07176 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 15.78 | 0.3619 | 2.251 | 0.4337 | 0.0375 | 0.1177 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 22.45 | 0.4574 | 2.103 | 0.4004 | 0.02049 | 0.07289 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.63 | 0.2743 | 1.453 | 0.2243 | 0.02235 | 0.08456 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 14.28 | 0.3369 | 1.513 | 0.2433 | 0.03763 | 0.1031 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.04 | 0.3119 | 1.464 | 0.2266 | 0.06203 | 0.159 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 10.74 | 0.2771 | 1.136 | 0.1311 | 0.03102 | 0.1615 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 18.14 | 0.3957 | 2.566 | 0.494 | 0.03852 | 0.05518 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 12.11 | 0.2938 | 1.264 | 0.1677 | 0.02523 | 0.1275 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.23 | 0.3146 | 1.635 | 0.2831 | 0.02562 | 0.1259 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.69 | 0.3239 | 1.997 | 0.3703 | 0.01412 | 0.125 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 18.02 | 0.3939 | 2.283 | 0.4416 | 0.02878 | 0.05728 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 9.922 | 0.2683 | 1.538 | 0.2521 | 0.05317 | 0.1667 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.14 | 0.3953 | 2.176 | 0.4194 | 0.02135 | 0.07174 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 17.96 | 0.393 | 1.942 | 0.3596 | 0.02021 | 0.07801 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 10.3 | 0.2711 | 1.037 | 0.1066 | 0.03211 | 0.09347 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.26 | 0.2706 | 1.169 | 0.1381 | 0.04624 | 0.1606 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 15.02 | 0.3489 | 1.995 | 0.3698 | 0.01508 | 0.07685 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 18.12 | 0.3948 | 2.243 | 0.431 | 0.0166 | 0.05564 |
| 603202 | 天有为 | CN | SW_UNKNOWN | 0.1623 | 10.48 | 0.2729 | 1.534 | 0.2488 | 0.02276 | 0.1012 |
| 603391 | 力聚热能 | CN | SW_UNKNOWN | 0.1037 | 23.88 | 0.4759 | 2.375 | 0.4597 | 0.02329 | 0.06421 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.41 | 0.285 | 2.002 | 0.3716 | 0.03102 | 0.105 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 17.01 | 0.3777 | 1.984 | 0.3675 | 0.03205 | 0.07381 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 13.36 | 0.3188 | 2.178 | 0.4198 | 0.04695 | 0.1149 |
| 605338 | 巴比食品 | CN | SW_UNKNOWN | 0.1197 | 19.06 | 0.4129 | 2.183 | 0.4212 | 0.05124 | 0.06136 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 3.242 | 3.245 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.138 | 2.141 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000893 | WATCH | passed_depth_scan | 4.321 | 4.33 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 6.378 | 6.397 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 4.084 | 4.098 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 4.911 | 4.929 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.278 | 9.317 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.114 | 1.119 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.127 | 1.132 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 7.02 | 7.058 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.147 | 1.153 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.052 | 2.064 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.831 | 3.857 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002831 | SKIP | spread_too_wide | 3.761 | 3.789 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.376 | 1.387 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.344 | 1.356 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.165 | 1.177 | 106 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.277 | 2.302 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 2.182 | 2.207 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.989 | 3.025 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 10.08 | 10.2 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.75 | 1.773 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.517 | 6.602 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.8 | 2.838 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.142 | 3.186 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 8.264 | 8.382 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.993 | 1.007 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.596 | 1.62 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 165.9 | 168.5 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 1.04 | 1.057 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.477 | 1.502 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 103.8 | 105.5 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.252 | 2.29 | 170 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.6 | 1.628 | 174 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.059 | 1.078 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.582 | 1.611 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603202 | SKIP | spread_too_wide | 1.045 | 1.065 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603391 | SKIP | spread_too_wide | 0.99 | 1.01 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.038 | 3.098 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.799 | 1.836 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.389 | 2.439 | 206 | normal | True | 0 | 0 | OK |  | True |
| 605338 | SKIP | spread_too_wide | 0.99 | 1.01 | 210 | normal | True | 0 | 0 | OK |  | True |
