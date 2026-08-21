# DailyStock Funnel Dashboard

- As of: `2026-08-21`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7928 | - | 911.300 |
| step2_hard_filters | 7928 | 2656 | risk_screen: 1468, listing_age: 533, liquidity: 1300, market_cap: 1517, missing_financials: 57, performance_floor: 397 | 0.421 |
| step3_financial_quality | 2656 | 255 | profitability: 2173, leverage: 51, cash_flow_quality: 100, growth: 77 | 0.050 |
| step4_valuation | 255 | 50 | missing_valuation_data: 6, pe_valuation_percentile: 122, pb_valuation_percentile: 66, dividend_yield: 11 | 0.194 |
| step5_futu_executor | 50 | 50 | spread_too_wide: 44 | 0.005 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5126 | 0 | 2802 | 0 |
| step2_hard_filters | 2423 | 2703 | 233 | 2569 |
| step3_financial_quality | 224 | 2199 | 31 | 202 |
| step4_valuation | 50 | 174 | 0 | 31 |
| step5_futu_executor | 50 | 44 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 1465 |
| step2_hard_filters | listing_age | 241 | 292 |
| step2_hard_filters | liquidity | 692 | 608 |
| step2_hard_filters | market_cap | 1387 | 130 |
| step2_hard_filters | missing_financials | 0 | 57 |
| step2_hard_filters | performance_floor | 380 | 17 |
| step3_financial_quality | profitability | 1993 | 180 |
| step3_financial_quality | leverage | 43 | 8 |
| step3_financial_quality | cash_flow_quality | 96 | 4 |
| step3_financial_quality | growth | 67 | 10 |
| step4_valuation | missing_valuation_data | 5 | 1 |
| step4_valuation | pe_valuation_percentile | 96 | 26 |
| step4_valuation | pb_valuation_percentile | 63 | 3 |
| step4_valuation | dividend_yield | 10 | 1 |
| step5_futu_executor | spread_too_wide | 44 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.6 | 0.2241 | 1.051 | 0.2414 | 0.03439 | 0.1739 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 19.14 | 0.3403 | 1.905 | 0.2684 | 0.008764 | 0.08464 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.38 | 0.2414 | 1.54 | 0.4828 | 0.02561 | 0.2206 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.8 | 0.2757 | 2.619 | 0.4659 | 0.05821 | 0.1199 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.39 | 0.2437 | 2.123 | 0.3372 | 0.07065 | 0.229 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.72 | 0.2521 | 1.728 | 0.2106 | 0.02437 | 0.1372 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 11.89 | 0.2586 | 1.344 | 0.431 | 0.03755 | 0.2521 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 19 | 0.3393 | 2.658 | 0.4743 | 0.04053 | 0.09132 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 14.33 | 0.282 | 1.862 | 0.2547 | 0.02778 | 0.06885 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.21 | 0.1667 | 2.136 | 0.3 | 0.0331 | 0.1086 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 17.71 | 0.3188 | 2.492 | 0.4317 | 0.009532 | 0.05087 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.9 | 0.2542 | 2.691 | 0.4816 | 0.04338 | 0.1352 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.91 | 0.3697 | 2.657 | 0.4737 | 0.01974 | 0.04837 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.65 | 0.3041 | 2.254 | 0.3782 | 0.02012 | 0.06422 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14 | 0.2773 | 1.837 | 0.2489 | 0.01326 | 0.06576 |
| 002545 | 东方铁塔 | CN | C 制造业 | 0.1297 | 17.97 | 0.3246 | 2.121 | 0.3361 | 0.01913 | 0.1102 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 27.8 | 0.4832 | 3.044 | 0.4412 | 0.007291 | 0.06011 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 24.51 | 0.4181 | 1.92 | 0.2726 | 0.01238 | 0.04804 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 24.09 | 0.4139 | 2.429 | 0.417 | 0.01458 | 0.0852 |
| 002831 | 裕同科技 | CN | C 制造业 | 0.1356 | 14.59 | 0.2841 | 2.667 | 0.4769 | 0.01961 | 0.08322 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.02 | 0.3262 | 2.614 | 0.4627 | 0.03077 | 0.07963 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.45 | 0.4412 | 2.001 | 0.1471 | 0.007937 | 0.07299 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 23.83 | 0.3571 | 3.361 | 0.5 | 0.0111 | 0.0771 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 18.5 | 0.4244 | 3.09 | 0.458 | 0.01185 | 0.09768 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.99 | 0.3845 | 2.292 | 0.3866 | 0.014 | 0.03917 |
| 300286 | 安科瑞 | CN | C 制造业 | 0.1025 | 23.28 | 0.4028 | 2.179 | 0.3535 | 0.01405 | 0.04438 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.64 | 0.2453 | 1.416 | 0.1229 | 0.02034 | 0.08422 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.26 | 0.2426 | 2.302 | 0.3887 | 0.02579 | 0.1514 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 12.05 | 0.2558 | 2.181 | 0.3545 | 0.03303 | 0.1118 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 10.06 | 0.2411 | 2.434 | 0.4181 | 0.03286 | 0.07752 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 8.81 | 0.2369 | 2.264 | 0.3808 | 0.00878 | 0.07992 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 16.68 | 0.3046 | 1.637 | 0.1828 | 0.01989 | 0.05719 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 15.63 | 0.3752 | 1.864 | 0.3766 | 0.05596 | 0.08407 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 13.9 | 0.3459 | 1.983 | 0.4092 | 0.03634 | 0.1337 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 23.7 | 0.4954 | 2.222 | 0.4775 | 0.02544 | 0.06898 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.11 | 0.3275 | 1.471 | 0.2647 | 0.06203 | 0.1582 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.11 | 0.3656 | 2.137 | 0.4541 | 0.04277 | 0.06624 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.64 | 0.3037 | 1.438 | 0.2546 | 0.02672 | 0.1432 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.18 | 0.3289 | 1.923 | 0.3931 | 0.01689 | 0.1299 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.04 | 0.3995 | 2.16 | 0.4619 | 0.02841 | 0.06054 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 17.45 | 0.4073 | 2.093 | 0.4399 | 0.0245 | 0.07457 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 10.95 | 0.2899 | 1.223 | 0.1826 | 0.02239 | 0.09637 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.958 | 0.2752 | 1.135 | 0.1541 | 0.0464 | 0.1655 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.24 | 0.3298 | 1.759 | 0.3537 | 0.01977 | 0.08718 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 13.78 | 0.3436 | 1.86 | 0.3757 | 0.01039 | 0.06844 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.67 | 0.3931 | 2.065 | 0.4339 | 0.01694 | 0.06047 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.14 | 0.294 | 2.048 | 0.428 | 0.03102 | 0.1077 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 18.5 | 0.4257 | 2.158 | 0.461 | 0.03908 | 0.06786 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 11.29 | 0.295 | 2.074 | 0.4362 | 0.05941 | 0.1207 |
| 688566 | 吉贝尔 | CN | SW_UNKNOWN | 0.1116 | 20.06 | 0.4505 | 2.13 | 0.4518 | 0.0102 | 0.04698 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.127 | 2.129 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.214 | 3.218 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.333 | 2.338 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.011 | 4.023 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.56 | 3.572 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.24 | 1.245 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.132 | 1.137 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.46 | 8.499 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.275 | 2.286 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.087 | 1.093 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.223 | 2.236 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.133 | 1.14 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.501 | 3.525 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002545 | SKIP | spread_too_wide | 2.16 | 2.175 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.948 | 4.985 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.813 | 1.827 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002831 | SKIP | spread_too_wide | 3.275 | 3.303 | 86 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.557 | 1.571 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.709 | 7.784 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.03 | 1.041 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300286 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 0.994 | 1.006 | 126 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.993 | 1.007 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.861 | 1.886 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.63 | 2.667 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 10.63 | 10.79 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.812 | 2.855 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.879 | 6.986 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.403 | 1.425 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 159.6 | 162.2 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.992 | 1.008 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 99.81 | 101.5 | 170 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 5.708 | 5.808 | 174 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.027 | 1.046 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.395 | 1.421 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.991 | 1.009 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.01 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.962 | 3.02 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.958 | 1.997 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.275 | 2.322 | 202 | normal | True | 0 | 0 | OK |  | True |
| 688566 | SKIP | spread_too_wide | 0.99 | 1.01 | 206 | normal | True | 0 | 0 | OK |  | True |
