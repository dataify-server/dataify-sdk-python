"""Dataify SDK — a Python client that talks **directly** to the Dataify
upstream REST API (no MCP layer).

Typical usage::

    from dataify_sdk import DataifyClient
    from dataify_sdk.tools.amazonproduct import amazon_product_by_asin

    client = DataifyClient(token="YOUR_TOKEN")
    task = amazon_product_by_asin(asin="B0BZYCJK89", client=client)
    task_id = task["data"]["task_id"]
    status = client.query_scraper_task_status(task_id)
    if status["data"]["status"] == "成功":
        result = client.download_scraper_task_result(task_id, result_type="json")

or, using the default client (token from ``DATAIFY_API_TOKEN``, with
``DATAIFY_TOKEN`` still accepted)::

    task = amazon_product_by_asin(asin="B0BZYCJK89")
    client = DataifyClient()
    status = client.query_scraper_task_status(task["data"]["task_id"])
"""

from __future__ import annotations

from dataify_sdk.client import DataifyClient, get_default_client
from dataify_sdk.errors import (
    DataifyAPIError,
    DataifyConnectionError,
    DataifyError,
    DataifyTimeoutError,
)

__version__ = "1.0.0"




__all__ = [
    "__version__",
    "DataifyClient",
    "get_default_client",
    "DataifyError",
    "DataifyAPIError",
    "DataifyConnectionError",
    "DataifyTimeoutError",
]
