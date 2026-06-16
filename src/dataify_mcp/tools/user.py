"""User management tools.

Wraps MCP tools for querying user account info, balance, API keys,
and credit usage.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# query_user_info — no parameters
# ---------------------------------------------------------------------------


async def query_user_info(self) -> Any:
    """Call ``query_user_info`` — 查询用户账号信息。

    根据链接 token 查询 Dataify 用户账号信息、注册日期、
    脱敏手机号和实名认证信息。
    """
    return await self.call_tool("query_user_info", {})


# ---------------------------------------------------------------------------
# query_user_balance — no parameters
# ---------------------------------------------------------------------------


async def query_user_balance(self) -> Any:
    """Call ``query_user_balance`` — 查询用户余额。

    查询 Dataify 用户剩余积分或余额、累计充值和累计使用。
    """
    return await self.call_tool("query_user_balance", {})


# ---------------------------------------------------------------------------
# query_user_api_keys — no parameters
# ---------------------------------------------------------------------------


async def query_user_api_keys(self) -> Any:
    """Call ``query_user_api_keys`` — 查询用户 API Token 列表。

    根据链接 token 查询当前 Dataify 用户的 API Token 列表。
    """
    return await self.call_tool("query_user_api_keys", {})


# ---------------------------------------------------------------------------
# query_user_credit_usage — no parameters
# ---------------------------------------------------------------------------


async def query_user_credit_usage(self) -> Any:
    """Call ``query_user_credit_usage`` — 查询用户积分使用明细。

    查询 Dataify 用户的每日积分消耗统计。
    """
    return await self.call_tool("query_user_credit_usage", {})


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all user management methods to the client class."""
    client_cls.query_user_info = query_user_info
    client_cls.query_user_balance = query_user_balance
    client_cls.query_user_api_keys = query_user_api_keys
    client_cls.query_user_credit_usage = query_user_credit_usage
