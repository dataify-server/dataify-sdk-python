"""Auto-generated Dataify tool functions.  Do not edit by hand.

Generated from the Go reference project by ``dataify_sdk._codegen.generate``.
Each function calls the Dataify upstream REST API directly (no MCP layer).
"""

from __future__ import annotations

import json
from typing import Any

from dataify_sdk.client import DataifyClient, get_default_client


def _client(client: DataifyClient | None) -> DataifyClient:
    return client if client is not None else get_default_client()

def chatgpt_answer_by_keywords(file_name: str = '{{TasksID}}', search_terms: str = 'pizza', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 ChatGPT 答案、ChatGPT 回答内容、ChatGPT 提问结果、AI 回答文本、引用来源链接、相关推荐问题、答案生成时间、模型版本，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 ChatGPT 答案采集 Builder 任务，支持 chatgpt_answer_by-keywords（通过搜索关键词采集）和 chatgpt_answer_by-url（通过 URL 采集）。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: chatgpt.com
    spider_id: chatgpt_answer_by-keywords

    Parameters
    ----------
    search_terms: 搜索关键词，该参数用于指定向 ChatGPT 提问并采集答案的关键词。用于 chatgpt_answer_by-keywords。  [默认: pizza]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "search_terms": search_terms,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='chatgpt.com',
        spider_id='chatgpt_answer_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def chatgpt_answer_by_url(chatgpt_url: str = '', file_name: str = '{{TasksID}}', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 ChatGPT 答案、ChatGPT 回答内容、ChatGPT 提问结果、AI 回答文本、引用来源链接、相关推荐问题、答案生成时间、模型版本，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 ChatGPT 答案采集 Builder 任务，支持 chatgpt_answer_by-keywords（通过搜索关键词采集）和 chatgpt_answer_by-url（通过 URL 采集）。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: chatgpt.com
    spider_id: chatgpt_answer_by-url

    Parameters
    ----------
    chatgpt_url: ChatGPT 页面 URL，该参数用于指定待采集答案的 ChatGPT 访问 URL。用于 chatgpt_answer_by-url。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "chatgpt_url": chatgpt_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='chatgpt.com',
        spider_id='chatgpt_answer_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

