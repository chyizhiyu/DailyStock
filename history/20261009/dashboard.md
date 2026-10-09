# DailyStock Funnel Dashboard

- As of: `2026-10-09`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7942 | - | 417.786 |
| step2_hard_filters | 7942 | 2595 | risk_screen: 1485, listing_age: 517, liquidity: 959, market_cap: 1982, performance_floor: 404 | 0.438 |
| step3_financial_quality | 2595 | 246 | profitability: 2136, leverage: 32, cash_flow_quality: 101, growth: 80 | 0.047 |
| step4_valuation | 246 | 51 | missing_valuation_data: 3, pe_valuation_percentile: 103, pb_valuation_percentile: 70, dividend_yield: 19 | 0.184 |
| step5_futu_executor | 51 | 51 | spread_too_wide: 45 | 0.005 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5121 | 0 | 2821 | 0 |
| step2_hard_filters | 2499 | 2622 | 96 | 2725 |
| step3_financial_quality | 232 | 2267 | 14 | 82 |
| step4_valuation | 51 | 181 | 0 | 14 |
| step5_futu_executor | 51 | 45 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 2 | 1483 |
| step2_hard_filters | listing_age | 214 | 303 |
| step2_hard_filters | liquidity | 347 | 612 |
| step2_hard_filters | market_cap | 1666 | 316 |
| step2_hard_filters | performance_floor | 393 | 11 |
| step3_financial_quality | profitability | 2066 | 70 |
| step3_financial_quality | leverage | 30 | 2 |
| step3_financial_quality | cash_flow_quality | 98 | 3 |
| step3_financial_quality | growth | 73 | 7 |
| step4_valuation | missing_valuation_data | 1 | 2 |
| step4_valuation | pe_valuation_percentile | 92 | 11 |
| step4_valuation | pb_valuation_percentile | 69 | 1 |
| step4_valuation | dividend_yield | 19 | 0 |
| step5_futu_executor | spread_too_wide | 45 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.58 | 0.2 | 1.06 | 0.2333 | 0.03439 | 0.1742 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 19.13 | 0.3452 | 1.904 | 0.2601 | 0.01675 | 0.08471 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.4 | 0.2167 | 1.542 | 0.5 | 0.02561 | 0.2203 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.82 | 0.2769 | 2.622 | 0.4661 | 0.05821 | 0.1197 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.62 | 0.2444 | 2.17 | 0.3494 | 0.07065 | 0.224 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 12.05 | 0.2606 | 1.809 | 0.2338 | 0.02437 | 0.1335 |
| 001216 | 华瓷股份 | CN | C 制造业 | 0.1235 | 25.85 | 0.443 | 2.649 | 0.4729 | 0.02395 | 0.05252 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.43 | 0.25 | 1.404 | 0.4333 | 0.03755 | 0.2412 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.9 | 0.2675 | 1.703 | 0.2007 | 0.02778 | 0.07645 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.9 | 0.1724 | 1.704 | 0.2759 | 0.0331 | 0.1023 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 17 | 0.3153 | 2.382 | 0.4115 | 0.009532 | 0.05298 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.47 | 0.2533 | 2.746 | 0.4929 | 0.01781 | 0.14 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 20.7 | 0.3715 | 2.624 | 0.4666 | 0.01974 | 0.04897 |
| 002275 | 桂林三金 | CN | C 制造业 | 0.1389 | 16.69 | 0.3116 | 2.223 | 0.3715 | 0.02244 | 0.09758 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.4 | 0.3079 | 2.195 | 0.3594 | 0.01153 | 0.06521 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 12.88 | 0.2669 | 1.679 | 0.1923 | 0.01108 | 0.07144 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 24.28 | 0.4599 | 2.578 | 0.3038 | 0.03227 | 0.06883 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 22.39 | 0.3967 | 1.755 | 0.2239 | 0.01238 | 0.05257 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 24.83 | 0.4293 | 2.504 | 0.4414 | 0.01458 | 0.08265 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 22.68 | 0.3636 | 2.249 | 0.2879 | 0.008721 | 0.08632 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.33 | 0.4262 | 1.973 | 0.1308 | 0.007937 | 0.07345 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 22.6 | 0.3333 | 3.191 | 0.4667 | 0.0111 | 0.0813 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 18.08 | 0.4177 | 3.124 | 0.4557 | 0.01185 | 0.09993 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.53 | 0.3826 | 2.242 | 0.3799 | 0.0125 | 0.04001 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.18 | 0.2433 | 1.378 | 0.1088 | 0.02034 | 0.08805 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 14.72 | 0.2906 | 1.946 | 0.2727 | 0.01626 | 0.07134 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 9.765 | 0.2428 | 2.192 | 0.3584 | 0.02579 | 0.1591 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.7 | 0.2554 | 2.198 | 0.36 | 0.03303 | 0.1152 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 10.98 | 0.2491 | 2.77 | 0.4997 | 0.03286 | 0.07103 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 9.756 | 0.2422 | 2.506 | 0.4419 | 0.01133 | 0.07216 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 10.75 | 0.2454 | 1.564 | 0.1576 | 0.01274 | 0.06013 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 17.18 | 0.4047 | 2.214 | 0.4571 | 0.05596 | 0.07646 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.61 | 0.356 | 2.21 | 0.4561 | 0.03634 | 0.1272 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 14.79 | 0.3601 | 1.636 | 0.3091 | 0.01853 | 0.0995 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 13.36 | 0.3303 | 1.62 | 0.3055 | 0.06203 | 0.1553 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.23 | 0.3684 | 2.228 | 0.4603 | 0.04277 | 0.06574 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 11.78 | 0.3027 | 1.482 | 0.2549 | 0.02557 | 0.1311 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.02 | 0.2917 | 1.392 | 0.2278 | 0.02672 | 0.1512 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.16 | 0.3261 | 1.878 | 0.3739 | 0.01689 | 0.13 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17 | 0.4006 | 2.228 | 0.4603 | 0.02841 | 0.0607 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.2 | 0.4231 | 2.328 | 0.4906 | 0.02025 | 0.0715 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 12.39 | 0.3151 | 1.381 | 0.2232 | 0.01393 | 0.08514 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 14.84 | 0.3606 | 1.601 | 0.2954 | 0.009791 | 0.09436 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.93 | 0.2894 | 1.291 | 0.1929 | 0.0464 | 0.1508 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 13.54 | 0.3353 | 1.793 | 0.3477 | 0.01977 | 0.08529 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 14.79 | 0.3597 | 1.97 | 0.3987 | 0.01039 | 0.06377 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.21 | 0.3836 | 2.008 | 0.4088 | 0.01694 | 0.06219 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 10 | 0.2729 | 1.838 | 0.3606 | 0.03102 | 0.1201 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 17.89 | 0.4175 | 2.204 | 0.4548 | 0.03908 | 0.07019 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.7 | 0.283 | 2.095 | 0.4272 | 0.05941 | 0.1274 |
| 688566 | 吉贝尔 | CN | SW_UNKNOWN | 0.1116 | 20.96 | 0.4649 | 2.195 | 0.4534 | 0.0102 | 0.04496 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.123 | 2.126 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.211 | 3.215 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.337 | 2.341 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.124 | 4.137 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001216 | SKIP | spread_too_wide | 0.998 | 1.002 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.72 | 3.735 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.02 | 1.024 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.984 | 9.025 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.184 | 2.195 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.05 | 1.055 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.196 | 2.209 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002275 | SKIP | spread_too_wide | 0.997 | 1.003 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.115 | 1.123 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.222 | 3.245 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.321 | 4.353 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.656 | 1.669 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.098 | 1.107 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.547 | 1.561 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.312 | 7.381 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.009 | 1.019 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.045 | 1.058 | 122 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.086 | 1.1 | 126 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 1.542 | 1.562 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 2.046 | 2.074 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.764 | 2.803 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.748 | 6.844 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.865 | 2.908 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.934 | 7.038 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.992 | 1.008 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.328 | 1.35 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 159.4 | 162 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.992 | 1.008 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 104.1 | 105.9 | 170 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 6.46 | 6.574 | 174 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 1.861 | 1.894 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.127 | 1.148 | 182 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.425 | 1.452 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.991 | 1.01 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.99 | 1.01 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.657 | 2.71 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.892 | 1.931 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.156 | 2.201 | 206 | normal | True | 0 | 0 | OK |  | True |
| 688566 | SKIP | spread_too_wide | 0.99 | 1.01 | 210 | normal | True | 0 | 0 | OK |  | True |
