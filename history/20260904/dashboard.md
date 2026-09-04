# DailyStock Funnel Dashboard

- As of: `2026-09-04`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7926 | - | 375.730 |
| step2_hard_filters | 7926 | 2617 | risk_screen: 1475, listing_age: 524, liquidity: 1048, market_cap: 1859, performance_floor: 403 | 0.571 |
| step3_financial_quality | 2617 | 252 | profitability: 2148, leverage: 36, cash_flow_quality: 103, growth: 78 | 0.063 |
| step4_valuation | 252 | 46 | missing_valuation_data: 4, pe_valuation_percentile: 110, pb_valuation_percentile: 72, dividend_yield: 20 | 0.252 |
| step5_futu_executor | 46 | 46 | spread_too_wide: 40 | 0.006 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5122 | 0 | 2804 | 0 |
| step2_hard_filters | 2505 | 2617 | 112 | 2692 |
| step3_financial_quality | 236 | 2269 | 16 | 96 |
| step4_valuation | 46 | 190 | 0 | 16 |
| step5_futu_executor | 46 | 40 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1474 |
| step2_hard_filters | listing_age | 232 | 292 |
| step2_hard_filters | liquidity | 449 | 599 |
| step2_hard_filters | market_cap | 1539 | 320 |
| step2_hard_filters | performance_floor | 396 | 7 |
| step3_financial_quality | profitability | 2065 | 83 |
| step3_financial_quality | leverage | 33 | 3 |
| step3_financial_quality | cash_flow_quality | 98 | 5 |
| step3_financial_quality | growth | 73 | 5 |
| step4_valuation | missing_valuation_data | 2 | 2 |
| step4_valuation | pe_valuation_percentile | 96 | 14 |
| step4_valuation | pb_valuation_percentile | 72 | 0 |
| step4_valuation | dividend_yield | 20 | 0 |
| step5_futu_executor | spread_too_wide | 40 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.73 | 0.2241 | 1.075 | 0.2414 | 0.03439 | 0.1718 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 18.91 | 0.3358 | 1.882 | 0.2475 | 0.008873 | 0.08569 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.42 | 0.2414 | 1.544 | 0.4828 | 0.02561 | 0.22 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 14.03 | 0.2754 | 2.663 | 0.4619 | 0.05821 | 0.1179 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.14 | 0.2449 | 2.275 | 0.3736 | 0.07065 | 0.2137 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 12.09 | 0.2538 | 1.815 | 0.2286 | 0.01667 | 0.133 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 11.97 | 0.2586 | 1.353 | 0.4138 | 0.03755 | 0.2503 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 13.78 | 0.2722 | 1.82 | 0.2307 | 0.02778 | 0.07157 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 12.09 | 0.1667 | 1.731 | 0.2667 | 0.0331 | 0.1007 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 18.66 | 0.3316 | 2.615 | 0.4524 | 0.009532 | 0.04826 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 21.49 | 0.3757 | 2.723 | 0.4761 | 0.01974 | 0.04719 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14.54 | 0.2796 | 1.895 | 0.2517 | 0.00982 | 0.0633 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 29.44 | 0.4916 | 3.126 | 0.416 | 0.02891 | 0.05676 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 24.21 | 0.4136 | 1.897 | 0.2522 | 0.01238 | 0.04862 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 27.23 | 0.4446 | 2.746 | 0.4824 | 0.01458 | 0.07536 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.56 | 0.3311 | 2.74 | 0.4819 | 0.03077 | 0.07729 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.53 | 0.2601 | 2.506 | 0.4283 | 0.05394 | 0.08066 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 23.25 | 0.3731 | 2.305 | 0.3881 | 0.008489 | 0.08422 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 24 | 0.3571 | 3.389 | 0.5 | 0.0111 | 0.07655 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 19.71 | 0.4202 | 3.404 | 0.4958 | 0.01185 | 0.09169 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 24.36 | 0.4162 | 2.537 | 0.4325 | 0.0125 | 0.03536 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.42 | 0.2428 | 1.41 | 0.114 | 0.02034 | 0.08606 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 14.93 | 0.2838 | 1.974 | 0.2801 | 0.01789 | 0.07034 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.31 | 0.2417 | 2.314 | 0.3836 | 0.02579 | 0.1507 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.52 | 0.248 | 2.164 | 0.3416 | 0.03303 | 0.1169 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 9.645 | 0.2396 | 2.478 | 0.4251 | 0.01316 | 0.073 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 15.92 | 0.3753 | 2.052 | 0.4166 | 0.05596 | 0.08252 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.81 | 0.3555 | 2.239 | 0.4621 | 0.03634 | 0.1255 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.62 | 0.3349 | 1.506 | 0.2618 | 0.02013 | 0.1081 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.11 | 0.3261 | 1.59 | 0.2935 | 0.04576 | 0.1582 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.31 | 0.3629 | 2.24 | 0.4635 | 0.04277 | 0.06538 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 12.45 | 0.3128 | 1.567 | 0.2834 | 0.02557 | 0.124 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.41 | 0.2954 | 1.441 | 0.2407 | 0.02672 | 0.1461 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13 | 0.3225 | 1.855 | 0.362 | 0.02444 | 0.1316 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.08 | 0.3978 | 2.239 | 0.4621 | 0.02841 | 0.06041 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 17.9 | 0.4111 | 2.29 | 0.4796 | 0.02058 | 0.07269 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 11.37 | 0.2931 | 1.267 | 0.1856 | 0.01519 | 0.09281 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 14.88 | 0.3574 | 1.604 | 0.2981 | 0.009791 | 0.09415 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 9.047 | 0.2637 | 0.926 | 0.08498 | 0.0148 | 0.1064 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.55 | 0.2788 | 1.246 | 0.1791 | 0.0464 | 0.1562 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.26 | 0.328 | 1.755 | 0.3399 | 0.01977 | 0.08711 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 15.01 | 0.3592 | 2 | 0.4056 | 0.01039 | 0.06283 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.78 | 0.3914 | 2.078 | 0.4194 | 0.01694 | 0.06009 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.02 | 0.2871 | 2.024 | 0.4107 | 0.03102 | 0.109 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 17.64 | 0.407 | 2.173 | 0.4446 | 0.03908 | 0.07119 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.79 | 0.282 | 2.114 | 0.4272 | 0.05941 | 0.1262 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.153 | 2.156 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.174 | 3.179 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.34 | 2.344 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.138 | 4.15 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.586 | 3.599 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.09 | 1.094 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 9.126 | 9.164 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.398 | 2.409 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.28 | 2.291 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.639 | 3.659 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 5.244 | 5.274 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.792 | 1.804 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.003 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.126 | 1.135 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.77 | 7.834 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.142 | 1.152 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.075 | 1.087 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.898 | 1.92 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.804 | 2.838 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.219 | 6.295 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.816 | 2.851 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.979 | 7.07 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.993 | 1.007 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.377 | 1.396 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 157.7 | 159.9 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.993 | 1.007 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 102.5 | 104 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 5.932 | 6.024 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 1.867 | 1.896 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.406 | 1.429 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.089 | 1.107 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.397 | 1.421 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.991 | 1.009 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.929 | 2.983 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.867 | 1.902 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.177 | 2.219 | 190 | normal | True | 0 | 0 | OK |  | True |
