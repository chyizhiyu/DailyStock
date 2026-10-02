# DailyStock Funnel Dashboard

- As of: `2026-10-02`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7939 | - | 417.435 |
| step2_hard_filters | 7939 | 2559 | risk_screen: 1485, listing_age: 435, liquidity: 1444, market_cap: 1613, performance_floor: 403 | 0.833 |
| step3_financial_quality | 2559 | 248 | profitability: 2101, leverage: 33, cash_flow_quality: 101, growth: 76 | 0.070 |
| step4_valuation | 248 | 48 | missing_valuation_data: 4, pe_valuation_percentile: 105, pb_valuation_percentile: 70, dividend_yield: 21 | 0.286 |
| step5_futu_executor | 48 | 48 | spread_too_wide: 42 | 0.008 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5122 | 0 | 2817 | 0 |
| step2_hard_filters | 2477 | 2645 | 82 | 2735 |
| step3_financial_quality | 233 | 2244 | 15 | 67 |
| step4_valuation | 48 | 185 | 0 | 15 |
| step5_futu_executor | 48 | 42 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1484 |
| step2_hard_filters | listing_age | 137 | 298 |
| step2_hard_filters | liquidity | 768 | 676 |
| step2_hard_filters | market_cap | 1343 | 270 |
| step2_hard_filters | performance_floor | 396 | 7 |
| step3_financial_quality | profitability | 2043 | 58 |
| step3_financial_quality | leverage | 31 | 2 |
| step3_financial_quality | cash_flow_quality | 99 | 2 |
| step3_financial_quality | growth | 71 | 5 |
| step4_valuation | missing_valuation_data | 2 | 2 |
| step4_valuation | pe_valuation_percentile | 93 | 12 |
| step4_valuation | pb_valuation_percentile | 69 | 1 |
| step4_valuation | dividend_yield | 21 | 0 |
| step5_futu_executor | spread_too_wide | 42 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.49 | 0.2069 | 1.051 | 0.2414 | 0.03439 | 0.1757 |
| 000729 | 燕京啤酒 | CN | C 制造业 | 0.1107 | 18.46 | 0.3358 | 1.837 | 0.2401 | 0.009091 | 0.08779 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.16 | 0.2414 | 1.51 | 0.4828 | 0.02561 | 0.225 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.57 | 0.2748 | 2.575 | 0.4477 | 0.05821 | 0.1219 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.74 | 0.257 | 1.763 | 0.2249 | 0.01716 | 0.1369 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 11.81 | 0.2586 | 1.335 | 0.4138 | 0.03755 | 0.2537 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 12.86 | 0.2669 | 1.698 | 0.2039 | 0.02778 | 0.07671 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 11.53 | 0.1667 | 1.651 | 0.2667 | 0.0331 | 0.1056 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 17.08 | 0.3158 | 2.392 | 0.4136 | 0.009532 | 0.05275 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.2 | 0.2501 | 2.68 | 0.4719 | 0.01781 | 0.1434 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 21.65 | 0.3847 | 2.744 | 0.4887 | 0.01974 | 0.04684 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 12.77 | 0.2654 | 1.665 | 0.1923 | 0.01118 | 0.07205 |
| 002558 | 巨人网络 | CN | I 信息技术 | 0.1245 | 23.94 | 0.4622 | 2.542 | 0.3025 | 0.03227 | 0.06981 |
| 002611 | 东方精工 | CN | C 制造业 | 0.1339 | 22.92 | 0.4036 | 1.796 | 0.2328 | 0.01238 | 0.05137 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 25.54 | 0.4346 | 2.576 | 0.4482 | 0.01458 | 0.08034 |
| 002880 | 卫光生物 | CN | C 制造业 | 0.1067 | 20.47 | 0.3642 | 2.091 | 0.3269 | 0.007773 | 0.0522 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 23.11 | 0.3731 | 2.291 | 0.3134 | 0.008721 | 0.08474 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 19.3 | 0.4328 | 1.971 | 0.1303 | 0.007937 | 0.07355 |
| 300015 | 爱尔眼科 | CN | Q 卫生 | 0.1497 | 22.83 | 0.3571 | 3.224 | 0.5 | 0.0111 | 0.08048 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 17.75 | 0.4202 | 3.066 | 0.4622 | 0.01185 | 0.1018 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.63 | 0.3836 | 2.252 | 0.3773 | 0.0125 | 0.03983 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.04 | 0.2422 | 1.359 | 0.1051 | 0.02034 | 0.08933 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 9.551 | 0.2396 | 2.144 | 0.3405 | 0.02579 | 0.1626 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.53 | 0.2533 | 2.166 | 0.35 | 0.03303 | 0.1168 |
| 301004 | 嘉益股份 | CN | C 制造业 | 0.2303 | 11.64 | 0.2559 | 2.708 | 0.4766 | 0.02312 | 0.1583 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.46 | 0.2433 | 2.687 | 0.4735 | 0.01133 | 0.06731 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 17.23 | 0.4065 | 2.22 | 0.4607 | 0.05596 | 0.07628 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 13.97 | 0.3463 | 2.113 | 0.4327 | 0.03634 | 0.133 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 14.26 | 0.3519 | 1.577 | 0.2921 | 0.01923 | 0.1032 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.56 | 0.3206 | 1.523 | 0.2719 | 0.04779 | 0.1652 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 14.87 | 0.362 | 2.177 | 0.446 | 0.04277 | 0.0673 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 12.15 | 0.311 | 1.528 | 0.2733 | 0.02557 | 0.1271 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.25 | 0.2958 | 1.42 | 0.2444 | 0.02672 | 0.1482 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13 | 0.3266 | 1.856 | 0.3702 | 0.02443 | 0.1316 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 16.68 | 0.396 | 2.186 | 0.4492 | 0.02841 | 0.06185 |
| 601083 | 锦江航运 | CN | SW_UNKNOWN | 0.1663 | 10.9 | 0.2908 | 1.77 | 0.3445 | 0.01842 | 0.1517 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 17.97 | 0.4212 | 2.299 | 0.4823 | 0.0205 | 0.0724 |
| 601298 | 青岛港 | CN | SW_UNKNOWN | 0.1195 | 12.42 | 0.3183 | 1.383 | 0.2278 | 0.01391 | 0.08497 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 15.19 | 0.3721 | 1.638 | 0.3096 | 0.009791 | 0.09222 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 10.75 | 0.288 | 1.27 | 0.1911 | 0.0464 | 0.1533 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 12.8 | 0.3252 | 1.695 | 0.3229 | 0.01977 | 0.0902 |
| 603100 | 川仪股份 | CN | SW_UNKNOWN | 0.1413 | 14.52 | 0.3578 | 1.934 | 0.3932 | 0.01039 | 0.06496 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 16.14 | 0.3881 | 1.999 | 0.4093 | 0.01694 | 0.06244 |
| 603202 | 天有为 | CN | SW_UNKNOWN | 0.1623 | 8.156 | 0.2568 | 1.207 | 0.1732 | 0.009747 | 0.1301 |
| 603402 | 陕西旅游 | CN | SW_UNKNOWN | 0.2774 | 9.124 | 0.2646 | 2.064 | 0.4217 | 0.02117 | 0.08706 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 10.24 | 0.2774 | 1.883 | 0.3771 | 0.03102 | 0.1172 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 18.23 | 0.424 | 2.245 | 0.4667 | 0.03908 | 0.0689 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.82 | 0.2885 | 2.12 | 0.435 | 0.05941 | 0.1259 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.106 | 2.108 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000729 | WATCH | passed_depth_scan | 3.098 | 3.103 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.288 | 2.292 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.021 | 4.031 | 26 | normal | True | 0 | 0 | OK |  | True |
| 001286 | WATCH | passed_depth_scan | 3.538 | 3.549 | 30 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.017 | 1.02 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.706 | 8.739 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.195 | 2.204 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.025 | 1.03 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.297 | 2.308 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.197 | 3.215 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002558 | SKIP | spread_too_wide | 4.264 | 4.289 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002611 | SKIP | spread_too_wide | 1.696 | 1.707 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.003 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002880 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.119 | 1.127 | 74 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.546 | 1.558 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300015 | SKIP | spread_too_wide | 7.391 | 7.451 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.014 | 1.023 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 301004 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.166 | 1.178 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 2.053 | 2.077 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.646 | 2.678 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.509 | 6.589 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.696 | 2.731 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 6.779 | 6.868 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.993 | 1.007 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.357 | 1.376 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 157.7 | 160 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.993 | 1.007 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601083 | SKIP | spread_too_wide | 1.625 | 1.649 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 102.9 | 104.5 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601298 | SKIP | spread_too_wide | 6.478 | 6.582 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 1.905 | 1.936 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.11 | 1.129 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.349 | 1.372 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603100 | SKIP | spread_too_wide | 0.991 | 1.009 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603202 | SKIP | spread_too_wide | 0.991 | 1.009 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603402 | SKIP | spread_too_wide | 0.991 | 1.009 | 186 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.723 | 2.775 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.929 | 1.966 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.182 | 2.226 | 198 | normal | True | 0 | 0 | OK |  | True |
