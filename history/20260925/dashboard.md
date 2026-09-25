# DailyStock Funnel Dashboard

- As of: `2026-09-25`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7935 | - | 347.339 |
| step2_hard_filters | 7935 | 2539 | risk_screen: 1488, listing_age: 511, liquidity: 1405, market_cap: 1583, performance_floor: 409 | 0.776 |
| step3_financial_quality | 2539 | 241 | profitability: 2088, leverage: 35, cash_flow_quality: 97, growth: 78 | 0.064 |
| step4_valuation | 241 | 48 | missing_valuation_data: 4, pe_valuation_percentile: 104, pb_valuation_percentile: 65, dividend_yield: 20 | 0.273 |
| step5_futu_executor | 48 | 48 | spread_too_wide: 42 | 0.008 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5122 | 0 | 2813 | 0 |
| step2_hard_filters | 2460 | 2662 | 79 | 2734 |
| step3_financial_quality | 228 | 2232 | 13 | 66 |
| step4_valuation | 48 | 180 | 0 | 13 |
| step5_futu_executor | 48 | 42 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1487 |
| step2_hard_filters | listing_age | 218 | 293 |
| step2_hard_filters | liquidity | 694 | 711 |
| step2_hard_filters | market_cap | 1346 | 237 |
| step2_hard_filters | performance_floor | 403 | 6 |
| step3_financial_quality | profitability | 2033 | 55 |
| step3_financial_quality | leverage | 32 | 3 |
| step3_financial_quality | cash_flow_quality | 95 | 2 |
| step3_financial_quality | growth | 72 | 6 |
| step4_valuation | missing_valuation_data | 2 | 2 |
| step4_valuation | pe_valuation_percentile | 94 | 10 |
| step4_valuation | pb_valuation_percentile | 64 | 1 |
| step4_valuation | dividend_yield | 20 | 0 |
| step5_futu_executor | spread_too_wide | 42 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.48 | 0.2069 | 1.049 | 0.2414 | 0.03439 | 0.1759 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 18.09 | 0.3284 | 1.8 | 0.2302 | 0.009276 | 0.08958 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.15 | 0.2414 | 1.508 | 0.5 | 0.02561 | 0.2253 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.43 | 0.2743 | 2.549 | 0.4383 | 0.05821 | 0.1231 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.51 | 0.2433 | 2.147 | 0.3374 | 0.07065 | 0.2264 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.35 | 0.2528 | 1.705 | 0.2065 | 0.01774 | 0.1416 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 11.79 | 0.2586 | 1.332 | 0.4138 | 0.03755 | 0.2542 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.23 | 0.2617 | 1.614 | 0.175 | 0.02778 | 0.08066 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.5 | 0.1667 | 1.646 | 0.2667 | 0.0331 | 0.1059 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 17.49 | 0.3205 | 2.45 | 0.4193 | 0.009532 | 0.0515 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.34 | 0.2522 | 2.713 | 0.4687 | 0.01781 | 0.1417 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.15 | 0.3594 | 2.554 | 0.4388 | 0.01974 | 0.05031 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.25 | 0.3058 | 2.175 | 0.3458 | 0.01153 | 0.06581 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 12.98 | 0.2701 | 1.692 | 0.2028 | 0.011 | 0.07089 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 25.13 | 0.4622 | 2.668 | 0.3193 | 0.03227 | 0.0665 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 23.67 | 0.4115 | 1.855 | 0.2433 | 0.01238 | 0.04973 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 27.4 | 0.4519 | 2.763 | 0.4845 | 0.01458 | 0.07489 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.14 | 0.329 | 2.677 | 0.4614 | 0.01586 | 0.0791 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 23.83 | 0.3881 | 2.363 | 0.3284 | 0.008721 | 0.08217 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.52 | 0.4328 | 1.993 | 0.1387 | 0.007937 | 0.07272 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 22.63 | 0.3571 | 3.195 | 0.5 | 0.0111 | 0.0812 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 18.12 | 0.416 | 3.131 | 0.458 | 0.01185 | 0.0997 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.57 | 0.3778 | 2.246 | 0.3689 | 0.0125 | 0.03994 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.11 | 0.2422 | 1.368 | 0.1067 | 0.02034 | 0.08869 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 9.868 | 0.2417 | 2.215 | 0.3594 | 0.02579 | 0.1574 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.21 | 0.2512 | 2.106 | 0.3258 | 0.03303 | 0.1202 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 11.08 | 0.2501 | 2.797 | 0.4908 | 0.03286 | 0.07036 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.67 | 0.2449 | 2.742 | 0.4771 | 0.01133 | 0.06597 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 17.2 | 0.3169 | 1.713 | 0.2097 | 0.01989 | 0.05545 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 13.94 | 0.3468 | 2.108 | 0.4286 | 0.03634 | 0.1333 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 14 | 0.3482 | 1.549 | 0.283 | 0.01958 | 0.1051 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.58 | 0.3211 | 1.525 | 0.2747 | 0.0477 | 0.1649 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 14.84 | 0.3647 | 2.171 | 0.4474 | 0.04277 | 0.06748 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 13.07 | 0.3326 | 1.644 | 0.3124 | 0.02557 | 0.1181 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.59 | 0.3023 | 1.463 | 0.2559 | 0.02672 | 0.1438 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 12.76 | 0.3261 | 1.821 | 0.3592 | 0.02489 | 0.1341 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 16.41 | 0.3927 | 2.15 | 0.4414 | 0.02841 | 0.06289 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.06 | 0.4212 | 2.31 | 0.4814 | 0.0204 | 0.07205 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 12.04 | 0.3096 | 1.341 | 0.2168 | 0.01435 | 0.08767 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 18.06 | 0.4212 | 1.947 | 0.3914 | 0.009791 | 0.07758 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.59 | 0.2848 | 1.25 | 0.186 | 0.0464 | 0.1557 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 12.3 | 0.3156 | 1.629 | 0.3068 | 0.01977 | 0.09386 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 14.72 | 0.362 | 1.962 | 0.3946 | 0.01039 | 0.06405 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.51 | 0.3937 | 2.045 | 0.4143 | 0.01694 | 0.06105 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 10.2 | 0.2779 | 1.874 | 0.3734 | 0.03102 | 0.1177 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 18 | 0.4198 | 2.217 | 0.458 | 0.03908 | 0.06978 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.25 | 0.2784 | 2.008 | 0.4061 | 0.05941 | 0.1329 |
| 605183 | 确成股份 | CN | SW_UNKNOWN | 0.1407 | 13.64 | 0.3422 | 1.849 | 0.3679 | 0.02712 | 0.08316 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.103 | 2.105 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.036 | 3.041 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.285 | 2.289 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 3.887 | 3.898 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.53 | 3.542 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 0.998 | 1.002 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.68 | 8.716 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.247 | 2.258 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.037 | 1.042 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.138 | 2.149 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.106 | 1.112 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.248 | 3.269 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.474 | 4.504 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.752 | 1.764 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.154 | 1.163 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.563 | 1.577 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.323 | 7.389 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.011 | 1.02 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.055 | 1.067 | 114 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.189 | 1.203 | 118 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.638 | 2.672 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.391 | 6.475 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.7 | 2.737 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.759 | 6.853 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.993 | 1.007 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.398 | 1.418 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 154.7 | 157.1 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.992 | 1.008 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 103.4 | 105 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 6.278 | 6.38 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.265 | 2.302 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.092 | 1.111 | 170 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.296 | 1.319 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.991 | 1.009 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.711 | 2.762 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.905 | 1.941 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.067 | 2.108 | 194 | normal | True | 0 | 0 | OK |  | True |
| 605183 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
