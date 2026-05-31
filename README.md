# DailyStock

DailyStock 是一个面向 A 股与港股的周频自动化选股与交易扫盘项目骨架。它由外部自动化框架 OpenClaw 在每周五 A 股和港股收盘后触发，通过本地漏斗式筛选先快速缩小股票池，再只对少量候选调用富途 OpenD 做盘口深扫与交易计划生成。

> 当前版本默认 `dry_run=true`，不会真实下单。项目仅用于工程骨架、策略研发和模拟验证，不构成投资建议。

## 核心流程

```text
OpenClaw Webhook
      |
      v
Step 1 Fetch Meta
      |
      v
Step 2 Hard Filters        local daily bars + local financial history
      |
      v
Step 3 Financial Quality   local financial history
      |
      v
Step 4 Valuation           local industry valuation history
      |
      v
Step 5 Futu Executor       selected candidates only
```

| 步骤 | 目标 | 数据边界 | 输出 |
| --- | --- | --- | --- |
| Step 1 | 获取中证全指、恒生综合指数成分股与元信息 | 富途、AkShare、Tushare 或本地库适配器 | 全市场候选池 |
| Step 2 | 剔除高风险、低流动性、微盘、业绩底线不达标股票 | 本地日线与财报 | 硬过滤候选 |
| Step 3 | 筛选 ROE、利润率、杠杆、现金流、成长性 | 本地财报 | 高质量候选 |
| Step 4 | 按行业历史分位判断 PE、PB、股息率、FCF Yield | 本地估值历史 | 价值候选 |
| Step 5 | 盘口、价差、量能、交易状态与订单计划 | 富途 OpenD | 扫描结果与执行计划 |

富途 API 官方文档说明 OpenD 是本地或云端网关，SDK 通过 OpenD 访问行情与交易能力；DailyStock 只在第五步接触这个边界。相关文档见 [Futu API Introduction](https://openapi.futunn.com/futu-api-doc/en/) 与 [AI Integration & OpenClaw](https://openapi.futunn.com/futu-api-doc/en/intro/ai.html)。

## 多因子看板

每次运行会在 `runs/YYYYMMDD/` 下生成 CSV、JSON 和 `dashboard.md`：

- 漏斗收缩：每一步输入数量、输出数量、拒绝原因与耗时。
- 财务质量：ROE、毛利率、净利率、资产负债率、经营现金流 / 净利润、营收 CAGR、净利润 CAGR。
- 估值性价比：行业 5 年 PE/PB 历史分位、股息率相对行业中位数、自由现金流收益率。
- 执行观察：买一卖一、spread bps、量能信号、是否可交易、dry-run 动作计划。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

本地 CLI 运行：

```bash
dailystock run --as-of 2026-05-29 --markets CN,HK --dry-run
```

启动 Webhook 服务：

```bash
uvicorn dailystock.webhook:app --host 0.0.0.0 --port 8000
```

OpenClaw 可调用：

```bash
curl -X POST http://127.0.0.1:8000/webhook/openclaw \
  -H "Content-Type: application/json" \
  -H "X-OpenClaw-Token: ${DAILYSTOCK_WEBHOOK_SECRET}" \
  -d '{"as_of":"2026-05-29","markets":["CN","HK"],"dry_run":true}'
```

## 配置

主要阈值位于 `config/default.yaml`：

- `hard_filters`: 上市年限、20 日均成交额、市值、连续亏损、经营现金流底线。
- `quality_filters`: ROE、毛利率、净利率、资产负债率、现金流含金量、5 年 CAGR。
- `valuation_filters`: 行业历史 PE/PB 分位、FCF Yield。
- `futu`: OpenD host/port、交易环境、dry-run、live-trading 总开关、单笔订单金额上限、单只持仓比例上限。

敏感信息放在 `.env`，参考 `.env.example`。不要提交真实 token、账号、交易密码或 OpenD 生产配置。
Webhook 会校验 `X-OpenClaw-Token`，其值必须等于环境变量 `DAILYSTOCK_WEBHOOK_SECRET`。

## 数据源适配器

当前默认使用 `akshare` 真数据适配器，并将网络结果缓存到 `data/cache/akshare/`。测试和离线演示仍可把 `config/default.yaml` 中的 `app.data_source` 改回 `sample`，使用 `data/samples/` 中的 CSV 样例数据。

如果 GitHub Actions 访问东方财富或 AkShare 发生 `RemoteDisconnected`，可以把手动准备好的稳定快照放到 `data/seed/akshare/`。适配器会优先读取这些无日期的种子 CSV；手动触发 workflow 时可勾选 `offline=true`，或设置仓库变量 `DAILYSTOCK_AKSHARE_OFFLINE=true`，让 CI 只使用种子文件、不再访问外部行情接口。种子文件格式见 `data/seed/akshare/README.md`。

- AkShare: [AKShare 官方文档](https://akshare.akfamily.xyz/)
- Tushare: [Tushare Pro 文档](https://tushare.pro/document/1?doc_id=1)
- 本地 DuckDB/SQLite/Parquet 数据仓库
- 富途 API 元信息或盘口数据

AkShare 适配器当前覆盖：

- A 股：通过 `index_stock_cons_weight_csindex(symbol="000985")` 获取中证全指成分股，并用全市场行情快照补充成交额、市值、PE/PB；申万行业分类来自 `stock_industry_clf_hist_sw()`。
- 港股：优先尝试 AkShare 中可用的恒生综合指数成分接口；若当前 AkShare 版本未暴露稳定 HSCI 成分接口，则使用港股全市场快照作为港股初筛池，并保留 `HS_UNKNOWN` 行业兜底。
- 历史数据：日线、财务、估值、分红等逐股接口均带 3 次指数退避重试，并写入本地缓存，避免每周重复拉取 5 年历史数据。

第二、三、四步只依赖本地日线与历史财报/估值数据；实时盘口只允许进入第五步。

## 安全边界

- 默认 `dry_run=true`，`FutuClient.place_order()` 会直接阻止下单。
- 即使 CLI 使用 `--live`，仍需 `DAILYSTOCK_LIVE_TRADING_ENABLED=true` 且完成真实 Futu adapter 后才可能进入下单路径。
- 订单计划会经过 `max_order_notional` 和 `max_position_pct` 风控拦截；dry-run 也会计算并在执行计划中标记 `risk_status`。
- 第一版骨架不会实现真实订单数量、完整仓位管理或账户同步逻辑；第五步仅生成可审计的执行计划。

## 开发校验

```bash
pytest
ruff check .
```

## GitHub 发布

项目已发布到 GitHub：

- Repository: [chyizhiyu/DailyStock](https://github.com/chyizhiyu/DailyStock)
- 默认分支：`main`
- CI：`.github/workflows/ci.yml` 会在 push 和 pull request 时运行 `ruff` 与 `pytest`
