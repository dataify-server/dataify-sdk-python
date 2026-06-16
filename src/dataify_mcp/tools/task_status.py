"""Task status and statistics tools.

Wraps MCP tools for querying web unlocker and scraper task status,
statistics, products, and tool lists.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# web_unlock_task
# ---------------------------------------------------------------------------


class WebUnlockTaskParams(BaseModel):
    """Parameters for the ``web_unlock_task`` tool.

    查询 Dataify 通用采集 API 的任务状态、消耗明细和用户累计统计。
    """

    keyword: str | None = Field(default="", description="搜索的任务 ID 或域名，可选")
    status: int | None = Field(default=-1, description="任务状态: -1 全部，0 成功，1 失败")
    page: int | None = Field(default=1, description="当前页，默认 1")
    page_size: int | None = Field(default=10, description="每页数据量，默认 10，最大 100")
    start: int | None = Field(default=None, description="查询时间范围开始时间，秒级时间戳")
    end: int | None = Field(default=None, description="查询时间范围结束时间，秒级时间戳")


async def web_unlock_task(self, params: WebUnlockTaskParams | None = None) -> Any:
    """Call ``web_unlock_task`` — 查询通用采集 API 任务状态。

    查询 Dataify 通用采集 API 的任务状态、消耗明细和用户累计统计。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    # Map snake_case parameter names back to the server's parameter names
    if "page_size" in arguments:
        arguments["pageSize"] = arguments.pop("page_size")
    return await self.call_tool("web_unlock_task", arguments)


# ---------------------------------------------------------------------------
# web_unlock_statistics
# ---------------------------------------------------------------------------


class WebUnlockStatisticsParams(BaseModel):
    """Parameters for the ``web_unlock_statistics`` tool.

    根据时间范围统计 Dataify 通用采集 API 的成功次数、失败次数、成功率等。
    """

    start: int | None = Field(default=None, description="查询时间范围开始时间，秒级时间戳")
    end: int | None = Field(default=None, description="查询时间范围结束时间，秒级时间戳")


async def web_unlock_statistics(self, params: WebUnlockStatisticsParams | None = None) -> Any:
    """Call ``web_unlock_statistics`` — 查询通用采集 API 统计数据。

    根据时间范围统计 Dataify 通用采集 API 的成功、失败次数、成功率、
    平均响应时间、P50/P90 响应时间和消耗积分。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("web_unlock_statistics", arguments)


# ---------------------------------------------------------------------------
# scraper_task_list
# ---------------------------------------------------------------------------


class ScraperTaskListParams(BaseModel):
    """Parameters for the ``scraper_task_list`` tool.

    根据任务 ID、工具名称、类型、状态和时间范围查询网页采集与 SERP 采集任务。
    """

    keyword: str | None = Field(default="", description="按任务 ID 或工具名称查询，可选")
    type: int | None = Field(default=0, description="类型: 0 全部，1 SERP 采集，2 网页采集")
    status: int | None = Field(default=0, description="任务状态: 0 全部，-1 处理中，200 成功，400 失败")
    start: int | None = Field(default=None, description="查询时间范围开始时间，秒级时间戳")
    end: int | None = Field(default=None, description="查询时间范围结束时间，秒级时间戳")
    page: int | None = Field(default=1, description="当前页，默认 1")
    page_size: int | None = Field(default=10, description="每页数据量，默认 10，最大 100")


async def scraper_task_list(self, params: ScraperTaskListParams | None = None) -> Any:
    """Call ``scraper_task_list`` — 查询采集任务列表。

    根据任务 ID、工具名称、类型、状态和时间范围查询 Dataify
    网页采集与 SERP 采集任务。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    if "page_size" in arguments:
        arguments["pageSize"] = arguments.pop("page_size")
    return await self.call_tool("scraper_task_list", arguments)


# ---------------------------------------------------------------------------
# scraper_statistics
# ---------------------------------------------------------------------------


class ScraperStatisticsParams(BaseModel):
    """Parameters for the ``scraper_statistics`` tool.

    根据时间范围统计网页采集和 SERP 采集的成功、失败次数和消耗积分。
    """

    start: int | None = Field(default=None, description="查询时间范围开始时间，秒级时间戳")
    end: int | None = Field(default=None, description="查询时间范围结束时间，秒级时间戳")


async def scraper_statistics(self, params: ScraperStatisticsParams | None = None) -> Any:
    """Call ``scraper_statistics`` — 查询采集统计数据。

    根据时间范围统计网页采集和 SERP 采集的成功、失败次数和消耗积分。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scraper_statistics", arguments)


# ---------------------------------------------------------------------------
# scraper_serp_products
# ---------------------------------------------------------------------------


class ScraperSerpProductsParams(BaseModel):
    """Parameters for the ``scraper_serp_products`` tool.

    查询 Dataify 网页采集和 SERP 的产品列表信息。
    """

    scraper_type: int | None = Field(default=-1, description="产品类型: -1 全部，0 网页抓取，1 SERP")


async def scraper_serp_products(self, params: ScraperSerpProductsParams | None = None) -> Any:
    """Call ``scraper_serp_products`` — 查询采集产品列表。

    查询 Dataify 网页采集和 SERP 的产品列表信息。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    if "scraper_type" in arguments:
        arguments["scraperType"] = arguments.pop("scraper_type")
    return await self.call_tool("scraper_serp_products", arguments)


# ---------------------------------------------------------------------------
# scraper_serp_tools
# ---------------------------------------------------------------------------


class ScraperSerpToolsParams(BaseModel):
    """Parameters for the ``scraper_serp_tools`` tool.

    查询指定采集产品的工具列表。
    """

    product_id: int = Field(..., description="采集产品 ID")


async def scraper_serp_tools(self, params: ScraperSerpToolsParams) -> Any:
    """Call ``scraper_serp_tools`` — 查询采集产品工具列表。

    查询指定采集产品的工具列表。
    """
    arguments = {"productId": params.product_id}
    return await self.call_tool("scraper_serp_tools", arguments)


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all task status methods to the client class."""
    client_cls.web_unlock_task = web_unlock_task
    client_cls.web_unlock_statistics = web_unlock_statistics
    client_cls.scraper_task_list = scraper_task_list
    client_cls.scraper_statistics = scraper_statistics
    client_cls.scraper_serp_products = scraper_serp_products
    client_cls.scraper_serp_tools = scraper_serp_tools
