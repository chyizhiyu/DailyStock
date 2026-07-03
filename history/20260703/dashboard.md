# DailyStock Funnel Dashboard

- As of: `2026-07-03`
- Markets: `CN,HK`
- Dry run: `True`

## Funnel

| Step | Input | Output | Rejections | Seconds |
| --- | ---: | ---: | --- | ---: |
| step1_fetch_meta | 0 | 7927 | - | 377.642 |
| step2_hard_filters | 7927 | 2714 | risk_screen: 1486, listing_age: 583, liquidity: 906, market_cap: 1805, performance_floor: 433 | 0.818 |
| step3_financial_quality | 2714 | 263 | profitability: 2230, leverage: 40, cash_flow_quality: 103, growth: 78 | 0.068 |
| step4_valuation | 263 | 55 | missing_valuation_data: 10, pe_valuation_percentile: 123, pb_valuation_percentile: 65, dividend_yield: 10 | 0.286 |
| step5_futu_executor | 55 | 55 | spread_too_wide: 49 | 0.008 |

## Market Coverage

| Step | CN Out | CN Rejected | HK Out | HK Rejected |
| --- | ---: | ---: | ---: | ---: |
| step1_fetch_meta | 5129 | 0 | 2798 | 0 |
| step2_hard_filters | 2504 | 2625 | 210 | 2588 |
| step3_financial_quality | 237 | 2267 | 26 | 184 |
| step4_valuation | 54 | 183 | 1 | 25 |
| step5_futu_executor | 54 | 48 | 1 | 1 |

## Rejection Breakdown By Market

| Step | Reason | CN | HK |
| --- | --- | ---: | ---: |
| step2_hard_filters | risk_screen | 3 | 1483 |
| step2_hard_filters | listing_age | 301 | 282 |
| step2_hard_filters | liquidity | 338 | 568 |
| step2_hard_filters | market_cap | 1568 | 237 |
| step2_hard_filters | performance_floor | 415 | 18 |
| step3_financial_quality | profitability | 2065 | 165 |
| step3_financial_quality | leverage | 32 | 8 |
| step3_financial_quality | cash_flow_quality | 100 | 3 |
| step3_financial_quality | growth | 70 | 8 |
| step4_valuation | missing_valuation_data | 8 | 2 |
| step4_valuation | pe_valuation_percentile | 103 | 20 |
| step4_valuation | pb_valuation_percentile | 62 | 3 |
| step4_valuation | dividend_yield | 10 | 0 |
| step5_futu_executor | spread_too_wide | 48 | 1 |

## Final Candidates

