# DailyStock Funnel Dashboard

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

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 18.37 | 0.3177 | 2.959 | 0.4778 | 0.02899 | 0.07167 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.21 | 0.1379 | 1.012 | 0.08621 | 0.03424 | 0.1805 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 14.55 | 0.2586 | 1.919 | 0.5 | 0.02561 | 0.1726 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.22 | 0.2616 | 2.18 | 0.3034 | 0.05821 | 0.1251 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.96 | 0.2511 | 2.151 | 0.2976 | 0.07331 | 0.1989 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 20.4 | 0.3103 | 3.729 | 0.4483 | 0.01703 | 0.07729 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.75 | 0.2479 | 1.733 | 0.1786 | 0.02437 | 0.1368 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 15.43 | 0.3103 | 1.683 | 0.431 | 0.03323 | 0.1943 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 14.36 | 0.2743 | 2.777 | 0.4456 | 0.02609 | 0.09018 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 16.53 | 0.2933 | 2.312 | 0.334 | 0.04053 | 0.105 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 13.78 | 0.268 | 1.792 | 0.194 | 0.02648 | 0.07157 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.99 | 0.1724 | 2.159 | 0.3103 | 0.0331 | 0.1074 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 12.23 | 0.2521 | 2.766 | 0.4445 | 0.04338 | 0.1316 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 18.4 | 0.3187 | 2.343 | 0.3494 | 0.01974 | 0.05495 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 15.07 | 0.2822 | 1.978 | 0.2542 | 0.01263 | 0.06106 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 29.97 | 0.444 | 2.942 | 0.4752 | 0.01458 | 0.06847 |
| 002831 | 裕同科技 | CN | C 制造业 | 0.1356 | 15.36 | 0.2844 | 2.808 | 0.4498 | 0.01961 | 0.07904 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.33 | 0.3161 | 2.628 | 0.4154 | 0.03077 | 0.07919 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 25.05 | 0.4375 | 2.466 | 0.4375 | 0.009588 | 0.07844 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 18.16 | 0.3129 | 2.814 | 0.4503 | 0.03041 | 0.06467 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 19.17 | 0.4316 | 3.201 | 0.4017 | 0.01087 | 0.09428 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 12.32 | 0.2532 | 1.639 | 0.1591 | 0.02034 | 0.07278 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 16.64 | 0.2949 | 2.18 | 0.3034 | 0.01605 | 0.06311 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.913 | 0.3803 | 3.517 | 0.4701 | 0.03779 | 0.1262 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.76 | 0.2484 | 2.128 | 0.2902 | 0.03303 | 0.1146 |
| 301004 | 嘉益股份 | CN | C 制造业 | 0.2303 | 12.6 | 0.2569 | 3.089 | 0.4979 | 0.01747 | 0.1463 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.51 | 0.241 | 2.7 | 0.4286 | 0.00878 | 0.06701 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 15.01 | 0.2817 | 2.195 | 0.3076 | 0.01274 | 0.04307 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 20.09 | 0.3367 | 1.972 | 0.2511 | 0.01989 | 0.04747 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 17.88 | 0.399 | 2.132 | 0.4161 | 0.05028 | 0.07348 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.24 | 0.3411 | 2.031 | 0.3943 | 0.04156 | 0.1305 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 21.29 | 0.4509 | 1.996 | 0.3832 | 0.0216 | 0.07678 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.58 | 0.278 | 1.446 | 0.2335 | 0.02247 | 0.08501 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.9 | 0.3369 | 1.474 | 0.24 | 0.03864 | 0.1059 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.82 | 0.317 | 1.439 | 0.2312 | 0.06203 | 0.1618 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 10.93 | 0.2836 | 1.156 | 0.1427 | 0.03048 | 0.1587 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 17.75 | 0.3967 | 2.51 | 0.4926 | 0.03936 | 0.05639 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 12.18 | 0.2994 | 1.27 | 0.1807 | 0.0251 | 0.1268 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.04 | 0.3221 | 1.612 | 0.291 | 0.02599 | 0.1277 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.69 | 0.3327 | 1.997 | 0.3837 | 0.01412 | 0.125 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.78 | 0.3976 | 2.253 | 0.4439 | 0.02917 | 0.05804 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 9.595 | 0.2678 | 1.488 | 0.247 | 0.05499 | 0.1724 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.24 | 0.4055 | 2.188 | 0.4277 | 0.02123 | 0.07132 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 17.04 | 0.3842 | 1.843 | 0.3485 | 0.02021 | 0.08218 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 10.24 | 0.272 | 1.032 | 0.1075 | 0.01328 | 0.09397 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.992 | 0.2697 | 1.138 | 0.1372 | 0.0475 | 0.165 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 14.53 | 0.3466 | 1.93 | 0.367 | 0.01558 | 0.07945 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 17.76 | 0.3971 | 2.199 | 0.4291 | 0.01694 | 0.05675 |
| 603202 | 天有为 | CN | SW_UNKNOWN | 0.1623 | 10.26 | 0.2729 | 1.503 | 0.2535 | 0.02323 | 0.1033 |
| 603391 | 力聚热能 | CN | SW_UNKNOWN | 0.1037 | 22.59 | 0.4671 | 2.247 | 0.443 | 0.02329 | 0.06787 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.44 | 0.2887 | 2.008 | 0.3855 | 0.03102 | 0.1047 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.63 | 0.3786 | 1.94 | 0.3689 | 0.03908 | 0.0755 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 12.58 | 0.3091 | 2.051 | 0.3985 | 0.04987 | 0.1221 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 3.193 | 3.196 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.049 | 2.051 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.982 | 2.987 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 6.046 | 6.064 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 4.022 | 4.036 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 4.619 | 4.636 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.735 | 9.776 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.078 | 1.083 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.089 | 1.095 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.548 | 8.594 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.117 | 1.123 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 1.956 | 1.969 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.77 | 3.795 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002831 | SKIP | spread_too_wide | 3.45 | 3.476 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.208 | 1.218 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.329 | 1.341 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 301004 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.171 | 1.184 | 114 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.153 | 2.179 | 118 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 2.13 | 2.157 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.696 | 2.731 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.559 | 9.688 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.74 | 1.764 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.343 | 6.433 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.751 | 2.791 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.195 | 3.244 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 8.082 | 8.207 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.992 | 1.008 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.573 | 1.598 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 165.8 | 168.6 | 166 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 1.026 | 1.043 | 170 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.428 | 1.453 | 174 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 104.3 | 106.2 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.136 | 2.175 | 182 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.59 | 1.62 | 186 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.03 | 1.05 | 190 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.53 | 1.56 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603202 | SKIP | spread_too_wide | 1.023 | 1.043 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603391 | SKIP | spread_too_wide | 0.99 | 1.01 | 206 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.044 | 3.108 | 210 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.758 | 1.796 | 214 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.248 | 2.298 | 218 | normal | True | 0 | 0 | OK |  | True |
