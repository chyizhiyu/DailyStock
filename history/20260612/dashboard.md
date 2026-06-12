# DailyStock Funnel Dashboard

- As of: `2026-06-12`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 9729 | - | 544.137 |
| step2_hard_filters | 9729 | 2767 | risk_screen: 2955, listing_age: 557, liquidity: 1305, market_cap: 1683, missing_financials: 24, performance_floor: 438 | 0.596 |
| step3_financial_quality | 2767 | 266 | profitability: 2270, leverage: 45, cash_flow_quality: 104, growth: 82 | 0.065 |
| step4_valuation | 266 | 42 | missing_valuation_data: 20, pe_valuation_percentile: 131, pb_valuation_percentile: 68, dividend_yield: 5 | 0.258 |
| step5_futu_executor | 42 | 42 | spread_too_wide: 36 | 0.006 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5061 | 0 | 4668 | 0 |
| step2_hard_filters | 2537 | 2524 | 230 | 4438 |
| step3_financial_quality | 234 | 2303 | 32 | 198 |
| step4_valuation | 41 | 193 | 1 | 31 |
| step5_futu_executor | 41 | 35 | 1 | 1 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 1 | 2954 |
| step2_hard_filters | listing_age | 267 | 290 |
| step2_hard_filters | liquidity | 378 | 927 |
| step2_hard_filters | market_cap | 1460 | 223 |
| step2_hard_filters | missing_financials | 0 | 24 |
| step2_hard_filters | performance_floor | 418 | 20 |
| step3_financial_quality | profitability | 2096 | 174 |
| step3_financial_quality | leverage | 36 | 9 |
| step3_financial_quality | cash_flow_quality | 98 | 6 |
| step3_financial_quality | growth | 73 | 9 |
| step4_valuation | missing_valuation_data | 17 | 3 |
| step4_valuation | pe_valuation_percentile | 111 | 20 |
| step4_valuation | pb_valuation_percentile | 60 | 8 |
| step4_valuation | dividend_yield | 5 | 0 |
| step5_futu_executor | spread_too_wide | 35 | 1 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 9.94 | 0.2069 | 1.04 | 0.2069 | 0.03346 | 0.1764 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 8.1 | 0.2378 | 2.51 | 0.3975 | 0.05821 | 0.1258 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 14.62 | 0.2807 | 2.18 | 0.3145 | 0.07246 | 0.1966 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 10.5 | 0.2414 | 3.6 | 0.4483 | 0.01703 | 0.07996 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 9.61 | 0.2452 | 1.86 | 0.2204 | 0.02437 | 0.1333 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.91 | 0.3793 | 1.67 | 0.4655 | 0.03352 | 0.196 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 12.65 | 0.2664 | 2.83 | 0.4656 | 0.02609 | 0.09513 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 28.9 | 0.4397 | 2.56 | 0.4117 | 0.04053 | 0.1054 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 16.17 | 0.2986 | 1.84 | 0.2141 | 0.02778 | 0.07312 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 10.24 | 0.2069 | 1.74 | 0.2414 | 0.0331 | 0.1123 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 29.04 | 0.4408 | 2.94 | 0.4852 | 0.008598 | 0.04318 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 15.55 | 0.2918 | 2.48 | 0.3885 | 0.01974 | 0.05461 |
| 002275 | 桂林三金 | CN | C 制造业 | 0.1389 | 15.07 | 0.2838 | 2.38 | 0.3615 | 0.02244 | 0.09445 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 12.69 | 0.268 | 2.43 | 0.3768 | 0.03077 | 0.08438 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 27.88 | 0.4292 | 2.63 | 0.4286 | 0.01431 | 0.03409 |
| 300286 | 安科瑞 | CN | C 制造业 | 0.1025 | 33.14 | 0.4789 | 3.01 | 0.5 | 0.01405 | 0.03344 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 16.93 | 0.3103 | 1.58 | 0.1506 | 0.02034 | 0.07858 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 24.03 | 0.3869 | 2.23 | 0.3256 | 0.01391 | 0.06393 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 23.26 | 0.3784 | 2.15 | 0.3066 | 0.03303 | 0.1226 |
| 301004 | 嘉益股份 | CN | C 制造业 | 0.2303 | 21.43 | 0.3626 | 2.93 | 0.4831 | 0.01747 | 0.1541 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 16.88 | 0.3092 | 2.64 | 0.4313 | 0.00878 | 0.07023 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 10.25 | 0.25 | 2.27 | 0.3346 | 0.01274 | 0.04286 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 29.46 | 0.4456 | 1.88 | 0.2278 | 0.01989 | 0.05159 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 16.3 | 0.4113 | 1.98 | 0.3863 | 0.0541 | 0.07905 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 13.11 | 0.3483 | 2.11 | 0.4182 | 0.0401 | 0.1259 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 11.01 | 0.3089 | 1.99 | 0.3886 | 0.02171 | 0.07718 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 9.19 | 0.283 | 1.47 | 0.2506 | 0.02207 | 0.08353 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 11.56 | 0.3214 | 1.46 | 0.2469 | 0.03907 | 0.107 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 7.54 | 0.2645 | 1.66 | 0.3062 | 0.06203 | 0.1566 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 12.42 | 0.339 | 1.16 | 0.1491 | 0.0304 | 0.1583 |
| 600897 | 厦门空港 | CN | SW_UNKNOWN | 0.1113 | 14.37 | 0.3733 | 1.36 | 0.2103 | 0.02347 | 0.1186 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 17.34 | 0.4224 | 1.61 | 0.2932 | 0.01877 | 0.1334 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 10.13 | 0.2974 | 1.89 | 0.3687 | 0.01489 | 0.1318 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 12.08 | 0.3321 | 2.24 | 0.4442 | 0.02937 | 0.05845 |
| 601811 | 新华文轩 | CN | SW_UNKNOWN | 0.1048 | 14.51 | 0.3752 | 0.99 | 0.1019 | 0.03331 | 0.101 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 8.61 | 0.277 | 1.13 | 0.1399 | 0.04774 | 0.1658 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 21.44 | 0.4766 | 1.76 | 0.3353 | 0.01706 | 0.08696 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 18.91 | 0.4465 | 2.33 | 0.4669 | 0.03102 | 0.09691 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 18.89 | 0.446 | 2.12 | 0.4201 | 0.03908 | 0.07511 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 11.23 | 0.3117 | 2.01 | 0.3956 | 0.05087 | 0.1245 |
| 605183 | 确成股份 | CN | SW_UNKNOWN | 0.1407 | 19.31 | 0.4502 | 1.69 | 0.3154 | 0.02712 | 0.09337 |
| 03933 | 联邦制药 | HK | 药品及生物科技 | 0.1313 | 7.48 | 0.4167 | 0.9 | 0.3208 | 0.06603 | 0.217 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000598 | WATCH | passed_depth_scan | 2.097 | 2.099 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 5.846 | 5.859 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 4.13 | 4.141 | 26 | normal | True | 0 | 0 | OK |  | True |
| 001286 | WATCH | passed_depth_scan | 4.579 | 4.593 | 30 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.232 | 9.264 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.074 | 1.078 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.066 | 1.071 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 8.177 | 8.215 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.68 | 2.693 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 1.969 | 1.98 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002275 | SKIP | spread_too_wide | 0.997 | 1.003 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.997 | 1.003 | 62 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.186 | 1.194 | 66 | normal | True | 0 | 0 | OK |  | True |
| 300286 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 301004 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 1.118 | 1.128 | 90 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.167 | 2.187 | 94 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.995 | 1.005 | 98 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.982 | 2.003 | 102 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.797 | 2.827 | 106 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.521 | 9.627 | 110 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.773 | 1.793 | 114 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.28 | 6.355 | 118 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.845 | 2.88 | 122 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 3.207 | 3.248 | 126 | normal | True | 0 | 0 | OK |  | True |
| 600897 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.508 | 1.529 | 134 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 157.5 | 159.7 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 1.02 | 1.034 | 142 | normal | True | 0 | 0 | OK |  | True |
| 601811 | SKIP | spread_too_wide | 1.482 | 1.504 | 146 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 1.027 | 1.042 | 150 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.4 | 1.422 | 154 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.298 | 3.351 | 158 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.772 | 1.801 | 162 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 2.21 | 2.247 | 166 | normal | True | 0 | 0 | OK |  | True |
| 605183 | SKIP | spread_too_wide | 0.992 | 1.008 | 170 | normal | True | 0 | 0 | OK |  | True |
| 03933 | SKIP | spread_too_wide | 1.713 | 1.743 | 174 | normal | True | 0 | 0 | OK |  | True |
