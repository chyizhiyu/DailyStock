# DailyStock Funnel Dashboard

- As of: `2026-05-29`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7835 | - | 248.731 |
| step2_hard_filters | 7835 | 2772 | risk_screen: 1449, listing_age: 571, liquidity: 1000, market_cap: 1584, performance_floor: 459 | 0.858 |
| step3_financial_quality | 2772 | 260 | profitability: 2281, leverage: 42, cash_flow_quality: 105, growth: 84 | 0.072 |
| step4_valuation | 260 | 45 | missing_valuation_data: 29, pe_valuation_percentile: 115, pb_valuation_percentile: 63, dividend_yield: 8 | 0.291 |
| step5_futu_executor | 45 | 45 | spread_too_wide: 39 | 0.008 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 2774 | 0 |
| step2_hard_filters | 2548 | 2513 | 224 | 2550 |
| step3_financial_quality | 230 | 2318 | 30 | 194 |
| step4_valuation | 45 | 185 | 0 | 30 |
| step5_futu_executor | 45 | 39 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 1448 |
| step2_hard_filters | listing_age | 283 | 288 |
| step2_hard_filters | liquidity | 426 | 574 |
| step2_hard_filters | market_cap | 1364 | 220 |
| step2_hard_filters | performance_floor | 439 | 20 |
| step3_financial_quality | profitability | 2114 | 167 |
| step3_financial_quality | leverage | 34 | 8 |
| step3_financial_quality | cash_flow_quality | 98 | 7 |
| step3_financial_quality | growth | 72 | 12 |
| step4_valuation | missing_valuation_data | 26 | 3 |
| step4_valuation | pe_valuation_percentile | 90 | 25 |
| step4_valuation | pb_valuation_percentile | 61 | 2 |
| step4_valuation | dividend_yield | 8 | 0 |
| step5_futu_executor | spread_too_wide | 39 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 18 | 0.3155 | 2.9 | 0.4683 | 0.02899 | 0.07314 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10.29 | 0.1379 | 1.02 | 0.1034 | 0.03399 | 0.1792 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.18 | 0.2606 | 2.174 | 0.3097 | 0.05821 | 0.1255 |
| 000893 | 亚钾国际 | CN | C 制造业 | 0.1328 | 24.52 | 0.3885 | 2.986 | 0.4868 | 0.009311 | 0.055 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.85 | 0.2516 | 2.131 | 0.297 | 0.07402 | 0.2008 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 20.75 | 0.3103 | 3.792 | 0.4483 | 0.01703 | 0.076 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.62 | 0.2474 | 1.713 | 0.1771 | 0.02437 | 0.1384 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 15.8 | 0.3276 | 1.724 | 0.4138 | 0.03244 | 0.1897 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.88 | 0.268 | 2.684 | 0.4334 | 0.02609 | 0.0933 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 16.76 | 0.297 | 2.345 | 0.351 | 0.04053 | 0.1035 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 13.73 | 0.2669 | 1.785 | 0.1961 | 0.02648 | 0.07185 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 12.24 | 0.1724 | 2.204 | 0.3448 | 0.0331 | 0.1052 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 12.17 | 0.2537 | 2.754 | 0.4456 | 0.04338 | 0.1321 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 18.5 | 0.3214 | 2.357 | 0.3547 | 0.01974 | 0.05464 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 15.35 | 0.2838 | 2.015 | 0.2674 | 0.0124 | 0.05995 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 29.46 | 0.4366 | 2.892 | 0.4667 | 0.01458 | 0.06966 |
| 002831 | 裕同科技 | CN | C 制造业 | 0.1356 | 16.21 | 0.2902 | 2.963 | 0.4815 | 0.01623 | 0.07489 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.1 | 0.3177 | 2.596 | 0.4149 | 0.03077 | 0.08018 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 17.98 | 0.315 | 2.786 | 0.4503 | 0.03041 | 0.06532 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 18.92 | 0.4231 | 3.159 | 0.3974 | 0.01101 | 0.09552 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 16.5 | 0.2939 | 2.162 | 0.3055 | 0.01618 | 0.06362 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.524 | 0.3803 | 3.344 | 0.4402 | 0.03779 | 0.1327 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.75 | 0.2484 | 2.126 | 0.296 | 0.03303 | 0.1147 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 10.23 | 0.24 | 2.628 | 0.4223 | 0.00878 | 0.06883 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 15.33 | 0.2833 | 2.243 | 0.3261 | 0.01427 | 0.04216 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 17.67 | 0.3108 | 1.734 | 0.1829 | 0.01989 | 0.05399 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 17.67 | 0.3962 | 2.107 | 0.4129 | 0.05088 | 0.07436 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.75 | 0.3503 | 2.104 | 0.4115 | 0.04012 | 0.1259 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 21.42 | 0.45 | 2.008 | 0.3879 | 0.02147 | 0.07631 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.44 | 0.2762 | 1.427 | 0.2312 | 0.02276 | 0.08614 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.98 | 0.3387 | 1.482 | 0.2456 | 0.03843 | 0.1053 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.76 | 0.3137 | 1.431 | 0.2322 | 0.06203 | 0.1626 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 11.24 | 0.2873 | 1.19 | 0.1525 | 0.02961 | 0.1542 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 17.67 | 0.3962 | 2.499 | 0.4944 | 0.03954 | 0.05665 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.09 | 0.3211 | 1.618 | 0.2929 | 0.02589 | 0.1272 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 13.79 | 0.3346 | 2.013 | 0.3888 | 0.01401 | 0.1241 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.27 | 0.3897 | 2.189 | 0.4296 | 0.03002 | 0.05973 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 18.43 | 0.4082 | 2.211 | 0.4361 | 0.02101 | 0.0706 |
| 601567 | 三星电气 | CN | SW_UNKNOWN | 0.1059 | 17.12 | 0.3846 | 1.852 | 0.3517 | 0.02021 | 0.0818 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.949 | 0.2702 | 1.134 | 0.1376 | 0.0477 | 0.1657 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 14.83 | 0.3526 | 1.97 | 0.3795 | 0.01527 | 0.07783 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 17.47 | 0.3934 | 2.163 | 0.424 | 0.0166 | 0.05769 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.04 | 0.2836 | 1.937 | 0.3689 | 0.03102 | 0.1086 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.35 | 0.3763 | 1.907 | 0.3605 | 0.03205 | 0.07678 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 12.99 | 0.3184 | 2.118 | 0.4161 | 0.04829 | 0.1182 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 3.128 | 3.131 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.063 | 2.066 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000893 | WATCH | passed_depth_scan | 4.144 | 4.154 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 6.149 | 6.167 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 3.976 | 3.989 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 4.731 | 4.749 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.409 | 9.449 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.094 | 1.099 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.085 | 1.09 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.727 | 8.775 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.112 | 1.118 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 1.968 | 1.98 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.841 | 3.866 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002831 | SKIP | spread_too_wide | 3.641 | 3.669 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.316 | 1.327 | 82 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.995 | 1.005 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.14 | 1.152 | 102 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.201 | 2.225 | 106 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 2.106 | 2.13 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.794 | 2.827 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.624 | 9.743 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.718 | 1.74 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.381 | 6.465 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.738 | 2.775 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.291 | 3.337 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 8.05 | 8.165 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.58 | 1.603 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 167.2 | 169.8 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.997 | 1.013 | 154 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 105.5 | 107.2 | 158 | normal | True | 0 | 0 | OK |  | True |
| 601567 | SKIP | spread_too_wide | 2.148 | 2.183 | 162 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.027 | 1.044 | 166 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.563 | 1.59 | 170 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.991 | 1.009 | 174 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 2.941 | 2.994 | 178 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.732 | 1.763 | 182 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.326 | 2.37 | 186 | normal | True | 0 | 0 | OK |  | True |
