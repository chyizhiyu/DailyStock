# DailyStock Funnel Dashboard

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7835 | - | 281.611 |
| step2_hard_filters | 7835 | 2794 | risk_screen: 1452, listing_age: 525, liquidity: 1034, market_cap: 1572, performance_floor: 458 | 0.623 |
| step3_financial_quality | 2794 | 286 | profitability: 2296, leverage: 42, cash_flow_quality: 106, growth: 64 | 0.064 |
| step4_valuation | 286 | 52 | missing_valuation_data: 29, pe_valuation_percentile: 126, pb_valuation_percentile: 67, dividend_yield: 12 | 0.278 |
| step5_futu_executor | 52 | 52 | spread_too_wide: 46 | 0.007 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 2774 | 0 |
| step2_hard_filters | 2580 | 2481 | 214 | 2560 |
| step3_financial_quality | 256 | 2324 | 30 | 184 |
| step4_valuation | 52 | 204 | 0 | 30 |
| step5_futu_executor | 52 | 46 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1451 |
| step2_hard_filters | listing_age | 237 | 288 |
| step2_hard_filters | liquidity | 432 | 602 |
| step2_hard_filters | market_cap | 1371 | 201 |
| step2_hard_filters | performance_floor | 440 | 18 |
| step3_financial_quality | profitability | 2136 | 160 |
| step3_financial_quality | leverage | 34 | 8 |
| step3_financial_quality | cash_flow_quality | 99 | 7 |
| step3_financial_quality | growth | 55 | 9 |
| step4_valuation | missing_valuation_data | 26 | 3 |
| step4_valuation | pe_valuation_percentile | 101 | 25 |
| step4_valuation | pb_valuation_percentile | 65 | 2 |
| step4_valuation | dividend_yield | 12 | 0 |
| step5_futu_executor | spread_too_wide | 46 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000513 | 丽珠集团 | CN | C 制造业 | 0.1467 | 13.37 | 0.2632 | 1.857 | 0.2236 | 0.04712 | 0.1167 |
| 000538 | 云南白药 | CN | C 制造业 | 0.1302 | 16.82 | 0.2986 | 2.06 | 0.278 | 0.02898 | 0.05304 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.29 | 0.1379 | 1.02 | 0.1034 | 0.03399 | 0.1792 |
| 000739 | 普洛药业 | CN | C 制造业 | 0.1322 | 20.78 | 0.3462 | 2.834 | 0.4598 | 0.01265 | 0.06563 |
| 000786 | 北新建材 | CN | C 制造业 | 0.1111 | 12.87 | 0.2585 | 1.347 | 0.09355 | 0.031 | 0.1117 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.18 | 0.2606 | 2.174 | 0.3097 | 0.05821 | 0.1255 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.85 | 0.2516 | 2.131 | 0.297 | 0.07402 | 0.2008 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 20.75 | 0.3103 | 3.792 | 0.4483 | 0.01703 | 0.076 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.62 | 0.2474 | 1.713 | 0.1771 | 0.02437 | 0.1384 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 15.8 | 0.3276 | 1.724 | 0.4138 | 0.03244 | 0.1897 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.88 | 0.268 | 2.684 | 0.4334 | 0.02609 | 0.0933 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 16.76 | 0.297 | 2.345 | 0.351 | 0.04053 | 0.1035 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 12.24 | 0.1724 | 2.204 | 0.3448 | 0.0331 | 0.1052 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 12.17 | 0.2537 | 2.754 | 0.4456 | 0.04338 | 0.1321 |
| 002223 | 鱼跃医疗 | CN | C 制造业 | 0.1142 | 17.53 | 0.3081 | 1.905 | 0.2331 | 0.02165 | 0.0578 |
| 002236 | 大华股份 | CN | C 制造业 | 0.1042 | 14.14 | 0.2701 | 1.42 | 0.1115 | 0.02043 | 0.07162 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 18.5 | 0.3214 | 2.357 | 0.3547 | 0.01974 | 0.05464 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 15.35 | 0.2838 | 2.015 | 0.2674 | 0.0124 | 0.05995 |
| 002555 | 三七互娱 | CN | I 信息技术 | 0.2173 | 14.39 | 0.3932 | 2.9 | 0.3248 | 0.0195 | 0.08418 |
| 002603 | 以岭药业 | CN | C 制造业 | 0.1199 | 19.7 | 0.334 | 2.224 | 0.3214 | 0.03296 | 0.07009 |
| 002605 | 姚记科技 | CN | I 信息技术 | 0.1273 | 16.56 | 0.4017 | 1.992 | 0.1154 | 0.01738 | 0.06377 |
| 002734 | 利民股份 | CN | C 制造业 | 0.1483 | 14.73 | 0.2812 | 2.001 | 0.2648 | 0.02661 | 0.06498 |
| 002773 | 康弘药业 | CN | C 制造业 | 0.1302 | 17.18 | 0.3029 | 2.075 | 0.2849 | 0.01967 | 0.07542 |
| 002831 | 裕同科技 | CN | C 制造业 | 0.1356 | 16.21 | 0.2902 | 2.963 | 0.4815 | 0.01623 | 0.07489 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.1 | 0.3177 | 2.596 | 0.4149 | 0.03077 | 0.08018 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 17.98 | 0.315 | 2.786 | 0.4503 | 0.03041 | 0.06532 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 16.5 | 0.2939 | 2.162 | 0.3055 | 0.01618 | 0.06362 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.524 | 0.3803 | 3.344 | 0.4402 | 0.03779 | 0.1327 |
| 300595 | 欧普康视 | CN | C 制造业 | 0.1003 | 21.32 | 0.3525 | 2.026 | 0.2696 | 0.01002 | 0.07122 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.75 | 0.2484 | 2.126 | 0.296 | 0.03303 | 0.1147 |
| 300770 | 新媒股份 | CN | I 信息技术 | 0.1747 | 11.64 | 0.3846 | 2.064 | 0.1325 | 0.01884 | 0.1012 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 15.33 | 0.2833 | 2.243 | 0.3261 | 0.01427 | 0.04216 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 17.67 | 0.3108 | 1.734 | 0.1829 | 0.01989 | 0.05399 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.75 | 0.3503 | 2.104 | 0.4115 | 0.04012 | 0.1259 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 21.42 | 0.45 | 2.008 | 0.3879 | 0.02147 | 0.07631 |
| 600461 | 洪城环境 | CN | SW_UNKNOWN | 0.1244 | 10.42 | 0.2757 | 1.217 | 0.1622 | 0.04819 | 0.1535 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 11.24 | 0.2873 | 1.19 | 0.1525 | 0.02961 | 0.1542 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.09 | 0.3211 | 1.618 | 0.2929 | 0.02589 | 0.1272 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.79 | 0.3346 | 2.013 | 0.3888 | 0.01401 | 0.1241 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.27 | 0.3897 | 2.189 | 0.4296 | 0.03002 | 0.05973 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 9.552 | 0.2674 | 1.481 | 0.2451 | 0.05523 | 0.1732 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.43 | 0.4082 | 2.211 | 0.4361 | 0.02101 | 0.0706 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 17.12 | 0.3846 | 1.852 | 0.3517 | 0.02021 | 0.0818 |
| 601827 | 三峰环境 | CN | SW_UNKNOWN | 0.1061 | 11.03 | 0.2831 | 1.094 | 0.1242 | 0.02806 | 0.1726 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.949 | 0.2702 | 1.134 | 0.1376 | 0.0477 | 0.1657 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 14.83 | 0.3526 | 1.97 | 0.3795 | 0.01527 | 0.07783 |
| 603043 | 广州酒家 | CN | SW_UNKNOWN | 0.1253 | 16.88 | 0.3818 | 2.063 | 0.405 | 0.02849 | 0.09053 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 17.47 | 0.3934 | 2.163 | 0.424 | 0.0166 | 0.05769 |
| 603391 | 力聚热能 | CN | SW_UNKNOWN | 0.1037 | 22.17 | 0.4611 | 2.205 | 0.4342 | 0.02329 | 0.06915 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.04 | 0.2836 | 1.937 | 0.3689 | 0.03102 | 0.1086 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.35 | 0.3763 | 1.907 | 0.3605 | 0.03205 | 0.07678 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 12.99 | 0.3184 | 2.118 | 0.4161 | 0.04829 | 0.1182 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000513 | WATCH | passed_depth_scan | 2.693 | 2.696 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000538 | WATCH | passed_depth_scan | 8.665 | 8.678 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.063 | 2.067 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000739 | WATCH | passed_depth_scan | 1.857 | 1.861 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000786 | WATCH | passed_depth_scan | 3.757 | 3.767 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.002 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000915 | SKIP | spread_too_wide | 0.998 | 1.002 | 34 | normal | True | 0 | 0 | OK |  | True |
| 000975 | SKIP | spread_too_wide | 6.146 | 6.169 | 38 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 3.974 | 3.991 | 42 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 4.729 | 4.751 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.406 | 9.453 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.093 | 1.099 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.726 | 8.776 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.111 | 1.118 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002223 | SKIP | spread_too_wide | 2.592 | 2.609 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002236 | SKIP | spread_too_wide | 5.437 | 5.475 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 1.966 | 1.981 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.838 | 3.868 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002555 | SKIP | spread_too_wide | 4.186 | 4.22 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002603 | SKIP | spread_too_wide | 2.524 | 2.545 | 86 | normal | True | 0 | 0 | OK |  | True |
| 002605 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 002734 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 002773 | SKIP | spread_too_wide | 1.984 | 2.004 | 98 | normal | True | 0 | 0 | OK |  | True |
| 002831 | SKIP | spread_too_wide | 3.636 | 3.674 | 102 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.314 | 1.329 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 300595 | SKIP | spread_too_wide | 1.019 | 1.031 | 122 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 126 | normal | True | 0 | 0 | OK |  | True |
| 300770 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.198 | 2.228 | 134 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.993 | 1.007 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.791 | 2.831 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.613 | 9.754 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600461 | SKIP | spread_too_wide | 1.235 | 1.254 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.288 | 3.339 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.579 | 1.604 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 167.1 | 169.9 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.997 | 1.014 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.422 | 1.446 | 170 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 105.4 | 107.2 | 174 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.146 | 2.185 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601827 | SKIP | spread_too_wide | 1.352 | 1.377 | 182 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.026 | 1.045 | 186 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.562 | 1.592 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603043 | SKIP | spread_too_wide | 0.99 | 1.01 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603391 | SKIP | spread_too_wide | 0.99 | 1.01 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.937 | 2.998 | 206 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.729 | 1.766 | 210 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.323 | 2.373 | 214 | normal | True | 0 | 0 | OK |  | True |
