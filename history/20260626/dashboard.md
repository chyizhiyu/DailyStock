# DailyStock Funnel Dashboard

- As of: `2026-06-26`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7848 | - | 677.289 |
| step2_hard_filters | 7848 | 2659 | risk_screen: 1490, listing_age: 531, liquidity: 970, market_cap: 1781, performance_floor: 417 | 0.765 |
| step3_financial_quality | 2659 | 256 | profitability: 2179, leverage: 39, cash_flow_quality: 103, growth: 82 | 0.071 |
| step4_valuation | 256 | 52 | missing_valuation_data: 12, pe_valuation_percentile: 123, pb_valuation_percentile: 61, dividend_yield: 8 | 0.288 |
| step5_futu_executor | 52 | 52 | spread_too_wide: 46 | 0.009 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 2787 | 0 |
| step2_hard_filters | 2436 | 2625 | 223 | 2564 |
| step3_financial_quality | 231 | 2205 | 25 | 198 |
| step4_valuation | 52 | 179 | 0 | 25 |
| step5_futu_executor | 52 | 46 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1489 |
| step2_hard_filters | listing_age | 256 | 275 |
| step2_hard_filters | liquidity | 424 | 546 |
| step2_hard_filters | market_cap | 1550 | 231 |
| step2_hard_filters | performance_floor | 394 | 23 |
| step3_financial_quality | profitability | 2003 | 176 |
| step3_financial_quality | leverage | 32 | 7 |
| step3_financial_quality | cash_flow_quality | 98 | 5 |
| step3_financial_quality | growth | 72 | 10 |
| step4_valuation | missing_valuation_data | 9 | 3 |
| step4_valuation | pe_valuation_percentile | 103 | 20 |
| step4_valuation | pb_valuation_percentile | 59 | 2 |
| step4_valuation | dividend_yield | 8 | 0 |
| step5_futu_executor | spread_too_wide | 46 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 16.1 | 0.3066 | 2.594 | 0.453 | 0.02899 | 0.08176 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 9.603 | 0.2069 | 0.952 | 0.2069 | 0.03641 | 0.192 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 12.18 | 0.2653 | 2.009 | 0.3087 | 0.05821 | 0.1358 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.84 | 0.2616 | 2.129 | 0.3393 | 0.01542 | 0.201 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 10.76 | 0.25 | 1.586 | 0.1813 | 0.02437 | 0.1495 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.81 | 0.2759 | 1.398 | 0.4138 | 0.03755 | 0.2339 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.38 | 0.2775 | 2.588 | 0.4498 | 0.02609 | 0.09677 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 15.14 | 0.2933 | 2.119 | 0.3367 | 0.04053 | 0.1146 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.8 | 0.2711 | 1.664 | 0.2061 | 0.02778 | 0.07703 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 9.909 | 0.1724 | 1.784 | 0.2414 | 0.0331 | 0.13 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 19.32 | 0.352 | 2.718 | 0.4757 | 0.009285 | 0.04663 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.83 | 0.2611 | 2.677 | 0.4704 | 0.04338 | 0.1359 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 17.36 | 0.3245 | 2.211 | 0.361 | 0.01974 | 0.05824 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 15.61 | 0.3023 | 2.113 | 0.3351 | 0.02012 | 0.0685 |
| 002351 | 漫步者 | CN | C 制造业 | 0.1494 | 19.12 | 0.3483 | 2.654 | 0.4641 | 0.01791 | 0.0478 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14.77 | 0.2912 | 1.939 | 0.2886 | 0.01326 | 0.0623 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 26.63 | 0.4339 | 2.614 | 0.4577 | 0.01458 | 0.07706 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 17.81 | 0.3325 | 2.555 | 0.4424 | 0.03077 | 0.08147 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 11.9 | 0.2622 | 2.15 | 0.3457 | 0.05394 | 0.08493 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 23.75 | 0.4219 | 2.338 | 0.4375 | 0.009588 | 0.08275 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 17.15 | 0.4274 | 1.764 | 0.1111 | 0.007937 | 0.08278 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 17.05 | 0.3214 | 2.642 | 0.4619 | 0.03041 | 0.06889 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 24.88 | 0.417 | 2.593 | 0.4519 | 0.01075 | 0.03462 |
| 300286 | 安科瑞 | CN | C 制造业 | 0.1025 | 28.96 | 0.4614 | 2.711 | 0.4752 | 0.01405 | 0.03567 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.56 | 0.2479 | 1.406 | 0.139 | 0.02034 | 0.08487 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 15.06 | 0.2923 | 1.974 | 0.2997 | 0.01626 | 0.06968 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 11.77 | 0.259 | 2.565 | 0.4445 | 0.02579 | 0.132 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 11.02 | 0.2532 | 2.666 | 0.4678 | 0.03286 | 0.07077 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 8.576 | 0.2363 | 2.204 | 0.3589 | 0.00878 | 0.0821 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 14.07 | 0.2838 | 2.058 | 0.3203 | 0.01274 | 0.04593 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 20.02 | 0.3621 | 1.965 | 0.2965 | 0.01989 | 0.04764 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 15.93 | 0.3957 | 1.9 | 0.4059 | 0.05596 | 0.08247 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.29 | 0.3665 | 2.039 | 0.4444 | 0.04141 | 0.13 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 9.781 | 0.2808 | 1.337 | 0.2479 | 0.02429 | 0.09193 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 12.88 | 0.3378 | 1.366 | 0.2567 | 0.0417 | 0.1142 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 11.93 | 0.323 | 1.339 | 0.2484 | 0.06203 | 0.1738 |
| 600415 | 小商品城 | CN | SW_UNKNOWN | 0.1753 | 12.68 | 0.3346 | 2.242 | 0.4842 | 0.04405 | 0.1967 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 9.953 | 0.2841 | 1.053 | 0.1497 | 0.03346 | 0.1742 |
| 600598 | 北大荒 | CN | SW_UNKNOWN | 0.149 | 16.45 | 0.4059 | 2.235 | 0.4815 | 0.03645 | 0.06467 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.34 | 0.3855 | 2.169 | 0.469 | 0.04555 | 0.06525 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 11.87 | 0.3216 | 1.238 | 0.2113 | 0.02576 | 0.1301 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.97 | 0.3244 | 1.479 | 0.2961 | 0.02672 | 0.1392 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 10.65 | 0.2956 | 1.554 | 0.3165 | 0.01815 | 0.1607 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 15.96 | 0.3971 | 2.023 | 0.4384 | 0.03248 | 0.06464 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 14.88 | 0.3772 | 1.785 | 0.3791 | 0.02603 | 0.08746 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.136 | 0.2706 | 1.041 | 0.1455 | 0.05195 | 0.1804 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 11.02 | 0.3035 | 1.463 | 0.2882 | 0.02055 | 0.1048 |
| 603277 | 银都股份 | CN | SW_UNKNOWN | 0.1694 | 12.68 | 0.3346 | 2.182 | 0.4703 | 0.03036 | 0.06998 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.96 | 0.3234 | 2.099 | 0.4551 | 0.03102 | 0.1002 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 15.36 | 0.3865 | 1.791 | 0.3804 | 0.03908 | 0.08175 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.22 | 0.2892 | 1.667 | 0.3471 | 0.05235 | 0.1502 |
| 605183 | 确成股份 | CN | SW_UNKNOWN | 0.1407 | 13.27 | 0.3475 | 1.761 | 0.3712 | 0.02712 | 0.08549 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 2.799 | 2.801 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 1.926 | 1.929 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 3.683 | 3.693 | 26 | normal | True | 0 | 0 | OK |  | True |
| 001286 | WATCH | passed_depth_scan | 3.838 | 3.85 | 30 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.076 | 9.107 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 0.998 | 1.002 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.012 | 1.016 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 7.066 | 7.099 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.481 | 2.494 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.081 | 1.087 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 1.846 | 1.857 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.062 | 1.069 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002351 | SKIP | spread_too_wide | 0.997 | 1.003 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.695 | 3.721 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.145 | 1.155 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.373 | 1.385 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.247 | 1.259 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.166 | 1.177 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300286 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.049 | 1.062 | 118 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.019 | 2.044 | 126 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.897 | 1.923 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.705 | 2.742 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.609 | 1.632 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 5.876 | 5.963 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.56 | 2.598 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600415 | SKIP | spread_too_wide | 5.311 | 5.393 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 2.91 | 2.956 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600598 | SKIP | spread_too_wide | 1.903 | 1.934 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.979 | 7.096 | 166 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.992 | 1.008 | 170 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.442 | 1.467 | 174 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 128.9 | 131.2 | 178 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.991 | 1.009 | 182 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 85.03 | 86.62 | 186 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 0.991 | 1.01 | 190 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.16 | 1.182 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603277 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.183 | 3.248 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.624 | 1.658 | 206 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 1.828 | 1.867 | 210 | normal | True | 0 | 0 | OK |  | True |
| 605183 | SKIP | spread_too_wide | 0.989 | 1.011 | 214 | normal | True | 0 | 0 | OK |  | True |
