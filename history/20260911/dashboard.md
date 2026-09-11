# DailyStock Funnel Dashboard

- As of: `2026-09-11`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6136 | - | 196.687 |
| step2_hard_filters | 6136 | 2463 | risk_screen: 648, listing_age: 271, liquidity: 776, market_cap: 1583, performance_floor: 395 | 0.603 |
| step3_financial_quality | 2463 | 226 | profitability: 2040, leverage: 33, cash_flow_quality: 94, growth: 70 | 0.060 |
| step4_valuation | 226 | 47 | missing_valuation_data: 2, pe_valuation_percentile: 90, pb_valuation_percentile: 71, dividend_yield: 16 | 0.228 |
| step5_futu_executor | 47 | 47 | spread_too_wide: 41 | 0.007 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5122 | 0 | 1014 | 0 |
| step2_hard_filters | 2463 | 2659 | 0 | 1014 |
| step3_financial_quality | 226 | 2237 | 0 | 0 |
| step4_valuation | 47 | 179 | 0 | 0 |
| step5_futu_executor | 47 | 41 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 647 |
| step2_hard_filters | listing_age | 226 | 45 |
| step2_hard_filters | liquidity | 454 | 322 |
| step2_hard_filters | market_cap | 1583 | 0 |
| step2_hard_filters | performance_floor | 395 | 0 |
| step3_financial_quality | profitability | 2040 | 0 |
| step3_financial_quality | leverage | 33 | 0 |
| step3_financial_quality | cash_flow_quality | 94 | 0 |
| step3_financial_quality | growth | 70 | 0 |
| step4_valuation | missing_valuation_data | 2 | 0 |
| step4_valuation | pe_valuation_percentile | 90 | 0 |
| step4_valuation | pb_valuation_percentile | 71 | 0 |
| step4_valuation | dividend_yield | 16 | 0 |
| step5_futu_executor | spread_too_wide | 41 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.53 | 0.2069 | 1.054 | 0.2241 | 0.03439 | 0.1752 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 18.47 | 0.3405 | 1.838 | 0.2522 | 0.009083 | 0.08771 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.77 | 0.2414 | 1.591 | 0.5 | 0.02561 | 0.2135 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.5 | 0.2759 | 2.562 | 0.4572 | 0.05821 | 0.1225 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.84 | 0.2454 | 2.215 | 0.3783 | 0.07065 | 0.2195 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.6 | 0.2512 | 1.741 | 0.2218 | 0.01737 | 0.1387 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.2 | 0.2586 | 1.379 | 0.4138 | 0.03755 | 0.2457 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.28 | 0.258 | 1.622 | 0.1881 | 0.02778 | 0.08031 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.27 | 0.1667 | 1.614 | 0.2667 | 0.0331 | 0.108 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 19.49 | 0.3537 | 2.73 | 0.4976 | 0.009532 | 0.04622 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.42 | 0.3689 | 2.588 | 0.463 | 0.01974 | 0.04965 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.21 | 0.3058 | 2.17 | 0.3615 | 0.01189 | 0.06595 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 13.58 | 0.2769 | 1.771 | 0.2302 | 0.01051 | 0.06776 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 26.82 | 0.4748 | 2.848 | 0.3866 | 0.03173 | 0.0623 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 22.89 | 0.4088 | 1.793 | 0.2391 | 0.01238 | 0.05144 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 17.57 | 0.3263 | 2.593 | 0.464 | 0.01586 | 0.08164 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.35 | 0.2596 | 2.47 | 0.4362 | 0.05394 | 0.08185 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 22.3 | 0.3582 | 2.211 | 0.3582 | 0.00885 | 0.08779 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.82 | 0.4286 | 2.023 | 0.1471 | 0.007937 | 0.07164 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 23.05 | 0.3571 | 3.256 | 0.5 | 0.0111 | 0.07968 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 18.42 | 0.416 | 3.181 | 0.4748 | 0.01185 | 0.09812 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.9 | 0.3925 | 2.281 | 0.3941 | 0.0125 | 0.03933 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.14 | 0.2422 | 1.373 | 0.1104 | 0.02034 | 0.08837 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 14.52 | 0.2853 | 1.92 | 0.2811 | 0.01839 | 0.07231 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 9.801 | 0.2412 | 2.2 | 0.372 | 0.02579 | 0.1585 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 10.92 | 0.2465 | 2.051 | 0.3237 | 0.03303 | 0.1234 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 8.909 | 0.238 | 2.289 | 0.3967 | 0.01425 | 0.07903 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.15 | 0.3482 | 2.14 | 0.4543 | 0.03634 | 0.1313 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.82 | 0.3441 | 1.528 | 0.2839 | 0.01984 | 0.1065 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.96 | 0.3275 | 1.571 | 0.3004 | 0.04631 | 0.1601 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.02 | 0.3638 | 2.198 | 0.4681 | 0.04277 | 0.06665 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 11.93 | 0.3073 | 1.501 | 0.2738 | 0.02557 | 0.1294 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 10.82 | 0.2894 | 1.367 | 0.2292 | 0.02672 | 0.154 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.2 | 0.3339 | 1.883 | 0.3826 | 0.02408 | 0.1297 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 16.39 | 0.3941 | 2.148 | 0.4571 | 0.02841 | 0.06294 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 17.86 | 0.4175 | 2.285 | 0.4915 | 0.02063 | 0.07284 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 11.74 | 0.3032 | 1.308 | 0.2049 | 0.01471 | 0.08988 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 14.31 | 0.3514 | 1.543 | 0.2921 | 0.009791 | 0.09787 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 9.205 | 0.2669 | 0.942 | 0.09554 | 0.01454 | 0.1046 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.37 | 0.2788 | 1.225 | 0.1791 | 0.0464 | 0.1589 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 12.74 | 0.3229 | 1.686 | 0.3303 | 0.01977 | 0.09066 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 14.41 | 0.3546 | 1.921 | 0.3955 | 0.01039 | 0.06542 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.16 | 0.3891 | 2.001 | 0.4143 | 0.01694 | 0.06239 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 10.5 | 0.2816 | 1.93 | 0.3987 | 0.03102 | 0.1143 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.65 | 0.3983 | 2.051 | 0.4249 | 0.03908 | 0.0754 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.44 | 0.2793 | 2.045 | 0.4235 | 0.05941 | 0.1305 |
| 688566 | 吉贝尔 | CN | SW_UNKNOWN | 0.1116 | 19.54 | 0.4437 | 2.047 | 0.424 | 0.01016 | 0.04823 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.112 | 2.114 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.101 | 3.105 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.411 | 2.416 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 3.97 | 3.982 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.654 | 3.666 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 0.998 | 1.002 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.511 | 8.547 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.504 | 2.516 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.166 | 2.177 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.103 | 1.109 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.399 | 3.419 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.776 | 4.806 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.694 | 1.705 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.08 | 1.088 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.587 | 1.6 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.463 | 7.528 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.027 | 1.036 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.68 | 2.712 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.309 | 6.386 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.782 | 2.818 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.846 | 6.935 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.993 | 1.007 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.306 | 1.324 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 160 | 162.3 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.993 | 1.007 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 102.3 | 103.8 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 6.126 | 6.221 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 1.796 | 1.824 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.431 | 1.454 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.071 | 1.088 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.342 | 1.365 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.991 | 1.009 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.793 | 2.844 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.763 | 1.796 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.106 | 2.147 | 190 | normal | True | 0 | 0 | OK |  | True |
| 688566 | SKIP | spread_too_wide | 0.99 | 1.01 | 194 | normal | True | 0 | 0 | OK |  | True |
