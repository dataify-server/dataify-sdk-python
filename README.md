# Dataify MCP Python SDK

Python 客户端库，用于通过 [MCP (Model Context Protocol)](https://spec.modelcontextprotocol.io/) 访问 [Dataify](https://dashboard.dataify.com) 数据采集平台。

## 功能

- 🌐 **网页解锁器** — 绕过 CAPTCHA、JS 渲染，返回 HTML 或 PNG 截图
- 🔍 **搜索引擎** — Google（17 种搜索类型）、Bing（6 种）、Yandex、DuckDuckGo
- 🛒 **平台抓取器** — Amazon、YouTube、TikTok、Facebook、Instagram、Reddit、Twitter/X、LinkedIn、Glassdoor、Indeed 等 35+ 平台
- ⚡ **异步优先** — 基于 `httpx` 的现代异步 API
- 🛡️ **类型安全** — 完整的类型注解，支持 `mypy --strict`
- 🔌 **双传输模式** — 支持 Streamable HTTP 和 SSE

## 安装

```bash
pip install dataify-mcp
```

要求 Python >= 3.10。

## 快速开始

```python
import asyncio
from dataify_mcp import DataifyClient

async def main():
    async with DataifyClient(
        base_url="http://localhost:7780",
        token="your-api-token",
    ) as client:
        # 列出可用工具
        tools = await client.list_tools()
        print(f"可用工具: {len(tools)} 个")

        # 调用 Google 搜索
        result = await client.call_tool("google_search", {
            "q": "今天天气",
            "gl": "cn",
            "hl": "zh-cn",
        })
        print(result)

asyncio.run(main())
```

## 连接方式

### Streamable HTTP（默认）

```python
client = DataifyClient(
    base_url="http://localhost:7780",
    token="your-token",
    transport="http",  # 默认值
)
```

### SSE（Server-Sent Events）

```python
client = DataifyClient(
    base_url="http://localhost:7780",
    token="your-token",
    transport="sse",
)
```

### 工具权限过滤

```python
# 只使用指定的工具类别
client = DataifyClient(
    base_url="http://localhost:7780",
    token="your-token",
    tool_codes="serp,google",  # 多个用逗号分隔
)
```

## 错误处理

```python
from dataify_mcp import (
    DataifyClient,
    AuthenticationError,
    ToolError,
    ConnectionError,
)

try:
    async with DataifyClient("http://localhost:7780", "token") as client:
        result = await client.call_tool("google_search", {"q": "test"})
except AuthenticationError:
    print("Token 无效，请检查 https://dashboard.dataify.com")
except ToolError as e:
    print(f"工具执行失败: {e}")
except ConnectionError:
    print("无法连接服务器")
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 代码检查
ruff check src/dataify_mcp/
mypy src/dataify_mcp/

# 运行测试
pytest

# 生成工具封装代码
python scripts/codegen.py --server http://localhost:7780 --token YOUR_TOKEN
```

## 许可

MIT License
