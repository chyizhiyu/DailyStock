# DailyStock Funnel Dashboard

- As of: `2026-10-23`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7935 | - | 285.013 |
| step2_hard_filters | 7935 | 2523 | risk_screen: 1500, listing_age: 507, liquidity: 887, market_cap: 2132, performance_floor: 386 | 0.292 |
| step3_financial_quality | 2523 | 222 | profitability: 2064, leverage: 67, cash_flow_quality: 95, growth: 75 | 0.031 |
| step4_valuation | 222 | 39 | missing_valuation_data: 4, pe_valuation_percentile: 94, pb_valuation_percentile: 69, dividend_yield: 16 | 0.105 |
| step5_futu_executor | 39 | 39 | spread_too_wide: 33 | 0.003 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5121 | 0 | 2814 | 0 |
| step2_hard_filters | 2414 | 2707 | 109 | 2705 |
| step3_financial_quality | 205 | 2209 | 17 | 92 |
| step4_valuation | 39 | 166 | 0 | 17 |
| step5_futu_executor | 39 | 33 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 2 | 1498 |
| step2_hard_filters | listing_age | 207 | 300 |
| step2_hard_filters | liquidity | 284 | 603 |
| step2_hard_filters | market_cap | 1835 | 297 |
| step2_hard_filters | performance_floor | 379 | 7 |
| step3_financial_quality | profitability | 1986 | 78 |
| step3_financial_quality | leverage | 65 | 2 |
| step3_financial_quality | cash_flow_quality | 91 | 4 |
| step3_financial_quality | growth | 67 | 8 |
| step4_valuation | missing_valuation_data | 2 | 2 |
| step4_valuation | pe_valuation_percentile | 82 | 12 |
| step4_valuation | pb_valuation_percentile | 66 | 3 |
| step4_valuation | dividend_yield | 16 | 0 |
| step5_futu_executor | spread_too_wide | 33 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.27 | 0.2 | 1.029 | 0.2667 | 0.03439 | 0.1795 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 19.09 | 0.36 | 1.9 | 0.31 | 0.008703 | 0.08486 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 10.44 | 0.2167 | 1.412 | 0.4667 | 0.02561 | 0.2406 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.61 | 0.2507 | 2.166 | 0.392 | 0.07065 | 0.2244 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.64 | 0.2667 | 1.428 | 0.4833 | 0.03755 | 0.2371 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.33 | 0.2712 | 1.627 | 0.2123 | 0.02778 | 0.08002 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.53 | 0.1724 | 1.58 | 0.2759 | 0.0331 | 0.1056 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 16.1 | 0.3163 | 2.255 | 0.4162 | 0.009532 | 0.05595 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 12.46 | 0.2717 | 1.624 | 0.2112 | 0.01213 | 0.0739 |
| 002545 | 东方铁塔 | CN | C 制造业 | 0.1297 | 13.11 | 0.279 | 1.525 | 0.1755 | 0.008045 | 0.151 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 21.7 | 0.4473 | 2.304 | 0.2068 | 0.03227 | 0.07699 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 23.43 | 0.4262 | 2.363 | 0.4419 | 0.01458 | 0.08759 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 11.99 | 0.2659 | 2.399 | 0.4519 | 0.05394 | 0.08426 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 22.34 | 0.3788 | 2.156 | 0.3788 | 0.008721 | 0.08764 |
| 002970 | 锐明技术 | CN | I 信息技术 | 0.2029 | 17.67 | 0.4219 | 3.181 | 0.4641 | 0.008247 | 0.05682 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.67 | 0.4388 | 2.008 | 0.1308 | 0.007937 | 0.07218 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 17.92 | 0.4262 | 3.095 | 0.4473 | 0.01185 | 0.1009 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 22.27 | 0.4115 | 2.319 | 0.433 | 0.0125 | 0.03869 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.05 | 0.2444 | 1.361 | 0.1251 | 0.02034 | 0.08917 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 14.71 | 0.2995 | 1.945 | 0.3253 | 0.01799 | 0.07139 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 9.14 | 0.2401 | 2.052 | 0.3615 | 0.02579 | 0.1699 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 10.97 | 0.2554 | 2.061 | 0.3647 | 0.03303 | 0.1228 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 10.14 | 0.2459 | 2.559 | 0.4866 | 0.03286 | 0.07688 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 9.005 | 0.2386 | 2.325 | 0.4356 | 0.01133 | 0.0778 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 9.729 | 0.2428 | 1.415 | 0.145 | 0.008119 | 0.06644 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 22.26 | 0.4966 | 2.092 | 0.4607 | 0.01446 | 0.07344 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 14.57 | 0.3637 | 1.612 | 0.3274 | 0.01881 | 0.101 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.73 | 0.331 | 1.544 | 0.3076 | 0.04355 | 0.1629 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.01 | 0.3756 | 2.197 | 0.4846 | 0.04277 | 0.06668 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 11.16 | 0.3007 | 1.404 | 0.2589 | 0.02557 | 0.1384 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.84 | 0.3122 | 1.495 | 0.2906 | 0.02672 | 0.1407 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.12 | 0.3393 | 1.872 | 0.4078 | 0.02338 | 0.1304 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 11.72 | 0.3103 | 1.305 | 0.2202 | 0.02239 | 0.09007 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 13.93 | 0.3526 | 1.503 | 0.2947 | 0.009791 | 0.1005 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 12.98 | 0.3366 | 1.719 | 0.3549 | 0.01977 | 0.08895 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 14.55 | 0.3618 | 1.932 | 0.4211 | 0.01039 | 0.06502 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 9.679 | 0.2745 | 1.779 | 0.3784 | 0.03102 | 0.124 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.48 | 0.2878 | 2.052 | 0.4497 | 0.05941 | 0.13 |
| 688566 | 吉贝尔 | CN | SW_UNKNOWN | 0.1116 | 20.3 | 0.4694 | 2.127 | 0.4667 | 0.009673 | 0.04642 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.061 | 2.063 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.205 | 3.21 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.139 | 2.143 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 001286 | WATCH | passed_depth_scan | 3.786 | 3.796 | 26 | normal | True | 0 | 0 | OK |  | True |
| 002020 | WATCH | passed_depth_scan | 0.999 | 1.002 | 30 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.705 | 8.735 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.069 | 2.077 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.119 | 3.133 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002545 | SKIP | spread_too_wide | 1.578 | 1.585 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 3.867 | 3.887 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.003 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.997 | 1.003 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.083 | 1.089 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002970 | SKIP | spread_too_wide | 0.997 | 1.003 | 66 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.576 | 1.587 | 70 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.044 | 1.052 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.009 | 1.019 | 102 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 1.397 | 1.412 | 106 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 10.01 | 10.12 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.657 | 6.733 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.736 | 2.768 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.846 | 6.93 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.994 | 1.006 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.43 | 1.448 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 159.2 | 161.3 | 134 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 6.118 | 6.203 | 138 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 1.75 | 1.775 | 142 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.37 | 1.39 | 146 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.993 | 1.008 | 150 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.577 | 2.617 | 154 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.117 | 2.15 | 158 | normal | True | 0 | 0 | OK |  | True |
| 688566 | SKIP | spread_too_wide | 0.992 | 1.008 | 162 | normal | True | 0 | 0 | OK |  | True |
