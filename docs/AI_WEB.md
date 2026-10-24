# AI Web API

`client.ai_web` 调用 AI Web 的搜索、站点发现、正文提取和结果下载接口。所有请求使用 Dataify Bearer Token；网关返回 JSON 响应体，`X-Request-Id` 响应头会暴露为 `response.request_id`。

## 配置网关

AI Web 默认使用正式域名 `https://aiwebapi.dataify.com`，不需要额外配置：

```python
from dataify_sdk import DataifyClient

client = DataifyClient()  # token 从 DATAIFY_API_TOKEN 读取
```

`ai_web_base_url` 只填域名（不要带 `/search`、`/map` 或 `/extract`），SDK 会自动拼接接口路径。测试或私有网关可通过 `AI_WEB_API_BASE_URL` 或 `ai_web_base_url` 覆盖：

```python
import os

from dataify_sdk import DataifyClient

client = DataifyClient(
    token=os.environ["DATAIFY_API_TOKEN"],
    ai_web_base_url="https://your-test-gateway.example.com",
)
```

显式把客户端基址清空时仍会抛出 `DataifyMissingAIWebBaseUrlError`。

## 基本用法

```python
from dataify_sdk import AI_WEB_UNIQUE_IDS, DataifyClient

client = DataifyClient()  # token 从 DATAIFY_API_TOKEN 读取

result = client.ai_web.search(
    AI_WEB_UNIQUE_IDS.SEARCH_WEB,
    "OpenAI",
    max_results=3,
    source="web",
)

print(result.request_id)
print(result.outputs)
```

`AI_WEB_UNIQUE_IDS` 提供当前网关的固定标识：`SEARCH_WEB`、`SEARCH_SHOPPING`、`SEARCH_NEWS`、`SEARCH_SCHOLAR`、`MAP`、`EXTRACT`；同时提供 TS 风格的小写别名（如 `search_news`）。

## 方法

| SDK 方法 | 上游接口 | 说明 |
| --- | --- | --- |
| `client.ai_web.search(...)` | `POST /search` | 聚合 web、news、shopping、scholar 搜索，可选择提取结果正文 |
| `client.ai_web.map(...)` | `POST /map` | 发现站点页面 URL、标题和描述 |
| `client.ai_web.extract(...)` | `POST /extract` | 提取 markdown、原始 HTML、清洗后 HTML 或链接 |
| `client.ai_web.execute(operation, params)` | `POST /search`、`/map`、`/extract` | 按名称动态调用，并把 `outputs` 统一成数组 |
| `client.ai_web.execute_raw(operation, params)` | 同上 | 保留上游原始 `outputs` 结构 |
| `client.ai_web.download_result(task_id)` | `POST /download` | 通过 `request_id`（即 `task_id`）下载服务端保留的结果 |

便捷方法返回 `AIWebResponse`：

```python
@dataclass(frozen=True)
class AIWebResponse:
    request_id: str | None
    outputs: Any
```

`search`、`map`、`extract`、`execute` 会统一 `outputs`：

- `None` -> `[]`
- JSON 数组 -> 保持数组
- 单个对象或基本类型 -> 包装成单元素数组

需要上游原始结构时使用 `execute_raw`。

## Search

```python
result = client.ai_web.search(
    AI_WEB_UNIQUE_IDS.SEARCH_WEB,
    "OpenAI",
    max_results=10,
    source="web",           # web | news | shopping | scholar
    country="US",
    language="en",
    time_range="week",      # web/news 支持；shopping/scholar 不支持
    extract_content=True,
    extract_options={
        "formats": ["markdown"],
        "only_main_content": True,
        "advanced_mode": True,
    },
)
```

`time_range` 仅网页搜索和新闻搜索支持；shopping 和 scholar 不支持。`extract_options.formats` 支持 `markdown`、`raw_html`、`clean_html`、`links`。`search` 的 `extract_options` 仅在 `extract_content=True` 时生效。

## Map

```python
result = client.ai_web.map(
    AI_WEB_UNIQUE_IDS.MAP,
    "https://docs.example.com",
    country="US",
    domain_filter="all",    # domain | all
    limit=100,
    sitemap="include",      # skip | include | only
)
```

## Extract

```python
result = client.ai_web.extract(
    AI_WEB_UNIQUE_IDS.EXTRACT,
    "https://example.com/article",
    formats=["markdown", "links"],
    only_main_content=True,
    headers={"User-Agent": "Dataify SDK"},
    timeout_ms=60_000,
    advanced_mode=True,
)
```

`formats` 缺省或传空数组时表示不抓取正文。`headers` 是传给目标网站的请求头，不能包含 `Host` 或 hop-by-hop headers。

## 动态 operation

```python
result = client.ai_web.execute(
    "extract",
    {
        "unique_id": AI_WEB_UNIQUE_IDS.EXTRACT,
        "url": "https://example.com",
        "formats": ["markdown"],
    },
)

raw = client.ai_web.execute_raw(
    "extract",
    {
        "unique_id": AI_WEB_UNIQUE_IDS.EXTRACT,
        "url": "https://example.com",
        "formats": ["markdown"],
    },
)
```

`execute` 会把 `outputs` 统一成数组；`execute_raw` 保留网关返回的原始 JSON 结构。

## 下载结果

保留 `request_id`，在服务端保留期内下载结果：

```python
result = client.ai_web.extract(
    AI_WEB_UNIQUE_IDS.EXTRACT,
    "https://example.com/article",
    formats=["markdown"],
)

if result.request_id:
    downloaded = client.ai_web.download_result(result.request_id)
    print(downloaded)
```

`download_result` 发送 `POST /download`，JSON 请求体为 `{"task_id": "<request_id>"}`，使用 Bearer 认证，不会在请求体里重复放置 API key。

## 错误处理

- 未配置网关：抛出 `DataifyMissingAIWebBaseUrlError`，请求不会发出。
- 上游返回非 2xx：抛出 `DataifyAPIError`，包含 `status_code` 和 `body`。
- 缺少 `unique_id`、`query` 或 `url`：抛出 `ValueError`。
- `formats` 非法或重复：抛出 `ValueError`。

```python
from dataify_sdk import DataifyAPIError, DataifyClient, DataifyMissingAIWebBaseUrlError

client = DataifyClient()

try:
    result = client.ai_web.search("search_news", "OpenAI")
except DataifyMissingAIWebBaseUrlError:
    print("AI Web 网关不可用")
except DataifyAPIError as exc:
    print(f"AI Web 返回错误 HTTP {exc.status_code}: {exc.body}")
```