| code | name | market | industry | roe | pe_ttm | pe_percentile | pb | pb_percentile | dividend_yield | fcf_yield |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | 东阿阿胶 | CN | C 制造业 | 0.1666 | 17.44 | 0.3108 | 2.792 | 0.4677 | 0.02899 | 0.07598 |
| 000598 | 兴蓉环境 | CN | D 水电煤气 | 0.106 | 9.722 | 0.2069 | 0.964 | 0.2069 | 0.03596 | 0.1896 |
| 000848 | 承德露露 | CN | C 制造业 | 0.1778 | 13.32 | 0.2682 | 2.196 | 0.3312 | 0.05821 | 0.1242 |
| 000915 | 华特达因 | CN | C 制造业 | 0.1829 | 11.12 | 0.2483 | 2 | 0.2798 | 0.07065 | 0.214 |
| 000975 | 山金国际 | CN | B 采矿业 | 0.2156 | 18.53 | 0.3333 | 3.387 | 0.4333 | 0.01703 | 0.08508 |
| 000999 | 华润三九 | CN | C 制造业 | 0.1607 | 11.66 | 0.2535 | 1.72 | 0.1948 | 0.02437 | 0.1379 |
| 001286 | 陕西能源 | CN | D 水电煤气 | 0.1182 | 13.21 | 0.2759 | 1.442 | 0.4138 | 0.03755 | 0.2268 |
| 002001 | 新和成 | CN | C 制造业 | 0.2187 | 13.57 | 0.2735 | 2.624 | 0.4362 | 0.02609 | 0.09541 |
| 002003 | 伟星股份 | CN | C 制造业 | 0.1441 | 15.96 | 0.2929 | 2.233 | 0.3428 | 0.04053 | 0.1087 |
| 002020 | 京新药业 | CN | C 制造业 | 0.1328 | 16.51 | 0.2971 | 2.146 | 0.3155 | 0.02778 | 0.05974 |
| 002128 | 电投能源 | CN | B 采矿业 | 0.1494 | 10.14 | 0.1667 | 1.826 | 0.2333 | 0.0331 | 0.127 |
| 002170 | 芭田股份 | CN | C 制造业 | 0.2593 | 11.91 | 0.2567 | 2.694 | 0.4493 | 0.04338 | 0.1351 |
| 002262 | 恩华药业 | CN | C 制造业 | 0.1388 | 19.03 | 0.337 | 2.423 | 0.3906 | 0.01974 | 0.05313 |
| 002275 | 桂林三金 | CN | C 制造业 | 0.1389 | 17.8 | 0.3181 | 2.328 | 0.369 | 0.02244 | 0.09151 |
| 002287 | 奇正藏药 | CN | C 制造业 | 0.1468 | 16.93 | 0.3034 | 2.292 | 0.3601 | 0.02012 | 0.06314 |
| 002351 | 漫步者 | CN | C 制造业 | 0.1494 | 19.81 | 0.3475 | 2.75 | 0.4593 | 0.01791 | 0.04615 |
| 002444 | 巨星科技 | CN | C 制造业 | 0.1416 | 15.8 | 0.2913 | 2.074 | 0.3008 | 0.01326 | 0.05825 |
| 002632 | 道明光学 | CN | C 制造业 | 0.1022 | 25.51 | 0.4121 | 2.505 | 0.4115 | 0.01458 | 0.08043 |
| 002833 | 弘亚数控 | CN | C 制造业 | 0.1481 | 18.83 | 0.3333 | 2.728 | 0.4551 | 0.03077 | 0.0763 |
| 002884 | 凌霄泵业 | CN | C 制造业 | 0.1946 | 12.47 | 0.2614 | 2.254 | 0.3496 | 0.05394 | 0.08102 |
| 002967 | 广电计量 | CN | M 科研服务 | 0.1219 | 25.13 | 0.4179 | 2.474 | 0.4478 | 0.009588 | 0.0782 |
| 300002 | 神州泰岳 | CN | I 信息技术 | 0.1094 | 18.72 | 0.4351 | 1.926 | 0.1213 | 0.007937 | 0.07585 |
| 300009 | 安科生物 | CN | C 制造业 | 0.175 | 18.55 | 0.327 | 2.874 | 0.4814 | 0.03041 | 0.06332 |
| 300043 | 星辉娱乐 | CN | I 信息技术 | 0.189 | 18.21 | 0.431 | 3.041 | 0.4184 | 0.01185 | 0.09924 |
| 300130 | 新国都 | CN | C 制造业 | 0.108 | 23.98 | 0.3916 | 2.499 | 0.4089 | 0.014 | 0.03593 |
| 300286 | 安科瑞 | CN | C 制造业 | 0.1025 | 26.71 | 0.4231 | 2.5 | 0.4105 | 0.01405 | 0.03868 |
| 300360 | 炬华科技 | CN | C 制造业 | 0.1362 | 10.96 | 0.2462 | 1.458 | 0.1344 | 0.02034 | 0.08184 |
| 300470 | 中密控股 | CN | C 制造业 | 0.138 | 16.49 | 0.2966 | 2.161 | 0.3181 | 0.01626 | 0.06366 |
| 300533 | 冰川网络 | CN | I 信息技术 | 0.3288 | 7.524 | 0.3808 | 3.344 | 0.4937 | 0.03779 | 0.1327 |
| 300641 | 正丹股份 | CN | C 制造业 | 0.2348 | 11.91 | 0.2572 | 2.597 | 0.4294 | 0.02579 | 0.1304 |
| 300705 | 九典制药 | CN | C 制造业 | 0.1804 | 11.07 | 0.2478 | 2.004 | 0.2814 | 0.03303 | 0.1217 |
| 300910 | 瑞丰新材 | CN | C 制造业 | 0.2099 | 11.84 | 0.2562 | 2.864 | 0.4787 | 0.03286 | 0.06587 |
| 301061 | 匠心家居 | CN | C 制造业 | 0.2196 | 8.904 | 0.2346 | 2.288 | 0.3585 | 0.00878 | 0.07908 |
| 301219 | 腾远钴业 | CN | C 制造业 | 0.1213 | 14.4 | 0.2787 | 2.106 | 0.3097 | 0.01274 | 0.04488 |
| 301303 | 真兰仪表 | CN | C 制造业 | 0.1018 | 18.98 | 0.336 | 1.863 | 0.2404 | 0.01989 | 0.05027 |
| 600007 | 中国国贸 | CN | SW_UNKNOWN | 0.1264 | 16.01 | 0.3817 | 1.909 | 0.3858 | 0.05596 | 0.08208 |
| 600012 | 皖通高速 | CN | SW_UNKNOWN | 0.1401 | 14.63 | 0.3587 | 2.086 | 0.428 | 0.04047 | 0.127 |
| 600026 | 中远海能 | CN | SW_UNKNOWN | 0.1042 | 21.02 | 0.4578 | 1.971 | 0.3995 | 0.02188 | 0.07775 |
| 600062 | 华润双鹤 | CN | SW_UNKNOWN | 0.1486 | 10.7 | 0.2853 | 1.463 | 0.2702 | 0.0222 | 0.08402 |
| 600377 | 宁沪高速 | CN | SW_UNKNOWN | 0.1148 | 13.17 | 0.3303 | 1.396 | 0.2468 | 0.03286 | 0.1118 |
| 600398 | 海澜之家 | CN | SW_UNKNOWN | 0.1231 | 12.36 | 0.3161 | 1.387 | 0.2422 | 0.06203 | 0.1679 |
| 600415 | 小商品城 | CN | SW_UNKNOWN | 0.1753 | 13.79 | 0.3427 | 2.44 | 0.4963 | 0.04405 | 0.1808 |
| 600483 | 福能股份 | CN | SW_UNKNOWN | 0.1127 | 9.934 | 0.2739 | 1.051 | 0.1344 | 0.03352 | 0.1745 |
| 600598 | 北大荒 | CN | SW_UNKNOWN | 0.149 | 17.3 | 0.4041 | 2.351 | 0.478 | 0.03645 | 0.06148 |
| 600600 | 青岛啤酒 | CN | SW_UNKNOWN | 0.155 | 15.87 | 0.3784 | 2.245 | 0.4601 | 0.04402 | 0.06307 |
| 600933 | 爱柯迪 | CN | SW_UNKNOWN | 0.1321 | 13.04 | 0.3266 | 1.612 | 0.3124 | 0.02672 | 0.1277 |
| 600938 | 中国海油 | CN | SW_UNKNOWN | 0.1564 | 10.77 | 0.2872 | 1.572 | 0.3028 | 0.02522 | 0.1588 |
| 600993 | 马应龙 | CN | SW_UNKNOWN | 0.1377 | 16.94 | 0.3986 | 2.147 | 0.4417 | 0.03061 | 0.06091 |
| 601088 | 中国神华 | CN | SW_UNKNOWN | 0.1276 | 15.3 | 0.3711 | 1.836 | 0.367 | 0.02531 | 0.08503 |
| 601900 | 南方传媒 | CN | SW_UNKNOWN | 0.1219 | 9.441 | 0.2679 | 1.076 | 0.1422 | 0.05027 | 0.1746 |
| 603568 | 伟明环保 | CN | SW_UNKNOWN | 0.1572 | 11.97 | 0.3096 | 2.1 | 0.4326 | 0.03102 | 0.1001 |
| 603658 | 安图生物 | CN | SW_UNKNOWN | 0.1225 | 16.59 | 0.3936 | 1.935 | 0.3908 | 0.03908 | 0.07569 |
| 603816 | 顾家家居 | CN | SW_UNKNOWN | 0.1768 | 10.56 | 0.283 | 1.722 | 0.3417 | 0.05235 | 0.1454 |
| 605183 | 确成股份 | CN | SW_UNKNOWN | 0.1407 | 12.39 | 0.3183 | 1.644 | 0.3216 | 0.02712 | 0.09159 |
| 02877 | 神威药业 | HK | 药品及生物科技 | 0.1223 | 5.929 | 0.4333 | 0.6986 | 0.2712 | 0.07353 | 0.188 |

