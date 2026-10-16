# DailyStock Funnel Dashboard

- As of: `2026-10-16`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7940 | - | 327.702 |
| step2_hard_filters | 7940 | 2512 | risk_screen: 1497, listing_age: 438, liquidity: 1125, market_cap: 1988, performance_floor: 380 | 0.507 |
| step3_financial_quality | 2512 | 245 | profitability: 2052, leverage: 36, cash_flow_quality: 101, growth: 78 | 0.060 |
| step4_valuation | 245 | 45 | missing_valuation_data: 4, pe_valuation_percentile: 99, pb_valuation_percentile: 80, dividend_yield: 17 | 0.234 |
| step5_futu_executor | 45 | 45 | spread_too_wide: 39 | 0.006 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5121 | 0 | 2819 | 0 |
| step2_hard_filters | 2418 | 2703 | 94 | 2725 |
| step3_financial_quality | 231 | 2187 | 14 | 80 |
| step4_valuation | 45 | 186 | 0 | 14 |
| step5_futu_executor | 45 | 39 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 2 | 1495 |
| step2_hard_filters | listing_age | 135 | 303 |
| step2_hard_filters | liquidity | 507 | 618 |
| step2_hard_filters | market_cap | 1685 | 303 |
| step2_hard_filters | performance_floor | 374 | 6 |
| step3_financial_quality | profitability | 1985 | 67 |
| step3_financial_quality | leverage | 34 | 2 |
| step3_financial_quality | cash_flow_quality | 97 | 4 |
| step3_financial_quality | growth | 71 | 7 |
| step4_valuation | missing_valuation_data | 2 | 2 |
| step4_valuation | pe_valuation_percentile | 89 | 10 |
| step4_valuation | pb_valuation_percentile | 78 | 2 |
| step4_valuation | dividend_yield | 17 | 0 |
| step5_futu_executor | spread_too_wide | 39 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.53 | 0.2 | 1.054 | 0.25 | 0.03439 | 0.1752 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 19.28 | 0.3663 | 1.919 | 0.3064 | 0.01675 | 0.08405 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 10.74 | 0.2167 | 1.452 | 0.4833 | 0.02561 | 0.2339 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.71 | 0.2507 | 2.187 | 0.3957 | 0.07065 | 0.2223 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 12.41 | 0.268 | 1.864 | 0.2827 | 0.01601 | 0.1296 |
| 001216 | 华瓷股份 | CN | C 制造业 | 0.1235 | 25.11 | 0.4551 | 2.573 | 0.4924 | 0.02395 | 0.05406 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.76 | 0.2667 | 1.442 | 0.4667 | 0.03755 | 0.2348 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.26 | 0.2659 | 1.619 | 0.2065 | 0.02778 | 0.08045 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.39 | 0.1724 | 1.631 | 0.2759 | 0.0331 | 0.1068 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 15.56 | 0.3074 | 2.181 | 0.3946 | 0.009532 | 0.05787 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.4 | 0.3847 | 2.586 | 0.4961 | 0.01974 | 0.0497 |
| 002275 | 桂林三金 | CN | C 制造业 | 0.1389 | 16.53 | 0.319 | 2.201 | 0.3978 | 0.02244 | 0.09854 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.06 | 0.3137 | 2.15 | 0.3873 | 0.01153 | 0.06657 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 12.62 | 0.2727 | 1.645 | 0.2144 | 0.01326 | 0.07292 |
| 002545 | 东方铁塔 | CN | C 制造业 | 0.1297 | 13.28 | 0.2806 | 1.546 | 0.1802 | 0.01913 | 0.149 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 22.29 | 0.4515 | 2.367 | 0.2658 | 0.03227 | 0.07497 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 20.43 | 0.3857 | 1.601 | 0.1997 | 0.01238 | 0.05764 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 23.14 | 0.4272 | 2.334 | 0.4293 | 0.01458 | 0.08867 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.13 | 0.2654 | 2.426 | 0.4488 | 0.05394 | 0.08333 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 21.24 | 0.3636 | 2.106 | 0.2879 | 0.008721 | 0.0922 |
| 002970 | 锐明技术 | CN | I 信息技术 | 0.2029 | 17.32 | 0.4219 | 3.118 | 0.481 | 0.008247 | 0.05796 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 18.86 | 0.4388 | 1.926 | 0.1308 | 0.007937 | 0.07526 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 17.96 | 0.4262 | 3.102 | 0.4768 | 0.01185 | 0.1006 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.1 | 0.3957 | 2.197 | 0.3962 | 0.0125 | 0.04083 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 9.782 | 0.2438 | 1.324 | 0.1125 | 0.02034 | 0.09165 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 14.19 | 0.2922 | 1.876 | 0.2848 | 0.01799 | 0.07399 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 9.184 | 0.2391 | 2.061 | 0.3605 | 0.02579 | 0.1691 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.25 | 0.2564 | 2.114 | 0.3773 | 0.03303 | 0.1198 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 9.239 | 0.2396 | 2.385 | 0.4388 | 0.01133 | 0.07584 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 15.07 | 0.3707 | 1.666 | 0.3339 | 0.0182 | 0.09769 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.38 | 0.3385 | 1.622 | 0.3211 | 0.04355 | 0.155 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 11.4 | 0.3 | 1.434 | 0.2591 | 0.02557 | 0.1355 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.13 | 0.2949 | 1.405 | 0.2499 | 0.02672 | 0.1497 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.52 | 0.3441 | 1.929 | 0.4153 | 0.02338 | 0.1266 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 11.79 | 0.3068 | 1.914 | 0.4116 | 0.01703 | 0.1403 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 12.2 | 0.3147 | 1.359 | 0.2347 | 0.01416 | 0.08652 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 11.24 | 0.2977 | 1.327 | 0.2219 | 0.0464 | 0.1467 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.07 | 0.3316 | 1.731 | 0.3569 | 0.01977 | 0.08831 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 14.08 | 0.3546 | 1.87 | 0.3973 | 0.01039 | 0.06719 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 14.88 | 0.3679 | 1.843 | 0.3904 | 0.01694 | 0.06774 |
| 603202 | 天有为 | CN | SW_UNKNOWN | 0.1623 | 7.75 | 0.2559 | 1.147 | 0.1631 | 0.01016 | 0.1369 |
| 603402 | 陕西旅游 | CN | SW_UNKNOWN | 0.2774 | 8.372 | 0.2582 | 1.894 | 0.4042 | 0.02117 | 0.09488 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 9.809 | 0.2742 | 1.803 | 0.3767 | 0.03102 | 0.1224 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.88 | 0.4084 | 2.08 | 0.4571 | 0.03908 | 0.07437 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.82 | 0.2894 | 2.119 | 0.4676 | 0.05941 | 0.1259 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.112 | 2.114 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.236 | 3.241 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.201 | 2.205 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.25 | 4.261 | 26 | normal | True | 0 | 0 | OK |  | True |
| 001216 | WATCH | passed_depth_scan | 0.999 | 1.002 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.822 | 3.835 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 0.998 | 1.002 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.602 | 8.638 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2 | 2.009 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.164 | 2.175 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002275 | SKIP | spread_too_wide | 0.997 | 1.003 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.093 | 1.099 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.158 | 3.178 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002545 | SKIP | spread_too_wide | 1.597 | 1.608 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 3.968 | 3.996 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.511 | 1.522 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.028 | 1.037 | 86 | normal | True | 0 | 0 | OK |  | True |
| 002970 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.51 | 1.524 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.034 | 1.047 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.878 | 6.965 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.872 | 2.91 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.993 | 1.007 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.343 | 1.362 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 163.9 | 166.3 | 142 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.757 | 1.783 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 6.365 | 6.461 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.16 | 1.178 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.379 | 1.401 | 158 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.992 | 1.008 | 162 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.992 | 1.008 | 166 | normal | True | 0 | 0 | OK |  | True |
| 603202 | SKIP | spread_too_wide | 0.992 | 1.008 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603402 | SKIP | spread_too_wide | 0.991 | 1.009 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.609 | 2.656 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.788 | 1.82 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.183 | 2.224 | 186 | normal | True | 0 | 0 | OK |  | True |
