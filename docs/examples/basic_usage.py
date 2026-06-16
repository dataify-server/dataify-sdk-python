"""Basic usage examples for the Dataify MCP SDK."""

import asyncio
from dataify_mcp import DataifyClient, AuthenticationError, ToolError, ConnectionError

# 配置
BASE_URL = "http://localhost:7780"
TOKEN = "your-api-token"


async def example_list_tools():
    """列出所有可用工具。"""
    async with DataifyClient(BASE_URL, TOKEN) as client:
        tools = await client.list_tools()
        for tool in tools:
            print(f"  {tool.name}: {tool.description[:80]}...")


async def example_google_search():
    """执行 Google 搜索。"""
    async with DataifyClient(BASE_URL, TOKEN) as client:
        result = await client.call_tool("google_search", {
            "q": "Python 异步编程",
            "gl": "cn",
            "hl": "zh-cn",
            "num": "10",
        })
        print(result)


async def example_web_unlocker():
    """解锁网页。"""
    async with DataifyClient(BASE_URL, TOKEN) as client:
        result = await client.call_tool("request_web_unlocker", {
            "url": "https://example.com",
            "type": "html",
            "js_render": "True",
        })
        print(result)


async def example_user_info():
    """查询用户信息。"""
    async with DataifyClient(BASE_URL, TOKEN) as client:
        result = await client.call_tool("query_user_info", {})
        print(result)


async def example_error_handling():
    """错误处理示例。"""
    try:
        async with DataifyClient(BASE_URL, "invalid-token") as client:
            await client.call_tool("google_search", {"q": "test"})
    except AuthenticationError:
        print("Token 无效，请检查 https://dashboard.dataify.com")
    except ToolError as e:
        print(f"工具执行失败: {e}")
    except ConnectionError:
        print("无法连接服务器")


async def example_with_tool_filter():
    """使用工具过滤。"""
    async with DataifyClient(
        BASE_URL, TOKEN,
        tool_codes="serp,google",  # 只使用 SERP 相关工具
    ) as client:
        tools = await client.list_tools()
        print(f"过滤后的工具数: {len(tools)}")


async def example_sse_transport():
    """使用 SSE 传输。"""
    async with DataifyClient(
        BASE_URL, TOKEN,
        transport="sse",
    ) as client:
        result = await client.call_tool("google_search", {"q": "test"})
        print(result)


async def main():
    """运行所有示例。"""
    print("=" * 60)
    print("Dataify MCP SDK — 使用示例")
    print("=" * 60)

    try:
        await example_list_tools()
    except ConnectionError:
        print("(跳过 — 服务器未运行)")

    print("\n提示: 修改 TOKEN 并启动服务器后运行完整示例。")


if __name__ == "__main__":
    asyncio.run(main())
