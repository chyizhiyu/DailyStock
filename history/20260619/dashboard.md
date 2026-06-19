# DailyStock Funnel Dashboard

- As of: `2026-06-19`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7841 | - | 366.749 |
| step2_hard_filters | 7841 | 2745 | risk_screen: 1475, listing_age: 531, liquidity: 1011, market_cap: 1622, missing_financials: 16, performance_floor: 441 | 0.587 |
| step3_financial_quality | 2745 | 262 | profitability: 2255, leverage: 42, cash_flow_quality: 103, growth: 83 | 0.065 |
| step4_valuation | 262 | 50 | missing_valuation_data: 15, pe_valuation_percentile: 125, pb_valuation_percentile: 64, dividend_yield: 8 | 0.251 |
| step5_futu_executor | 50 | 50 | spread_too_wide: 44 | 0.007 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 2780 | 0 |
| step2_hard_filters | 2517 | 2544 | 228 | 2552 |
| step3_financial_quality | 232 | 2285 | 30 | 198 |
| step4_valuation | 50 | 182 | 0 | 30 |
| step5_futu_executor | 50 | 44 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1474 |
| step2_hard_filters | listing_age | 262 | 269 |
| step2_hard_filters | liquidity | 479 | 532 |
| step2_hard_filters | market_cap | 1383 | 239 |
| step2_hard_filters | missing_financials | 0 | 16 |
| step2_hard_filters | performance_floor | 419 | 22 |
| step3_financial_quality | profitability | 2083 | 172 |
| step3_financial_quality | leverage | 33 | 9 |
| step3_financial_quality | cash_flow_quality | 97 | 6 |
| step3_financial_quality | growth | 72 | 11 |
| step4_valuation | missing_valuation_data | 12 | 3 |
| step4_valuation | pe_valuation_percentile | 100 | 25 |
| step4_valuation | pb_valuation_percentile | 62 | 2 |
| step4_valuation | dividend_yield | 8 | 0 |
| step5_futu_executor | spread_too_wide | 44 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 16.92 | 0.3087 | 2.726 | 0.4471 | 0.02899 | 0.07782 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.09 | 0.1724 | 1 | 0.2069 | 0.03464 | 0.1826 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 12.8 | 0.2632 | 2.111 | 0.2997 | 0.05821 | 0.1292 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.87 | 0.2569 | 2.134 | 0.3081 | 0.07391 | 0.2005 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 19.68 | 0.3448 | 3.597 | 0.4483 | 0.01703 | 0.08011 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.4 | 0.25 | 1.681 | 0.1823 | 0.02437 | 0.1411 |
| 001216 | 华瓷股份 | CN | C 制造业 | 0.1235 | 19.77 | 0.343 | 2.695 | 0.4376 | 0.02395 | 0.06866 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 13.61 | 0.2759 | 1.485 | 0.4138 | 0.03934 | 0.2202 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 12.67 | 0.2611 | 2.45 | 0.3885 | 0.02609 | 0.1022 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 15.73 | 0.2928 | 2.2 | 0.3235 | 0.04053 | 0.1103 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 13.11 | 0.2659 | 1.704 | 0.1908 | 0.02778 | 0.07525 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 9.983 | 0.1724 | 1.797 | 0.2414 | 0.0331 | 0.129 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.46 | 0.2505 | 2.593 | 0.417 | 0.04338 | 0.1403 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 17.8 | 0.3203 | 2.267 | 0.3473 | 0.01974 | 0.0568 |
| 002351 | 漫步者 | CN | C 制造业 | 0.1494 | 20.83 | 0.3531 | 2.892 | 0.4804 | 0.01791 | 0.04388 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14.08 | 0.2807 | 1.848 | 0.2326 | 0.01326 | 0.06538 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 25.43 | 0.4573 | 2.784 | 0.3077 | 0.007291 | 0.06572 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 27.89 | 0.4318 | 2.738 | 0.4524 | 0.01458 | 0.07359 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 17.65 | 0.3182 | 2.532 | 0.4043 | 0.03077 | 0.08221 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.25 | 0.2595 | 2.214 | 0.3298 | 0.05394 | 0.08248 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 17.81 | 0.4274 | 1.832 | 0.09829 | 0.007937 | 0.07971 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 17.43 | 0.315 | 2.701 | 0.4392 | 0.03041 | 0.06736 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 24.98 | 0.4049 | 2.603 | 0.4191 | 0.01447 | 0.03449 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 11.04 | 0.2468 | 1.47 | 0.1364 | 0.02034 | 0.08117 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 16.13 | 0.2997 | 2.113 | 0.3007 | 0.01626 | 0.06509 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 13.53 | 0.2722 | 2.95 | 0.4878 | 0.02579 | 0.1148 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 10.56 | 0.2437 | 1.912 | 0.2489 | 0.03303 | 0.1276 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 11.62 | 0.2548 | 2.81 | 0.4667 | 0.03286 | 0.06714 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 9.178 | 0.2373 | 2.358 | 0.3705 | 0.00878 | 0.07671 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 15.9 | 0.297 | 2.326 | 0.3631 | 0.01274 | 0.04065 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 21.41 | 0.3626 | 2.101 | 0.2955 | 0.01989 | 0.04456 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 15.76 | 0.3786 | 1.879 | 0.3749 | 0.04924 | 0.0834 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.6 | 0.3577 | 2.082 | 0.4263 | 0.04054 | 0.1272 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 23.36 | 0.4893 | 2.19 | 0.4458 | 0.01969 | 0.06998 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.27 | 0.2813 | 1.404 | 0.247 | 0.02314 | 0.08756 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.22 | 0.3332 | 1.402 | 0.2465 | 0.04063 | 0.1113 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.44 | 0.3197 | 1.397 | 0.2433 | 0.06203 | 0.1667 |
| 600415 | 小商品城 | CN | SW_UNKNOWN | 0.1753 | 13.69 | 0.3438 | 2.421 | 0.4917 | 0.04405 | 0.1822 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 10.53 | 0.2873 | 1.114 | 0.1511 | 0.03163 | 0.1647 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 16.03 | 0.3832 | 2.267 | 0.4611 | 0.0436 | 0.06246 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.33 | 0.336 | 1.648 | 0.3188 | 0.02672 | 0.125 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 11.95 | 0.3114 | 1.743 | 0.342 | 0.01618 | 0.1433 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 16.73 | 0.3925 | 2.119 | 0.4323 | 0.031 | 0.06169 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 15.51 | 0.3744 | 1.861 | 0.3716 | 0.02496 | 0.08387 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.678 | 0.2688 | 1.103 | 0.1474 | 0.04904 | 0.1703 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 12.15 | 0.3146 | 1.614 | 0.3095 | 0.01863 | 0.09503 |
| 603277 | 银都股份 | CN | SW_UNKNOWN | 0.1694 | 12.51 | 0.3211 | 2.154 | 0.4398 | 0.03036 | 0.07089 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 12.51 | 0.3207 | 2.195 | 0.4462 | 0.03102 | 0.09579 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.3 | 0.3869 | 1.902 | 0.38 | 0.03908 | 0.07701 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.86 | 0.2924 | 1.77 | 0.3466 | 0.05779 | 0.1414 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 2.94 | 2.943 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.025 | 2.028 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 5.834 | 5.849 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 3.902 | 3.913 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001216 | SKIP | spread_too_wide | 0.998 | 1.002 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 4.076 | 4.092 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 8.588 | 8.624 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.026 | 1.031 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.036 | 1.041 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 7.116 | 7.155 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.047 | 1.053 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 1.893 | 1.904 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002351 | SKIP | spread_too_wide | 0.997 | 1.003 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.521 | 3.546 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.526 | 4.559 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.426 | 1.439 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.275 | 1.287 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.17 | 1.182 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.106 | 1.119 | 118 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.022 | 1.035 | 122 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.281 | 2.31 | 126 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.876 | 1.901 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.762 | 2.801 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 10.48 | 10.63 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.689 | 1.714 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.03 | 6.121 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.669 | 2.71 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600415 | SKIP | spread_too_wide | 5.734 | 5.825 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.078 | 3.128 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 7.292 | 7.414 | 166 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.607 | 1.634 | 170 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 144.6 | 147.2 | 174 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.991 | 1.009 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 88.68 | 90.31 | 182 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 0.998 | 1.017 | 186 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.279 | 1.304 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603277 | SKIP | spread_too_wide | 0.99 | 1.01 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.33 | 3.397 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.725 | 1.76 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 1.941 | 1.982 | 206 | normal | True | 0 | 0 | OK |  | True |
