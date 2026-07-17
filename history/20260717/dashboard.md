# DailyStock Funnel Dashboard

- As of: `2026-07-17`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7940 | - | 615.723 |
| step2_hard_filters | 7940 | 2572 | risk_screen: 1484, listing_age: 578, liquidity: 842, market_cap: 2093, performance_floor: 371 | 0.318 |
| step3_financial_quality | 2572 | 251 | profitability: 2101, leverage: 41, cash_flow_quality: 101, growth: 78 | 0.033 |
| step4_valuation | 251 | 46 | missing_valuation_data: 7, pe_valuation_percentile: 116, pb_valuation_percentile: 73, dividend_yield: 9 | 0.121 |
| step5_futu_executor | 46 | 46 | spread_too_wide: 40 | 0.003 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5129 | 0 | 2811 | 0 |
| step2_hard_filters | 2364 | 2765 | 208 | 2603 |
| step3_financial_quality | 228 | 2136 | 23 | 185 |
| step4_valuation | 46 | 182 | 0 | 23 |
| step5_futu_executor | 46 | 40 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 1481 |
| step2_hard_filters | listing_age | 284 | 294 |
| step2_hard_filters | liquidity | 274 | 568 |
| step2_hard_filters | market_cap | 1850 | 243 |
| step2_hard_filters | performance_floor | 354 | 17 |
| step3_financial_quality | profitability | 1935 | 166 |
| step3_financial_quality | leverage | 33 | 8 |
| step3_financial_quality | cash_flow_quality | 98 | 3 |
| step3_financial_quality | growth | 70 | 8 |
| step4_valuation | missing_valuation_data | 5 | 2 |
| step4_valuation | pe_valuation_percentile | 97 | 19 |
| step4_valuation | pb_valuation_percentile | 71 | 2 |
| step4_valuation | dividend_yield | 9 | 0 |
| step5_futu_executor | spread_too_wide | 40 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.36 | 0.2069 | 1.027 | 0.2586 | 0.03439 | 0.1779 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.72 | 0.2414 | 1.545 | 0.4828 | 0.02561 | 0.2143 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.93 | 0.2829 | 2.298 | 0.4367 | 0.05821 | 0.1187 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.16 | 0.2499 | 2.007 | 0.3543 | 0.07065 | 0.2132 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 17.33 | 0.3 | 3.167 | 0.4 | 0.01703 | 0.091 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 12.21 | 0.2625 | 1.801 | 0.2866 | 0.02437 | 0.1317 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.6 | 0.2586 | 1.375 | 0.431 | 0.03755 | 0.2379 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.21 | 0.273 | 2.555 | 0.4955 | 0.02609 | 0.09803 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 17.09 | 0.3223 | 2.391 | 0.4583 | 0.04053 | 0.1015 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 15.02 | 0.2945 | 1.953 | 0.3344 | 0.02778 | 0.06566 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 10.38 | 0.1667 | 1.979 | 0.3333 | 0.0331 | 0.1172 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 16.57 | 0.315 | 2.331 | 0.4436 | 0.009532 | 0.05438 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.01 | 0.2493 | 2.49 | 0.4798 | 0.04338 | 0.1461 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 19.71 | 0.3648 | 2.511 | 0.4845 | 0.01974 | 0.05129 |
| 002275 | 桂林三金 | CN | C 制造业 | 0.1389 | 18.11 | 0.3407 | 2.369 | 0.4504 | 0.02244 | 0.08994 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 17.62 | 0.3323 | 2.385 | 0.4562 | 0.02012 | 0.06068 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 13.77 | 0.2824 | 1.807 | 0.2882 | 0.01326 | 0.06685 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 15.93 | 0.3066 | 2.311 | 0.4394 | 0.03077 | 0.09007 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.63 | 0.264 | 2.282 | 0.4346 | 0.05394 | 0.08001 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 21.61 | 0.403 | 2.126 | 0.4328 | 0.009588 | 0.09099 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.26 | 0.4435 | 1.981 | 0.1715 | 0.007937 | 0.07373 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 20.57 | 0.3774 | 2.144 | 0.3979 | 0.014 | 0.04188 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.54 | 0.2451 | 1.403 | 0.147 | 0.02034 | 0.08502 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 15.23 | 0.2987 | 1.995 | 0.3501 | 0.01626 | 0.06893 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.11 | 0.2415 | 2.205 | 0.4147 | 0.02579 | 0.1536 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.24 | 0.2514 | 2.034 | 0.3622 | 0.03303 | 0.1199 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 8.5 | 0.2352 | 2.184 | 0.4063 | 0.00878 | 0.08283 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 11.35 | 0.252 | 1.66 | 0.2346 | 0.01274 | 0.05697 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 15.85 | 0.305 | 1.555 | 0.1963 | 0.01989 | 0.0602 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 16.19 | 0.3963 | 1.931 | 0.4394 | 0.05596 | 0.08115 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 17.2 | 0.4142 | 1.612 | 0.3445 | 0.02544 | 0.09504 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.62 | 0.2894 | 1.451 | 0.2945 | 0.02239 | 0.08471 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 12.95 | 0.3303 | 1.373 | 0.2615 | 0.03914 | 0.1136 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.09 | 0.3335 | 1.469 | 0.2995 | 0.06203 | 0.1585 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 10.09 | 0.2803 | 1.068 | 0.1463 | 0.03224 | 0.1718 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.27 | 0.2991 | 1.393 | 0.2711 | 0.02672 | 0.1478 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 11.27 | 0.2995 | 1.645 | 0.3523 | 0.01689 | 0.1518 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 16.52 | 0.4009 | 1.982 | 0.4495 | 0.0245 | 0.07874 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 9.661 | 0.2725 | 0.973 | 0.1174 | 0.03331 | 0.09964 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.09 | 0.2794 | 1.149 | 0.1766 | 0.03664 | 0.1635 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 11.93 | 0.3151 | 1.585 | 0.3367 | 0.01977 | 0.09676 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.49 | 0.3995 | 2.041 | 0.4628 | 0.01694 | 0.06115 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.24 | 0.2986 | 1.969 | 0.4463 | 0.03102 | 0.1068 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 17.23 | 0.4161 | 2.01 | 0.4541 | 0.03908 | 0.07285 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.44 | 0.2853 | 1.702 | 0.3702 | 0.05941 | 0.147 |
| 605183 | 确成股份 | CN | SW_UNKNOWN | 0.1407 | 11.57 | 0.3046 | 1.535 | 0.3183 | 0.02712 | 0.09807 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.079 | 2.081 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.402 | 2.405 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 5.136 | 5.15 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.181 | 4.193 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.774 | 3.786 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 8.957 | 8.991 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.115 | 1.12 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.187 | 1.193 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 7.837 | 7.876 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.128 | 2.139 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.005 | 1.011 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.096 | 2.109 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002275 | SKIP | spread_too_wide | 0.997 | 1.003 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.198 | 1.207 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.443 | 3.468 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.042 | 1.051 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.541 | 1.555 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 1.628 | 1.647 | 118 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.929 | 1.953 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 7.724 | 7.825 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.747 | 1.77 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 5.909 | 5.991 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.809 | 2.849 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 2.953 | 2.996 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.36 | 1.38 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 136.6 | 138.8 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 94.57 | 96.08 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.502 | 1.526 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.041 | 1.058 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.258 | 1.279 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.991 | 3.044 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.825 | 1.858 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 1.869 | 1.904 | 186 | normal | True | 0 | 0 | OK |  | True |
| 605183 | SKIP | spread_too_wide | 0.991 | 1.01 | 190 | normal | True | 0 | 0 | OK |  | True |
