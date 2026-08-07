"""Synchronous, zero-dependency HTTP client for the Dataify upstream API.

This client talks **directly** to the Dataify REST endpoints (the same ones the
Dataify MCP server proxies), instead of going through the MCP protocol:

* Scraper / platform tools  -> ``POST {base_url}/builder?platform=1``
  (form fields: ``spider_name``, ``spider_id``, ``spider_parameters``,
  ``spider_errors``, ``file_name``)
* Search engines (Google / Bing / Yandex / DuckDuckGo) -> ``POST {base_url}/request``
  (form fields are the engine-specific parameters plus a fixed ``engine`` value)

Authentication is via a Bearer token, supplied either to the constructor or
through the ``DATAIFY_TOKEN`` environment variable.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from dataify_sdk.errors import (
    DataifyAPIError,
    DataifyConnectionError,
    DataifyTimeoutError,
)

DEFAULT_BASE_URL = "https://scraperapi.dataify.com"
DEFAULT_TIMEOUT = 120
ENV_TOKEN = "DATAIFY_TOKEN"

# Endpoints on the upstream.
_SCRAPER_PATH = "/builder?platform=1"
_SERP_PATH = "/request"


class DataifyClient:
    """Synchronous client for the Dataify upstream REST API.

    Parameters
    ----------
    token:
        Dataify API token. If omitted, the ``DATAIFY_TOKEN`` environment
        variable is used. A token is required to make any request.
    base_url:
        Upstream base URL. Fixed to the Dataify production endpoint by default;
        exposed only for testing / private deployments.
    timeout:
        Per-request timeout in seconds.
    """

    def __init__(
        self,
        token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.token = token or os.environ.get(ENV_TOKEN)
        if not self.token:
            raise ValueError(
                "A Dataify token is required: pass token=... or set the "
                f"{ENV_TOKEN} environment variable."
            )
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    # ------------------------------------------------------------------
    # Low-level transport
    # ------------------------------------------------------------------
    def _post_form(self, path: str, fields: dict[str, str]) -> dict[str, Any]:
        """POST form-encoded fields and return the parsed JSON response."""
        url = self.base_url + path
        # Only send non-empty values (mirrors the Go upstream behaviour).
        payload = {k: v for k, v in fields.items() if v not in (None, "")}
        data = urllib.parse.urlencode(payload, doseq=False).encode("utf-8")

        req = urllib.request.Request(url, data=data, method="POST")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        req.add_header("Authorization", f"Bearer {self.token}")

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:  # upstream returned >= 400
            body = exc.read().decode("utf-8", errors="replace")
            raise DataifyAPIError(
                f"Dataify API request failed: {url}", exc.code, body
            ) from exc
        except urllib.error.URLError as exc:
            if isinstance(exc.reason, TimeoutError):
                raise DataifyTimeoutError(
                    f"Request to {url} timed out after {self.timeout}s"
                ) from exc
            raise DataifyConnectionError(
                f"Could not connect to Dataify API at {url}: {exc.reason}"
            ) from exc

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"raw": raw}

    # ------------------------------------------------------------------
    # High-level helpers used by the generated tool functions
    # ------------------------------------------------------------------
    def request_scraper(
        self,
        spider_name: str,
        spider_id: str,
        spider_parameters: str,
        *,
        file_name: str = "{{TasksID}}",
        spider_errors: str = "true",
        spider_universal: str | None = None,
    ) -> dict[str, Any]:
        """Submit a Scraper / platform Builder task.

        Parameters
        ----------
        spider_name:
            Platform spider name, e.g. ``"amazon.com"``.
        spider_id:
            Builder spider id, e.g. ``"amazon_product_by-asin"``.
        spider_parameters:
            JSON-encoded string of the scraper parameters, i.e.
            ``json.dumps([{...}])`` (a single-element array of the
            parameter object).
        file_name:
            Builder ``file_name`` field. Defaults to ``"{{TasksID}}"``.
        spider_errors:
            Builder ``spider_errors`` field. Defaults to ``"true"``.
        spider_universal:
            Optional universal parameters (JSON object string).
        """
        fields: dict[str, str] = {
            "spider_name": spider_name,
            "spider_id": spider_id,
            "spider_parameters": spider_parameters,
            "spider_errors": spider_errors,
            "file_name": file_name,
        }
        if spider_universal:
            fields["spider_universal"] = spider_universal
        return self._post_form(_SCRAPER_PATH, fields)

    def request_serp(self, engine: str, fields: dict[str, str]) -> dict[str, Any]:
        """Call a search-engine endpoint.

        Parameters
        ----------
        engine:
            Fixed engine value, e.g. ``"google"``, ``"bing"``, ``"yandex"``.
        fields:
            Engine-specific parameters (already mapped to the upstream form
            field names / JSON tags). The ``engine`` field is added
            automatically.
        """
        form = {"engine": engine}
        form.update(fields)
        return self._post_form(_SERP_PATH, form)


_DEFAULT_CLIENT: DataifyClient | None = None


def get_default_client() -> DataifyClient:
    """Return a process-wide default :class:`DataifyClient`.

    Uses ``DATAIFY_TOKEN`` from the environment. Handy for the generated
    tool functions, which accept an optional ``client`` argument.
    """
    global _DEFAULT_CLIENT
    if _DEFAULT_CLIENT is None:
        _DEFAULT_CLIENT = DataifyClient()
    return _DEFAULT_CLIENT
