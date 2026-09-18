# DailyStock Funnel Dashboard

- As of: `2026-09-18`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6126 | - | 214.388 |
| step2_hard_filters | 6126 | 2469 | risk_screen: 641, listing_age: 269, liquidity: 981, market_cap: 1361, performance_floor: 405 | 0.741 |
| step3_financial_quality | 2469 | 230 | profitability: 2041, leverage: 32, cash_flow_quality: 94, growth: 72 | 0.066 |
| step4_valuation | 230 | 48 | missing_valuation_data: 2, pe_valuation_percentile: 101, pb_valuation_percentile: 62, dividend_yield: 17 | 0.266 |
| step5_futu_executor | 48 | 48 | spread_too_wide: 42 | 0.009 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5122 | 0 | 1004 | 0 |
| step2_hard_filters | 2469 | 2653 | 0 | 1004 |
| step3_financial_quality | 230 | 2239 | 0 | 0 |
| step4_valuation | 48 | 182 | 0 | 0 |
| step5_futu_executor | 48 | 42 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 640 |
| step2_hard_filters | listing_age | 223 | 46 |
| step2_hard_filters | liquidity | 663 | 318 |
| step2_hard_filters | market_cap | 1361 | 0 |
| step2_hard_filters | performance_floor | 405 | 0 |
| step3_financial_quality | profitability | 2041 | 0 |
| step3_financial_quality | leverage | 32 | 0 |
| step3_financial_quality | cash_flow_quality | 94 | 0 |
| step3_financial_quality | growth | 72 | 0 |
| step4_valuation | missing_valuation_data | 2 | 0 |
| step4_valuation | pe_valuation_percentile | 101 | 0 |
| step4_valuation | pb_valuation_percentile | 62 | 0 |
| step4_valuation | dividend_yield | 17 | 0 |
| step5_futu_executor | spread_too_wide | 42 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.44 | 0.2069 | 1.045 | 0.2414 | 0.03439 | 0.1767 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 18.05 | 0.329 | 1.797 | 0.2296 | 0.009294 | 0.08975 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.58 | 0.2748 | 2.578 | 0.4509 | 0.05821 | 0.1218 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.54 | 0.2428 | 2.153 | 0.3437 | 0.07065 | 0.2258 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.46 | 0.2512 | 1.72 | 0.2133 | 0.01758 | 0.1404 |
| 001216 | 华瓷股份 | CN | C 制造业 | 0.1235 | 24.85 | 0.4225 | 2.546 | 0.4435 | 0.02395 | 0.05463 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.07 | 0.2586 | 1.365 | 0.4138 | 0.03755 | 0.2482 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.39 | 0.2627 | 1.636 | 0.1808 | 0.02778 | 0.0796 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.43 | 0.1667 | 1.636 | 0.2667 | 0.0331 | 0.1065 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 18.63 | 0.3384 | 2.61 | 0.4587 | 0.009532 | 0.04835 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.53 | 0.2522 | 2.758 | 0.4892 | 0.01781 | 0.1393 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.47 | 0.3668 | 2.594 | 0.4551 | 0.01974 | 0.04954 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 13.31 | 0.2727 | 1.735 | 0.2154 | 0.01073 | 0.06914 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 26.56 | 0.4706 | 2.821 | 0.3824 | 0.007291 | 0.0629 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 22.9 | 0.402 | 1.795 | 0.2286 | 0.01238 | 0.05141 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 27.26 | 0.4503 | 2.749 | 0.4887 | 0.01458 | 0.07528 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.14 | 0.3311 | 2.677 | 0.4719 | 0.01586 | 0.0791 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 22.53 | 0.3731 | 2.233 | 0.2537 | 0.009588 | 0.08692 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.45 | 0.4328 | 1.986 | 0.1345 | 0.007937 | 0.07299 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 23 | 0.3571 | 3.248 | 0.5 | 0.0111 | 0.07988 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 18.42 | 0.416 | 3.181 | 0.479 | 0.01185 | 0.09812 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.37 | 0.381 | 2.226 | 0.3684 | 0.0125 | 0.0403 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.06 | 0.2417 | 1.362 | 0.1067 | 0.02034 | 0.08909 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 14.88 | 0.2916 | 1.967 | 0.2853 | 0.01795 | 0.07057 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.09 | 0.2422 | 2.265 | 0.3826 | 0.02579 | 0.154 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 10.99 | 0.2459 | 2.065 | 0.3169 | 0.03303 | 0.1226 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 11.1 | 0.2491 | 2.802 | 0.4997 | 0.03286 | 0.07023 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.77 | 0.2444 | 2.766 | 0.4913 | 0.00878 | 0.06539 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 16.71 | 0.3973 | 2.152 | 0.4488 | 0.05596 | 0.07866 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.32 | 0.3505 | 2.166 | 0.4534 | 0.03634 | 0.1297 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.88 | 0.3441 | 1.535 | 0.2807 | 0.01975 | 0.106 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.87 | 0.328 | 1.56 | 0.2885 | 0.04663 | 0.1612 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 14.89 | 0.3624 | 2.178 | 0.4561 | 0.04277 | 0.06725 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 12.16 | 0.3124 | 1.53 | 0.2779 | 0.02557 | 0.127 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.89 | 0.3073 | 1.502 | 0.2678 | 0.02672 | 0.1401 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 12.57 | 0.3215 | 1.793 | 0.3555 | 0.02528 | 0.1362 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 16.79 | 0.3983 | 2.201 | 0.4612 | 0.02841 | 0.06145 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 17.38 | 0.4116 | 2.224 | 0.4667 | 0.0212 | 0.07486 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 11.91 | 0.3078 | 1.327 | 0.2118 | 0.0145 | 0.08858 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 10.95 | 0.2921 | 1.12 | 0.1488 | 0.01223 | 0.08795 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.26 | 0.2784 | 1.212 | 0.1764 | 0.0464 | 0.1606 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 12.41 | 0.3165 | 1.644 | 0.3179 | 0.01977 | 0.09301 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 14.29 | 0.35 | 1.904 | 0.3877 | 0.01039 | 0.06601 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.28 | 0.39 | 2.016 | 0.4143 | 0.01694 | 0.06194 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 10.23 | 0.2779 | 1.88 | 0.3799 | 0.03102 | 0.1174 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 17.2 | 0.4088 | 2.119 | 0.4378 | 0.03908 | 0.07299 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.23 | 0.2774 | 2.003 | 0.4102 | 0.05941 | 0.1332 |
| 688566 | 吉贝尔 | CN | SW_UNKNOWN | 0.1116 | 20 | 0.4497 | 2.095 | 0.4322 | 0.009924 | 0.04713 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.094 | 2.096 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.031 | 3.035 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 3.922 | 3.933 | 26 | normal | True | 0 | 0 | OK |  | True |
| 001216 | WATCH | passed_depth_scan | 0.999 | 1.002 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.616 | 3.629 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 0.998 | 1.002 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.63 | 8.666 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.394 | 2.405 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.055 | 1.06 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.171 | 2.183 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.331 | 3.351 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.731 | 4.76 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.695 | 1.706 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.091 | 1.099 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.557 | 1.57 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.445 | 7.509 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.002 | 1.011 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.057 | 1.069 | 114 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.199 | 1.214 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.99 | 2.015 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.711 | 2.746 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.336 | 6.419 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.762 | 2.799 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.782 | 6.876 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.993 | 1.007 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.435 | 1.456 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 152.4 | 154.7 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.992 | 1.008 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 99.48 | 101.1 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 6.213 | 6.315 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.701 | 1.729 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.059 | 1.077 | 170 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.308 | 1.331 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.991 | 1.009 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.719 | 2.77 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.821 | 1.856 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.063 | 2.103 | 194 | normal | True | 0 | 0 | OK |  | True |
| 688566 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
