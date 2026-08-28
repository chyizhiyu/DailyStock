# DailyStock Funnel Dashboard

- As of: `2026-08-28`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7929 | - | 317.711 |
| step2_hard_filters | 7929 | 2639 | risk_screen: 1471, listing_age: 527, liquidity: 1099, market_cap: 1784, performance_floor: 409 | 0.693 |
| step3_financial_quality | 2639 | 235 | profitability: 2160, leverage: 81, cash_flow_quality: 91, growth: 72 | 0.068 |
| step4_valuation | 235 | 44 | missing_valuation_data: 4, pe_valuation_percentile: 108, pb_valuation_percentile: 63, dividend_yield: 16 | 0.287 |
| step5_futu_executor | 44 | 44 | spread_too_wide: 38 | 0.007 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5126 | 0 | 2803 | 0 |
| step2_hard_filters | 2510 | 2616 | 129 | 2674 |
| step3_financial_quality | 216 | 2294 | 19 | 110 |
| step4_valuation | 44 | 172 | 0 | 19 |
| step5_futu_executor | 44 | 38 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 1468 |
| step2_hard_filters | listing_age | 235 | 292 |
| step2_hard_filters | liquidity | 495 | 604 |
| step2_hard_filters | market_cap | 1487 | 297 |
| step2_hard_filters | performance_floor | 396 | 13 |
| step3_financial_quality | profitability | 2069 | 91 |
| step3_financial_quality | leverage | 75 | 6 |
| step3_financial_quality | cash_flow_quality | 85 | 6 |
| step3_financial_quality | growth | 65 | 7 |
| step4_valuation | missing_valuation_data | 2 | 2 |
| step4_valuation | pe_valuation_percentile | 91 | 17 |
| step4_valuation | pb_valuation_percentile | 63 | 0 |
| step4_valuation | dividend_yield | 16 | 0 |
| step5_futu_executor | spread_too_wide | 38 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.7 | 0.2241 | 1.072 | 0.2414 | 0.03439 | 0.1722 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 19.38 | 0.3393 | 1.929 | 0.2595 | 0.008658 | 0.08361 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.45 | 0.2414 | 1.549 | 0.4655 | 0.02561 | 0.2194 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 14.45 | 0.2789 | 2.742 | 0.4811 | 0.05821 | 0.1145 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.98 | 0.2453 | 2.243 | 0.3577 | 0.07065 | 0.2167 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.84 | 0.2511 | 1.778 | 0.2195 | 0.01702 | 0.1358 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.05 | 0.2586 | 1.362 | 0.4138 | 0.03755 | 0.2487 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 14.2 | 0.2784 | 1.874 | 0.2432 | 0.02778 | 0.06948 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 12.03 | 0.1667 | 1.722 | 0.2667 | 0.0331 | 0.1012 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 18.65 | 0.3293 | 2.613 | 0.4496 | 0.009532 | 0.04829 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.99 | 0.364 | 2.661 | 0.4632 | 0.01974 | 0.0483 |
| 002275 | 桂林三金 | CN | C 制造业 | 0.1389 | 16.95 | 0.3062 | 2.257 | 0.3613 | 0.02244 | 0.09611 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 17.14 | 0.3099 | 2.295 | 0.375 | 0.01125 | 0.06237 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14.47 | 0.2794 | 1.887 | 0.2468 | 0.009865 | 0.06359 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 29.02 | 0.4916 | 3.082 | 0.4496 | 0.02933 | 0.05757 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 24.43 | 0.4154 | 1.914 | 0.2547 | 0.01238 | 0.0482 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 24.2 | 0.4133 | 2.44 | 0.4097 | 0.01458 | 0.08479 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.59 | 0.3283 | 2.744 | 0.4816 | 0.01597 | 0.07717 |
| 002880 | 卫光生物 | CN | C 制造业 | 0.1067 | 20.89 | 0.3613 | 2.134 | 0.3272 | 0.007773 | 0.05114 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 22.64 | 0.3582 | 2.245 | 0.3731 | 0.008716 | 0.08647 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.65 | 0.4328 | 2.006 | 0.1387 | 0.007937 | 0.07227 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 23.6 | 0.3571 | 3.333 | 0.5 | 0.0111 | 0.07785 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 23.75 | 0.4049 | 2.473 | 0.4165 | 0.014 | 0.03627 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.53 | 0.2421 | 1.425 | 0.114 | 0.02034 | 0.08516 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 14.94 | 0.2831 | 1.975 | 0.2752 | 0.01788 | 0.07029 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.65 | 0.2432 | 2.392 | 0.396 | 0.02579 | 0.1458 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.8 | 0.2505 | 2.217 | 0.3508 | 0.03303 | 0.1142 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.72 | 0.3528 | 2.227 | 0.4656 | 0.03634 | 0.1262 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.56 | 0.3349 | 1.5 | 0.2596 | 0.02021 | 0.1085 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.21 | 0.361 | 2.225 | 0.4642 | 0.04277 | 0.06583 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 11.96 | 0.306 | 1.505 | 0.2606 | 0.02557 | 0.1291 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.37 | 0.2945 | 1.437 | 0.2381 | 0.02672 | 0.1465 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.3 | 0.3298 | 1.898 | 0.3743 | 0.02388 | 0.1286 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.33 | 0.4014 | 2.271 | 0.4766 | 0.02841 | 0.05955 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 16.44 | 0.3853 | 1.779 | 0.345 | 0.009791 | 0.08518 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 8.772 | 0.261 | 0.897 | 0.07844 | 0.01526 | 0.1097 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.814 | 0.2702 | 1.159 | 0.1532 | 0.0464 | 0.168 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.3 | 0.3294 | 1.761 | 0.3404 | 0.01977 | 0.08681 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 15.12 | 0.3596 | 2.015 | 0.4078 | 0.01039 | 0.06237 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 17.26 | 0.4005 | 2.138 | 0.4381 | 0.01694 | 0.0584 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.34 | 0.294 | 2.085 | 0.4188 | 0.03102 | 0.1058 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 17.68 | 0.4078 | 2.178 | 0.4514 | 0.03908 | 0.071 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 11.08 | 0.2876 | 2.171 | 0.4486 | 0.05941 | 0.1229 |
| 688566 | 吉贝尔 | CN | SW_UNKNOWN | 0.1116 | 19.43 | 0.4376 | 2.035 | 0.4119 | 0.01021 | 0.0485 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.147 | 2.15 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.253 | 3.258 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.346 | 2.351 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.053 | 4.065 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.609 | 3.621 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.122 | 1.127 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 9.082 | 9.12 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.397 | 2.408 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.227 | 2.238 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002275 | SKIP | spread_too_wide | 0.997 | 1.003 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.167 | 1.173 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.621 | 3.644 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 5.168 | 5.202 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.807 | 1.82 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002880 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.096 | 1.106 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.573 | 1.587 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.636 | 7.708 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.113 | 1.124 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.789 | 2.822 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.194 | 6.27 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.933 | 7.02 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.373 | 1.392 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 161.4 | 163.6 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 1.001 | 1.015 | 142 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.065 | 2.095 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.364 | 1.385 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.013 | 1.029 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.403 | 1.425 | 158 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.992 | 1.008 | 162 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.992 | 1.008 | 166 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.018 | 3.07 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.873 | 1.906 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.237 | 2.277 | 178 | normal | True | 0 | 0 | OK |  | True |
| 688566 | SKIP | spread_too_wide | 0.991 | 1.009 | 182 | normal | True | 0 | 0 | OK |  | True |
