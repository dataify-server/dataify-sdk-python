# Dataify Python SDK

Python 客户端库，**直接调用** [Dataify](https://dashboard.dataify.com) 上游 REST 接口（**不走 MCP 协议**），用于网页采集与搜索引擎抓取。


## 功能

- 🔍 **搜索引擎** — Google（17 种）、Bing（6 种）、Yandex、DuckDuckGo，走 `POST /request`
- 🛒 **平台抓取器** — Amazon、YouTube、TikTok、Facebook、Instagram、Reddit、Twitter/X、LinkedIn、Glassdoor、Indeed、Walmart、Zillow、Airbnb、Booking、Crunchbase、eBay、GitHub 等 45 个采集器，先走 `POST /builder?platform=1`，再可查询任务状态并下载结果
- 📖 **参数全暴露** — 每个工具函数把上游请求参数、类型、是否必填、中文描述都写在签名与 docstring 里；另见 `docs/api_reference.md`
- 🐍 **零依赖** — 仅用标准库 `urllib`，同步 API

## 安装

```bash
pip install dataify-sdk
```

要求 Python >= 3.10。

## 快速开始

```python
from dataify_sdk import DataifyClient
from dataify_sdk.tools.amazonproduct import amazon_product_by_asin
from dataify_sdk.tools.googlesearch import google_search

# token 也可通过环境变量 DATAIFY_API_TOKEN 提供（兼容旧版 DATAIFY_TOKEN）
client = DataifyClient(token="YOUR_TOKEN")

# 采集类：先提交 Builder 任务
task = amazon_product_by_asin(asin="B0BZYCJK89", client=client)
task_id = task["data"]["task_id"]

# 再查询任务状态
status = client.query_scraper_task_status(task_id)
if status["data"]["status"] == "成功":
    result = client.download_scraper_task_result(task_id, result_type="json")

# 搜索类：直接打搜索引擎接口
result = google_search(q="pizza", client=client)
```

也可以不传 `client`，使用默认 client（优先读取 `DATAIFY_API_TOKEN`，兼容 `DATAIFY_TOKEN`）：

```bash
export DATAIFY_API_TOKEN="..."
```

```python
from dataify_sdk.tools.googlesearch import google_search

result = google_search(q="pizza")
```

`client.query_scraper_task_status(...)` 会返回任务状态 JSON，`data.status` 常见值为 `处理中`、`成功`、`失败`。任务成功后可用 `client.download_scraper_task_result(task_id, result_type="json")` 下载最终结果；`result_type` 支持 `json`、`csv`、`xlsx`。

## API 设计

- **每个 `spider_id` = 一个独立函数**（采集类），例如 `amazon_product_by_asin()`、`amazon_product_by_url()`、`amazon_product_by_keywords()`。
- **搜索类每个引擎一个函数**，例如 `google_search()`、`bing_search()`、`yandex_search()`。
- 所有函数签名与 docstring 完整暴露上游参数及其描述；`docs/api_reference.md` 为离线参数手册。
- 函数返回解析后的 JSON `dict`（即上游原始响应）。

## 错误处理

```python
from dataify_sdk import DataifyClient, DataifyAPIError, DataifyConnectionError

client = DataifyClient(token="YOUR_TOKEN")
try:
    result = google_search(q="pizza", client=client)
except DataifyAPIError as e:
    print(f"上游返回错误 HTTP {e.status_code}: {e.body}")
except DataifyConnectionError:
    print("无法连接 Dataify 上游")
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 从 Go 参考项目重新生成工具函数与参数手册
python scripts/codegen.py
```

## 许可

MIT License