## Execution Plan

| code | action | decision_reason | bid | ask | spread_bps | volume_signal | tradable | planned_notional | planned_position_pct | risk_status | risk_reason | dry_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000423 | WATCH | passed_depth_scan | 3.011 | 3.014 | 10 | normal | True | 0 | 0 | OK |  | True |
| 000598 | WATCH | passed_depth_scan | 1.95 | 1.953 | 14 | normal | True | 0 | 0 | OK |  | True |
| 000848 | WATCH | passed_depth_scan | 0.999 | 1.001 | 18 | normal | True | 0 | 0 | OK |  | True |
| 000915 | WATCH | passed_depth_scan | 0.999 | 1.001 | 22 | normal | True | 0 | 0 | OK |  | True |
| 000975 | WATCH | passed_depth_scan | 5.494 | 5.508 | 26 | normal | True | 0 | 0 | OK |  | True |
| 000999 | WATCH | passed_depth_scan | 3.993 | 4.005 | 30 | normal | True | 0 | 0 | OK |  | True |
| 001286 | SKIP | spread_too_wide | 3.957 | 3.97 | 34 | normal | True | 0 | 0 | OK |  | True |
| 002001 | SKIP | spread_too_wide | 9.203 | 9.238 | 38 | normal | True | 0 | 0 | OK |  | True |
| 002003 | SKIP | spread_too_wide | 1.042 | 1.046 | 42 | normal | True | 0 | 0 | OK |  | True |
| 002020 | SKIP | spread_too_wide | 1.305 | 1.311 | 46 | normal | True | 0 | 0 | OK |  | True |
| 002128 | SKIP | spread_too_wide | 7.232 | 7.269 | 50 | normal | True | 0 | 0 | OK |  | True |
| 002170 | SKIP | spread_too_wide | 1.088 | 1.094 | 54 | normal | True | 0 | 0 | OK |  | True |
| 002262 | SKIP | spread_too_wide | 2.024 | 2.035 | 58 | normal | True | 0 | 0 | OK |  | True |
| 002275 | SKIP | spread_too_wide | 0.997 | 1.003 | 62 | normal | True | 0 | 0 | OK |  | True |
| 002287 | SKIP | spread_too_wide | 1.152 | 1.159 | 66 | normal | True | 0 | 0 | OK |  | True |
| 002351 | SKIP | spread_too_wide | 0.997 | 1.004 | 70 | normal | True | 0 | 0 | OK |  | True |
| 002444 | SKIP | spread_too_wide | 3.951 | 3.98 | 74 | normal | True | 0 | 0 | OK |  | True |
| 002632 | SKIP | spread_too_wide | 0.996 | 1.004 | 78 | normal | True | 0 | 0 | OK |  | True |
| 002833 | SKIP | spread_too_wide | 0.996 | 1.004 | 82 | normal | True | 0 | 0 | OK |  | True |
| 002884 | SKIP | spread_too_wide | 0.996 | 1.004 | 86 | normal | True | 0 | 0 | OK |  | True |
| 002967 | SKIP | spread_too_wide | 1.212 | 1.223 | 90 | normal | True | 0 | 0 | OK |  | True |
| 300002 | SKIP | spread_too_wide | 1.498 | 1.512 | 94 | normal | True | 0 | 0 | OK |  | True |
| 300009 | SKIP | spread_too_wide | 1.357 | 1.37 | 98 | normal | True | 0 | 0 | OK |  | True |
| 300043 | SKIP | spread_too_wide | 0.995 | 1.005 | 102 | normal | True | 0 | 0 | OK |  | True |
| 300130 | SKIP | spread_too_wide | 1.123 | 1.135 | 106 | normal | True | 0 | 0 | OK |  | True |
| 300286 | SKIP | spread_too_wide | 0.995 | 1.006 | 110 | normal | True | 0 | 0 | OK |  | True |
| 300360 | SKIP | spread_too_wide | 0.994 | 1.006 | 114 | normal | True | 0 | 0 | OK |  | True |
| 300470 | SKIP | spread_too_wide | 0.994 | 1.006 | 118 | normal | True | 0 | 0 | OK |  | True |
| 300533 | SKIP | spread_too_wide | 0.994 | 1.006 | 122 | normal | True | 0 | 0 | OK |  | True |
| 300641 | SKIP | spread_too_wide | 0.994 | 1.006 | 126 | normal | True | 0 | 0 | OK |  | True |
| 300705 | SKIP | spread_too_wide | 0.994 | 1.006 | 130 | normal | True | 0 | 0 | OK |  | True |
| 300910 | SKIP | spread_too_wide | 1.126 | 1.141 | 134 | normal | True | 0 | 0 | OK |  | True |
| 301061 | SKIP | spread_too_wide | 0.993 | 1.007 | 138 | normal | True | 0 | 0 | OK |  | True |
| 301219 | SKIP | spread_too_wide | 2.064 | 2.094 | 142 | normal | True | 0 | 0 | OK |  | True |
| 301303 | SKIP | spread_too_wide | 0.993 | 1.007 | 146 | normal | True | 0 | 0 | OK |  | True |
| 600007 | SKIP | spread_too_wide | 1.904 | 1.933 | 150 | normal | True | 0 | 0 | OK |  | True |
| 600012 | SKIP | spread_too_wide | 2.765 | 2.808 | 154 | normal | True | 0 | 0 | OK |  | True |
| 600026 | SKIP | spread_too_wide | 9.428 | 9.579 | 158 | normal | True | 0 | 0 | OK |  | True |
| 600062 | SKIP | spread_too_wide | 1.759 | 1.787 | 162 | normal | True | 0 | 0 | OK |  | True |
| 600377 | SKIP | spread_too_wide | 6 | 6.101 | 166 | normal | True | 0 | 0 | OK |  | True |
| 600398 | SKIP | spread_too_wide | 2.648 | 2.693 | 170 | normal | True | 0 | 0 | OK |  | True |
| 600415 | SKIP | spread_too_wide | 5.773 | 5.874 | 174 | normal | True | 0 | 0 | OK |  | True |
| 600483 | SKIP | spread_too_wide | 2.901 | 2.954 | 178 | normal | True | 0 | 0 | OK |  | True |
| 600598 | SKIP | spread_too_wide | 1.999 | 2.036 | 182 | normal | True | 0 | 0 | OK |  | True |
| 600600 | SKIP | spread_too_wide | 7.214 | 7.35 | 186 | normal | True | 0 | 0 | OK |  | True |
| 600933 | SKIP | spread_too_wide | 1.57 | 1.6 | 190 | normal | True | 0 | 0 | OK |  | True |
| 600938 | SKIP | spread_too_wide | 130.3 | 132.9 | 194 | normal | True | 0 | 0 | OK |  | True |
| 600993 | SKIP | spread_too_wide | 0.99 | 1.01 | 198 | normal | True | 0 | 0 | OK |  | True |
| 601088 | SKIP | spread_too_wide | 87.38 | 89.17 | 202 | normal | True | 0 | 0 | OK |  | True |
| 601900 | SKIP | spread_too_wide | 0.99 | 1.01 | 206 | normal | True | 0 | 0 | OK |  | True |
| 603568 | SKIP | spread_too_wide | 3.184 | 3.252 | 210 | normal | True | 0 | 0 | OK |  | True |
| 603658 | SKIP | spread_too_wide | 1.754 | 1.792 | 214 | normal | True | 0 | 0 | OK |  | True |
| 603816 | SKIP | spread_too_wide | 1.887 | 1.929 | 218 | normal | True | 0 | 0 | OK |  | True |
| 605183 | SKIP | spread_too_wide | 0.989 | 1.011 | 222 | normal | True | 0 | 0 | OK |  | True |
| 02877 | SKIP | spread_too_wide | 0.989 | 1.011 | 226 | normal | True | 0 | 0 | OK |  | True |
