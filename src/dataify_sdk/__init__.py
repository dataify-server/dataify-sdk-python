"""Dataify SDK — a Python client that talks **directly** to the Dataify
upstream REST API (no MCP layer).

Typical usage::

    from dataify_sdk import DataifyClient
    from dataify_sdk.tools.amazonproduct import amazon_product_by_asin

    client = DataifyClient(token="YOUR_TOKEN")
    result = amazon_product_by_asin(asin="B0BZYCJK89", client=client)

or, using the default client (token from ``DATAIFY_TOKEN``)::

    result = amazon_product_by_asin(asin="B0BZYCJK89")
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
