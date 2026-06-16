"""Web unlocker tool.

Wraps the ``request_web_unlocker`` MCP tool for bypassing CAPTCHAs
and extracting rendered page content.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class RequestWebUnlockerParams(BaseModel):
    """Parameters for the ``request_web_unlocker`` tool.

    调用 Dataify 通用采集 API，输入任意 URL，智能识别 CAPTCHA、
    自动执行 JS 渲染，返回完整 PNG 截图或 HTML 源码。
    """

    url: str = Field(..., description="解锁网址，必填项")
    type: str | None = Field(default="html", description="输出格式。html 和/或 png，逗号分隔，默认 html")
    js_render: str | None = Field(default="True", description="JS 渲染，建议开启。True/False，默认 True")
    block_resources: str | None = Field(default="", description="阻止加载的资源类型，逗号分隔 (javascript,css)")
    clean_content: str | None = Field(default="", description="清除返回内容中的 JS 或 CSS 代码")
    country: str | None = Field(default="us", description="代理所在国家/地区代码，默认 us")
    headers: str | None = Field(default="", description='自定义请求 Headers，JSON 格式 {"aaa":"bbb"}')
    cookies: str | None = Field(default="", description='自定义请求 Cookies，JSON 格式 {"aaa":"bbb"}')
    wait: str | None = Field(default="", description="页面加载后额外等待的时间（毫秒）")
    wait_for: str | None = Field(default="", description="等待指定的 CSS 选择器出现后再返回内容")
    follow_redirect: str | None = Field(default="True", description="跟随 HTTP 重定向。True/False，默认 True")


async def request_web_unlocker(self, params: RequestWebUnlockerParams | None = None) -> Any:
    """Call ``request_web_unlocker`` — 通用网页解锁。

    调用 Dataify 通用采集 API，输入任意 URL，智能识别 CAPTCHA、
    自动执行 JS 渲染，返回完整 PNG 截图或 HTML 源码。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("request_web_unlocker", arguments)


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all web unlocker methods to the client class."""
    client_cls.request_web_unlocker = request_web_unlocker
