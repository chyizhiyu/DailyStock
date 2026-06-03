# DailyStock Funnel Dashboard

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 6288 | - | 177.727 |
| step2_hard_filters | 6288 | 2508 | risk_screen: 641, listing_age: 291, liquidity: 1563, market_cap: 862, performance_floor: 423 | 0.530 |
| step3_financial_quality | 2508 | 233 | profitability: 2081, leverage: 32, cash_flow_quality: 95, growth: 67 | 0.059 |
| step4_valuation | 233 | 44 | missing_valuation_data: 25, pe_valuation_percentile: 99, pb_valuation_percentile: 58, dividend_yield: 6, fcf_yield: 1 | 0.227 |
| step5_futu_executor | 44 | 44 | spread_too_wide: 38 | 0.006 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 1227 | 0 |
| step2_hard_filters | 2508 | 2553 | 0 | 1227 |
| step3_financial_quality | 233 | 2275 | 0 | 0 |
| step4_valuation | 44 | 189 | 0 | 0 |
| step5_futu_executor | 44 | 38 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 640 |
| step2_hard_filters | listing_age | 187 | 104 |
| step2_hard_filters | liquidity | 1080 | 483 |
| step2_hard_filters | market_cap | 862 | 0 |
| step2_hard_filters | performance_floor | 423 | 0 |
| step3_financial_quality | profitability | 2081 | 0 |
| step3_financial_quality | leverage | 32 | 0 |
| step3_financial_quality | cash_flow_quality | 95 | 0 |
| step3_financial_quality | growth | 67 | 0 |
| step4_valuation | missing_valuation_data | 25 | 0 |
| step4_valuation | pe_valuation_percentile | 99 | 0 |
| step4_valuation | pb_valuation_percentile | 58 | 0 |
| step4_valuation | dividend_yield | 6 | 0 |
| step4_valuation | fcf_yield | 1 | 0 |
| step5_futu_executor | spread_too_wide | 38 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 18.26 | 0.3129 | 2.942 | 0.4699 | 0.02899 | 0.07209 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.46 | 0.1379 | 1.037 | 0.1207 | 0.0328 | 0.1762 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.37 | 0.26 | 2.204 | 0.305 | 0.05821 | 0.1237 |
| 000893 | 亚钾国际 | CN | C 制造业 | 0.1328 | 24.85 | 0.3853 | 3.025 | 0.4852 | 0.009311 | 0.05429 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 12.04 | 0.2489 | 2.165 | 0.2939 | 0.07194 | 0.1977 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 21.51 | 0.3103 | 3.932 | 0.4483 | 0.01703 | 0.0733 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.66 | 0.2463 | 1.72 | 0.1739 | 0.02437 | 0.1379 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 15.88 | 0.3276 | 1.732 | 0.431 | 0.03125 | 0.1888 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.5 | 0.2627 | 2.61 | 0.4091 | 0.02609 | 0.09596 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 17.07 | 0.2965 | 2.388 | 0.352 | 0.04053 | 0.1016 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 14.01 | 0.268 | 1.821 | 0.1982 | 0.02668 | 0.0704 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 12.61 | 0.1724 | 2.27 | 0.3448 | 0.0331 | 0.1022 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 12.41 | 0.2532 | 2.806 | 0.4419 | 0.04338 | 0.1297 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 18.98 | 0.3219 | 2.417 | 0.3599 | 0.01974 | 0.05327 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 15.91 | 0.2844 | 2.088 | 0.278 | 0.01243 | 0.05785 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 30.11 | 0.4382 | 2.956 | 0.4741 | 0.01458 | 0.06814 |
| 002831 | 裕同科技 | CN | C 制造业 | 0.1356 | 23.41 | 0.3679 | 3.057 | 0.4878 | 0.01623 | 0.0726 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 17.89 | 0.3076 | 2.566 | 0.3996 | 0.03077 | 0.08111 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 18.41 | 0.3161 | 2.853 | 0.453 | 0.03041 | 0.06379 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 19.62 | 0.4231 | 3.277 | 0.3974 | 0.01048 | 0.09208 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.782 | 0.3803 | 3.459 | 0.4444 | 0.03779 | 0.1283 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 12.12 | 0.2495 | 2.192 | 0.3034 | 0.03303 | 0.1112 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.37 | 0.2405 | 2.665 | 0.4181 | 0.00878 | 0.06789 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 21.07 | 0.3436 | 2.372 | 0.3478 | 0.01427 | 0.03986 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 17.78 | 0.3939 | 2.12 | 0.4087 | 0.04911 | 0.0739 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.72 | 0.3457 | 2.099 | 0.4036 | 0.0375 | 0.1262 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 21.75 | 0.4476 | 2.037 | 0.3879 | 0.02049 | 0.07524 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.47 | 0.2757 | 1.431 | 0.2238 | 0.02235 | 0.08588 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.95 | 0.3336 | 1.479 | 0.2368 | 0.03763 | 0.1055 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.89 | 0.3128 | 1.446 | 0.2261 | 0.06203 | 0.1609 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 10.78 | 0.2794 | 1.141 | 0.1353 | 0.03102 | 0.1608 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 17.83 | 0.3948 | 2.521 | 0.4893 | 0.03852 | 0.05615 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.16 | 0.3197 | 1.627 | 0.2868 | 0.02562 | 0.1266 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.66 | 0.3276 | 1.994 | 0.3763 | 0.01412 | 0.1252 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.58 | 0.3916 | 2.227 | 0.4333 | 0.02878 | 0.0587 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 9.759 | 0.2678 | 1.513 | 0.2479 | 0.05317 | 0.1695 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.1 | 0.399 | 2.171 | 0.4203 | 0.02135 | 0.07189 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 17.83 | 0.3953 | 1.929 | 0.3614 | 0.02021 | 0.07854 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.07 | 0.2702 | 1.147 | 0.1367 | 0.04624 | 0.1637 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 14.98 | 0.3499 | 1.99 | 0.3753 | 0.01508 | 0.07704 |
| 603391 | 力聚热能 | CN | SW_UNKNOWN | 0.1037 | 23.87 | 0.4805 | 2.374 | 0.4615 | 0.02329 | 0.06423 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.24 | 0.2868 | 1.971 | 0.3703 | 0.03102 | 0.1067 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.62 | 0.3763 | 1.938 | 0.3633 | 0.03205 | 0.07555 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 13.01 | 0.3137 | 2.122 | 0.4092 | 0.04695 | 0.118 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 3.174 | 3.177 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.099 | 2.102 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000893 | WATCH | passed_depth_scan | 4.199 | 4.208 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 6.376 | 6.395 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 3.991 | 4.004 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 4.753 | 4.772 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.149 | 9.187 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.114 | 1.119 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.107 | 1.113 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.986 | 9.035 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.133 | 1.14 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.018 | 2.031 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.98 | 4.006 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002831 | SKIP | spread_too_wide | 3.756 | 3.784 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.348 | 1.359 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.156 | 1.168 | 98 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.329 | 2.353 | 102 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 2.12 | 2.143 | 106 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.788 | 2.819 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.765 | 9.877 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.724 | 1.745 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.369 | 6.447 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.768 | 2.803 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.157 | 3.198 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 8.125 | 8.235 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.589 | 1.611 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 165.7 | 168.1 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 1.015 | 1.03 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.454 | 1.476 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 103.6 | 105.2 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.238 | 2.273 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.039 | 1.056 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.58 | 1.606 | 166 | normal | True | 0 | 0 | OK |  | True |
| 603391 | SKIP | spread_too_wide | 0.992 | 1.008 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.994 | 3.047 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.76 | 1.792 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.33 | 2.373 | 182 | normal | True | 0 | 0 | OK |  | True |
