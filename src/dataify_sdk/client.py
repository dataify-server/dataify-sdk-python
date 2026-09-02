"""Synchronous, zero-dependency HTTP client for the Dataify upstream API.

This client talks **directly** to the Dataify REST endpoints (the same ones the
Dataify MCP server proxies), instead of going through the MCP protocol:

* Scraper / platform tools  -> ``POST {base_url}/builder?platform=1``
  (form fields: ``spider_name``, ``spider_id``, ``spider_parameters``,
  ``spider_errors``, ``file_name``)
* Scraper task status query -> ``GET {base_url}/task_status``
  (query params: ``api_key``, ``task_id``)
* Scraper task result download -> ``GET {base_url}/download``
  (query params: ``api_key``, ``task_id``, ``type``)
* Search engines (Google / Bing / Yandex / DuckDuckGo) -> ``POST {base_url}/request``
  (form fields are the engine-specific parameters plus a fixed ``engine`` value)

Authentication is via a Bearer token, supplied either to the constructor or
through the ``DATAIFY_API_TOKEN`` environment variable. The legacy
``DATAIFY_TOKEN`` name is still accepted for backward compatibility.
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
ENV_TOKEN = "DATAIFY_API_TOKEN"
LEGACY_ENV_TOKEN = "DATAIFY_TOKEN"


def _read_env_token() -> str | None:
    for env_name in (ENV_TOKEN, LEGACY_ENV_TOKEN):
        token = os.environ.get(env_name)
        if token:
            return token
    return None


def _redact_url(url: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(url)
        query = [
            (key, "***" if key == "api_key" else value)
            for key, value in urllib.parse.parse_qsl(
                parsed.query, keep_blank_values=True
            )
        ]
        return urllib.parse.urlunsplit(
            parsed._replace(query=urllib.parse.urlencode(query))
        )
    except ValueError:
        return url


# Endpoints on the upstream.
_SCRAPER_PATH = "/builder?platform=1"
_SCRAPER_TASK_STATUS_PATH = "/task_status"
_SCRAPER_TASK_RESULT_PATH = "/download"
_SCRAPER_TASK_RESULT_TYPES = {"json", "csv", "xlsx"}
_SERP_PATH = "/request"


class DataifyClient:
    """Synchronous client for the Dataify upstream REST API.

    Parameters
    ----------
    token:
        Dataify API token. If omitted, the ``DATAIFY_API_TOKEN`` environment
        variable is used first, with ``DATAIFY_TOKEN`` kept as a legacy
        fallback. A token is required to make any request.
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
        self.token = token or _read_env_token()
        if not self.token:
            raise ValueError(
                "A Dataify token is required: pass token=... or set the "
                f"{ENV_TOKEN} environment variable (legacy: {LEGACY_ENV_TOKEN})."
            )
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    # ------------------------------------------------------------------
    # Low-level transport
    # ------------------------------------------------------------------
    def _read_response_bytes(self, req: urllib.request.Request, url: str) -> bytes:
        display_url = _redact_url(url)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:  # upstream returned >= 400
            body = exc.read().decode("utf-8", errors="replace")
            raise DataifyAPIError(
                f"Dataify API request failed: {display_url}", exc.code, body
            ) from exc
        except urllib.error.URLError as exc:
            if isinstance(exc.reason, TimeoutError):
                raise DataifyTimeoutError(
                    f"Request to {display_url} timed out after {self.timeout}s"
                ) from exc
            raise DataifyConnectionError(
                f"Could not connect to Dataify API at {display_url}: {exc.reason}"
            ) from exc

    def _read_json_response(
        self, req: urllib.request.Request, url: str
    ) -> Any:
        raw = self._read_response_bytes(req, url).decode(
            "utf-8", errors="replace"
        )
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"raw": raw}

    def _post_form(self, path: str, fields: dict[str, str]) -> dict[str, Any]:
        """POST form-encoded fields and return the parsed JSON response."""
        url = self.base_url + path
        # Only send non-empty values (mirrors the Go upstream behaviour).
        payload = {k: v for k, v in fields.items() if v not in (None, "")}
        data = urllib.parse.urlencode(payload, doseq=False).encode("utf-8")

        req = urllib.request.Request(url, data=data, method="POST")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        req.add_header("Authorization", f"Bearer {self.token}")
        return self._read_json_response(req, url)

    def _get_json(self, path: str, query: dict[str, str]) -> Any:
        """GET a JSON endpoint with query parameters and return parsed JSON."""
        url, req = self._build_get_request(path, query)
        return self._read_json_response(req, url)

    def _get_bytes(self, path: str, query: dict[str, str]) -> bytes:
        """GET an endpoint with query parameters and return response bytes."""
        url, req = self._build_get_request(path, query)
        return self._read_response_bytes(req, url)

    def _build_get_request(
        self, path: str, query: dict[str, str]
    ) -> tuple[str, urllib.request.Request]:
        url = self.base_url + path
        payload = {k: v for k, v in query.items() if v not in (None, "")}
        if payload:
            url = url + "?" + urllib.parse.urlencode(payload, doseq=False)
        return url, urllib.request.Request(url, method="GET")

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

    def query_scraper_task_status(self, task_id: str) -> dict[str, Any]:
        """Query a scraper task status by task ID.

        Parameters
        ----------
        task_id:
            Task ID returned by ``request_scraper``.
        """
        task_id = task_id.strip()
        if not task_id:
            raise ValueError("task_id is required")
        return self._get_json(
            _SCRAPER_TASK_STATUS_PATH,
            {"api_key": self.token, "task_id": task_id},
        )

    def download_scraper_task_result(
        self, task_id: str, result_type: str = "json"
    ) -> Any:
        """Download a scraper task result.

        Parameters
        ----------
        task_id:
            Task ID returned by ``request_scraper``.
        result_type:
            Result format. Supported values are ``"json"``, ``"csv"``, and
            ``"xlsx"``. JSON results are parsed, CSV results are
            returned as text, and XLSX results are returned as bytes.
        """
        task_id = task_id.strip()
        if not task_id:
            raise ValueError("task_id is required")

        result_type = result_type.strip().lower()
        if result_type not in _SCRAPER_TASK_RESULT_TYPES:
            raise ValueError(
                "result_type must be one of: "
                + ", ".join(sorted(_SCRAPER_TASK_RESULT_TYPES))
            )

        fields = {
            "api_key": self.token,
            "task_id": task_id,
            "type": result_type,
        }
        if result_type == "json":
            return self._get_json(_SCRAPER_TASK_RESULT_PATH, fields)

        content = self._get_bytes(_SCRAPER_TASK_RESULT_PATH, fields)
        if result_type == "csv":
            return content.decode("utf-8", errors="replace")
        return content


_DEFAULT_CLIENT: DataifyClient | None = None


def get_default_client() -> DataifyClient:
    """Return a process-wide default :class:`DataifyClient`.

    Uses ``DATAIFY_API_TOKEN`` from the environment, with
    ``DATAIFY_TOKEN`` kept as a legacy fallback. Handy for the generated
    tool functions, which accept an optional ``client`` argument.
    """
    global _DEFAULT_CLIENT
    if _DEFAULT_CLIENT is None:
        _DEFAULT_CLIENT = DataifyClient()
    return _DEFAULT_CLIENT
