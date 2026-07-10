# DailyStock Funnel Dashboard

- As of: `2026-07-10`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7935 | - | 425.948 |
| step2_hard_filters | 7935 | 2641 | risk_screen: 1481, listing_age: 591, liquidity: 973, market_cap: 1833, performance_floor: 416 | 0.776 |
| step3_financial_quality | 2641 | 256 | profitability: 2168, leverage: 42, cash_flow_quality: 99, growth: 76 | 0.070 |
| step4_valuation | 256 | 50 | missing_valuation_data: 8, pe_valuation_percentile: 123, pb_valuation_percentile: 66, dividend_yield: 9 | 0.289 |
| step5_futu_executor | 50 | 50 | spread_too_wide: 44 | 0.009 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5129 | 0 | 2806 | 0 |
| step2_hard_filters | 2437 | 2692 | 204 | 2602 |
| step3_financial_quality | 231 | 2206 | 25 | 179 |
| step4_valuation | 50 | 181 | 0 | 25 |
| step5_futu_executor | 50 | 44 | 0 | 0 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 1478 |
| step2_hard_filters | listing_age | 294 | 297 |
| step2_hard_filters | liquidity | 381 | 592 |
| step2_hard_filters | market_cap | 1615 | 218 |
| step2_hard_filters | performance_floor | 399 | 17 |
| step3_financial_quality | profitability | 2007 | 161 |
| step3_financial_quality | leverage | 34 | 8 |
| step3_financial_quality | cash_flow_quality | 96 | 3 |
| step3_financial_quality | growth | 69 | 7 |
| step4_valuation | missing_valuation_data | 6 | 2 |
| step4_valuation | pe_valuation_percentile | 103 | 20 |
| step4_valuation | pb_valuation_percentile | 63 | 3 |
| step4_valuation | dividend_yield | 9 | 0 |
| step5_futu_executor | spread_too_wide | 44 | 0 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 17.33 | 0.3207 | 2.774 | 0.4929 | 0.02899 | 0.07647 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 10 | 0.2241 | 0.992 | 0.2414 | 0.02517 | 0.1843 |
| 000791 | 甘肃能源 | CN | D 水电煤气 | 0.144 | 11.51 | 0.2414 | 1.518 | 0.5 | 0.02561 | 0.2182 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.22 | 0.2745 | 2.18 | 0.3643 | 0.05821 | 0.1251 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 10.75 | 0.2488 | 1.934 | 0.2924 | 0.07065 | 0.2213 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 18.71 | 0.3333 | 3.42 | 0.4 | 0.01703 | 0.08427 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.53 | 0.2572 | 1.701 | 0.2157 | 0.02437 | 0.1394 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 12.39 | 0.2586 | 1.352 | 0.431 | 0.03755 | 0.2419 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 12.99 | 0.2709 | 2.511 | 0.4457 | 0.02609 | 0.09974 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 15.29 | 0.2934 | 2.139 | 0.3496 | 0.04053 | 0.1135 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 15.56 | 0.2961 | 2.023 | 0.3213 | 0.02778 | 0.06337 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 9.917 | 0.1667 | 1.785 | 0.2333 | 0.0331 | 0.1299 |
| 002130 | 沃尔核材 | CN | C 制造业 | 0.1905 | 19.15 | 0.3496 | 2.696 | 0.4798 | 0.009532 | 0.04703 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.35 | 0.2556 | 2.567 | 0.4525 | 0.04338 | 0.1418 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 18.99 | 0.3444 | 2.419 | 0.4268 | 0.01974 | 0.05324 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.8 | 0.3144 | 2.274 | 0.3916 | 0.02012 | 0.06364 |
| 002351 | 漫步者 | CN | C 制造业 | 0.1494 | 19.54 | 0.3543 | 2.712 | 0.4829 | 0.01791 | 0.04679 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 14.22 | 0.2835 | 1.866 | 0.2677 | 0.01326 | 0.06472 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 25.43 | 0.4215 | 2.496 | 0.4415 | 0.01458 | 0.0807 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 16.63 | 0.3118 | 2.409 | 0.4252 | 0.03077 | 0.08639 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.72 | 0.2656 | 2.298 | 0.3984 | 0.05394 | 0.07946 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 24.3 | 0.4179 | 2.391 | 0.4776 | 0.009588 | 0.08089 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 20.55 | 0.4393 | 2.114 | 0.1925 | 0.007937 | 0.06908 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 21.73 | 0.3843 | 2.265 | 0.389 | 0.014 | 0.03963 |
| 300286 | 安科瑞 | CN | C 制造业 | 0.1025 | 24.26 | 0.411 | 2.271 | 0.3906 | 0.01405 | 0.0426 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.46 | 0.243 | 1.391 | 0.1339 | 0.02034 | 0.08576 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 15.38 | 0.2945 | 2.015 | 0.3181 | 0.01626 | 0.06826 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 10.71 | 0.2478 | 2.336 | 0.4115 | 0.02579 | 0.145 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 10.84 | 0.2493 | 1.962 | 0.3013 | 0.03303 | 0.1242 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 11.18 | 0.253 | 2.705 | 0.4819 | 0.03286 | 0.06973 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 8.637 | 0.2352 | 2.219 | 0.3753 | 0.00878 | 0.08152 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 12.7 | 0.2651 | 1.858 | 0.2667 | 0.01274 | 0.05089 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 18.42 | 0.3381 | 1.808 | 0.2462 | 0.01989 | 0.05179 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.9 | 0.3683 | 2.126 | 0.4523 | 0.03971 | 0.1246 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 19.09 | 0.4381 | 1.79 | 0.3711 | 0.02049 | 0.08564 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.39 | 0.2862 | 1.42 | 0.267 | 0.02287 | 0.08655 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.73 | 0.3463 | 1.455 | 0.2821 | 0.03286 | 0.1072 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.44 | 0.3243 | 1.397 | 0.2592 | 0.06203 | 0.1667 |
| 600415 | 小商品城 | CN | SW_UNKNOWN | 0.1753 | 13.21 | 0.3372 | 2.336 | 0.4963 | 0.04405 | 0.1888 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.91 | 0.3876 | 2.25 | 0.4771 | 0.03074 | 0.06292 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 11.75 | 0.311 | 1.452 | 0.2798 | 0.02672 | 0.1419 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 10.95 | 0.2945 | 1.598 | 0.3257 | 0.01689 | 0.1562 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 17.22 | 0.4096 | 2.182 | 0.4651 | 0.03011 | 0.05991 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 15.8 | 0.3867 | 1.896 | 0.3995 | 0.02241 | 0.08232 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.542 | 0.2706 | 1.087 | 0.1532 | 0.04973 | 0.1727 |
| 601965 | 中国汽研 | CN | SW_UNKNOWN | 0.1431 | 12.09 | 0.3202 | 1.605 | 0.328 | 0.01977 | 0.09555 |
| 603181 | 皇马科技 | CN | SW_UNKNOWN | 0.1332 | 18.25 | 0.4271 | 2.259 | 0.4803 | 0.01694 | 0.05524 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 12.18 | 0.3211 | 2.132 | 0.4537 | 0.03102 | 0.09861 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.46 | 0.3977 | 1.92 | 0.4106 | 0.03908 | 0.07628 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.15 | 0.2826 | 1.656 | 0.3422 | 0.05941 | 0.1512 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 2.992 | 2.995 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 2.007 | 2.01 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000791 | WATCH | passed_depth_scan | 2.359 | 2.364 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 5.545 | 5.562 | 30 | normal | True | 0 | 0 | OK |  | True |
| 000999 | SKIP | spread_too_wide | 3.947 | 3.961 | 34 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.709 | 3.723 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 8.802 | 8.839 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 0.998 | 1.002 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.23 | 1.236 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 7.069 | 7.107 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002130 | SKIP | spread_too_wide | 2.459 | 2.474 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.036 | 1.042 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.019 | 2.032 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.143 | 1.151 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002351 | SKIP | spread_too_wide | 0.996 | 1.004 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.555 | 3.583 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 90 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.171 | 1.182 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.644 | 1.661 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.018 | 1.029 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300286 | SKIP | spread_too_wide | 0.995 | 1.005 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.064 | 1.078 | 126 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 1.821 | 1.846 | 134 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.993 | 1.007 | 138 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.82 | 2.86 | 142 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 8.565 | 8.691 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.708 | 1.734 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6.259 | 6.356 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.668 | 2.711 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600415 | SKIP | spread_too_wide | 5.532 | 5.622 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 7.238 | 7.359 | 166 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.415 | 1.44 | 170 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 132.6 | 135 | 174 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.993 | 1.011 | 178 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 90.35 | 92.01 | 182 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 0.991 | 1.009 | 186 | normal | True | 0 | 0 | OK |  | True |
| 601965 | SKIP | spread_too_wide | 1.272 | 1.297 | 190 | normal | True | 0 | 0 | OK |  | True |
| 603181 | SKIP | spread_too_wide | 0.99 | 1.01 | 194 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.235 | 3.3 | 198 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.741 | 1.777 | 202 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 1.816 | 1.854 | 206 | normal | True | 0 | 0 | OK |  | True |
