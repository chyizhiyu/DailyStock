# DailyStock Funnel Dashboard

- As of: `2026-07-24`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7947 | - | 387.399 |
| step2_hard_filters | 7947 | 2452 | risk_screen: 1479, listing_age: 572, liquidity: 1445, market_cap: 1643, performance_floor: 356 | 0.494 |
| step3_financial_quality | 2452 | 236 | profitability: 2006, leverage: 42, cash_flow_quality: 95, growth: 73 | 0.062 |
| step4_valuation | 236 | 40 | missing_valuation_data: 7, pe_valuation_percentile: 109, pb_valuation_percentile: 72, dividend_yield: 8 | 0.226 |
| step5_futu_executor | 40 | 40 | spread_too_wide: 34 | 0.006 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5129 | 0 | 2818 | 0 |
| step2_hard_filters | 2256 | 2873 | 196 | 2622 |
| step3_financial_quality | 215 | 2041 | 21 | 175 |
| step4_valuation | 40 | 175 | 0 | 21 |
| step5_futu_executor | 40 | 34 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 1476 |
| step2_hard_filters | listing_age | 273 | 299 |
| step2_hard_filters | liquidity | 819 | 626 |
| step2_hard_filters | market_cap | 1437 | 206 |
| step2_hard_filters | performance_floor | 341 | 15 |
| step3_financial_quality | profitability | 1848 | 158 |
| step3_financial_quality | leverage | 34 | 8 |
| step3_financial_quality | cash_flow_quality | 92 | 3 |
| step3_financial_quality | growth | 67 | 6 |
| step4_valuation | missing_valuation_data | 5 | 2 |
| step4_valuation | pe_valuation_percentile | 92 | 17 |
| step4_valuation | pb_valuation_percentile | 70 | 2 |
| step4_valuation | dividend_yield | 8 | 0 |
| step5_futu_executor | spread_too_wide | 34 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.79 | 0.2241 | 1.07 | 0.2759 | 0.03439 | 0.1708 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 20.84 | 0.3927 | 2.223 | 0.4294 | 0.01675 | 0.07775 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.83 | 0.2414 | 1.56 | 0.5 | 0.02561 | 0.2123 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.37 | 0.2787 | 2.204 | 0.4247 | 0.05821 | 0.1237 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.85 | 0.2488 | 1.95 | 0.3585 | 0.07065 | 0.2194 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 20.36 | 0.3333 | 3.722 | 0.4 | 0.01703 | 0.07743 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.99 | 0.2609 | 1.768 | 0.2903 | 0.02437 | 0.1341 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 13.04 | 0.2586 | 1.423 | 0.431 | 0.03755 | 0.2299 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 14.63 | 0.2908 | 1.902 | 0.3428 | 0.02778 | 0.06742 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 10.96 | 0.1667 | 2.088 | 0.3333 | 0.0331 | 0.111 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 16.83 | 0.3244 | 2.368 | 0.4667 | 0.009532 | 0.05353 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.76 | 0.3228 | 2.27 | 0.4394 | 0.02012 | 0.06377 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 13.3 | 0.2777 | 1.746 | 0.2845 | 0.01326 | 0.06919 |
| 002545 | 东方铁塔 | CN | C 制造业 | 0.1297 | 19.14 | 0.3648 | 2.26 | 0.4367 | 0.01913 | 0.1034 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 25.72 | 0.4854 | 2.817 | 0.4728 | 0.007291 | 0.06496 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 15.99 | 0.3102 | 2.319 | 0.4556 | 0.03077 | 0.08973 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 21 | 0.403 | 2.066 | 0.4179 | 0.009588 | 0.09361 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 18.57 | 0.4435 | 1.91 | 0.1632 | 0.007937 | 0.07645 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 24.2 | 0.3571 | 3.414 | 0.5 | 0.0111 | 0.07592 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 20.88 | 0.3942 | 2.176 | 0.4163 | 0.014 | 0.04125 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.67 | 0.2472 | 1.42 | 0.1633 | 0.02034 | 0.084 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 15.31 | 0.2997 | 2.005 | 0.3764 | 0.01626 | 0.0686 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.23 | 0.243 | 2.23 | 0.4299 | 0.02579 | 0.1519 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 10.57 | 0.2457 | 1.913 | 0.3444 | 0.03303 | 0.1274 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 8.931 | 0.2373 | 2.295 | 0.4493 | 0.00878 | 0.07883 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 11.5 | 0.2535 | 1.682 | 0.2614 | 0.01274 | 0.05622 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 15.42 | 0.3018 | 1.513 | 0.2021 | 0.01989 | 0.06187 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 18.82 | 0.4468 | 1.765 | 0.4005 | 0.02544 | 0.08685 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.39 | 0.3413 | 1.419 | 0.2876 | 0.03914 | 0.1099 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.29 | 0.3408 | 1.491 | 0.3206 | 0.06203 | 0.1561 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 10.09 | 0.2766 | 1.067 | 0.1537 | 0.03224 | 0.1719 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 10.8 | 0.2904 | 1.335 | 0.2596 | 0.02672 | 0.1542 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 12.42 | 0.3234 | 1.812 | 0.4151 | 0.01689 | 0.1378 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 17.18 | 0.4206 | 2.061 | 0.4908 | 0.0245 | 0.07572 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.492 | 0.2693 | 1.081 | 0.1601 | 0.0464 | 0.1737 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.01 | 0.3349 | 1.728 | 0.3913 | 0.01977 | 0.08876 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 15.84 | 0.3917 | 1.961 | 0.4619 | 0.01694 | 0.06364 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.4 | 0.3028 | 1.997 | 0.4711 | 0.03102 | 0.1053 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.82 | 0.4124 | 1.962 | 0.4624 | 0.03908 | 0.07463 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.83 | 0.2917 | 1.766 | 0.4018 | 0.05941 | 0.1417 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.165 | 2.167 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.498 | 3.503 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.424 | 2.429 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 6.035 | 6.053 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 4.104 | 4.118 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.904 | 3.919 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.157 | 1.161 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.272 | 8.31 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.162 | 2.172 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.141 | 1.147 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.329 | 3.348 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002545 | SKIP | spread_too_wide | 2.302 | 2.316 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.58 | 4.611 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.013 | 1.021 | 74 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.487 | 1.499 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.835 | 7.9 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 0.995 | 1.006 | 106 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 1.65 | 1.669 | 110 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 8.458 | 8.558 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.114 | 6.189 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.854 | 2.89 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 2.953 | 2.991 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.304 | 1.322 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 150.6 | 152.7 | 138 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 98.42 | 99.82 | 142 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 0.993 | 1.007 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.372 | 1.393 | 150 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.992 | 1.008 | 154 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.036 | 3.085 | 158 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.783 | 1.812 | 162 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 1.941 | 1.974 | 166 | normal | True | 0 | 0 | OK |  | True |
