"""AI Web search, map, extract, and result download helpers.

The AI Web gateway defaults to ``https://aiwebapi.dataify.com``. Override
it with:

* ``ai_web_base_url`` passed to :class:`~dataify_sdk.DataifyClient`, or
* the ``AI_WEB_API_BASE_URL`` environment variable.

Requests use the Dataify Bearer token.  The gateway returns the operation
output as the JSON response body, and the ``X-Request-Id`` response header is
exposed as :attr:`AIWebResponse.request_id`.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from dataify_sdk.errors import DataifyMissingAIWebBaseUrlError

if TYPE_CHECKING:  # pragma: no cover - imported only for type checkers
    from dataify_sdk.client import DataifyClient


class AIWebOperation:
    """Supported AI Web gateway operations."""

    SEARCH = "search"
    MAP = "map"
    EXTRACT = "extract"


class AIWebUniqueIds:
    """Fixed ``unique_id`` values used by the current AI Web gateway."""

    SEARCH_WEB = "search_web"
    SEARCH_SHOPPING = "search_shopping"
    SEARCH_NEWS = "search_news"
    SEARCH_SCHOLAR = "search_scholar"
    MAP = "map"
    EXTRACT = "extract"

    # Lower-case aliases keep the Python API close to the TypeScript SDK.
    search_web = SEARCH_WEB
    search_shopping = SEARCH_SHOPPING
    search_news = SEARCH_NEWS
    search_scholar = SEARCH_SCHOLAR
    map = MAP
    extract = EXTRACT


AI_WEB_UNIQUE_IDS = AIWebUniqueIds


class AIWebFormats:
    """Content formats supported by AI Web extraction."""

    MARKDOWN = "markdown"
    RAW_HTML = "raw_html"
    CLEAN_HTML = "clean_html"
    LINKS = "links"
    ALL = (MARKDOWN, RAW_HTML, CLEAN_HTML, LINKS)


AI_WEB_FORMATS = AIWebFormats.ALL

_AI_WEB_PATHS = {
    AIWebOperation.SEARCH: "/search",
    AIWebOperation.MAP: "/map",
    AIWebOperation.EXTRACT: "/extract",
}
_AI_WEB_FORMAT_SET = frozenset(AIWebFormats.ALL)


@dataclass(frozen=True)
class AIWebResponse:
    """Result of an AI Web operation.

    Attributes
    ----------
    request_id:
        Trimmed ``X-Request-Id`` response header, or ``None`` when the header
        is absent.
    outputs:
        Normalized output for the convenience methods, or the exact upstream
        JSON body for :meth:`AIWebService.execute_raw`.
    """

    request_id: str | None
    outputs: Any


def normalize_ai_web_outputs(outputs: Any) -> list[Any]:
    """Normalize an AI Web response body to a list.

    ``None`` becomes ``[]``; JSON arrays stay arrays; a single object or
    primitive is wrapped in a one-element list.
    """

    if outputs is None:
        return []
    if isinstance(outputs, list):
        return list(outputs)
    if isinstance(outputs, tuple):
        return list(outputs)
    return [outputs]


class AIWebService:
    """AI Web operations exposed as ``client.ai_web``."""

    def __init__(self, client: DataifyClient) -> None:
        self._client = client

    # ------------------------------------------------------------------
    # Convenience methods
    # ------------------------------------------------------------------
    def search(
        self,
        unique_id: str,
        query: str,
        *,
        max_results: int | None = None,
        source: str | None = None,
        country: str | None = None,
        language: str | None = None,
        time_range: str | None = None,
        extract_content: bool | None = None,
        extract_options: Mapping[str, Any] | None = None,
    ) -> AIWebResponse:
        """Run an AI Web search.

        Parameters
        ----------
        unique_id:
            Gateway tool identifier.  Use :class:`AIWebUniqueIds`, for example
            ``AI_WEB_UNIQUE_IDS.SEARCH_NEWS``.
        query:
            Search terms.
        max_results:
            Maximum number of results (upstream default: 10).
        source:
            Search source such as ``"news"``, ``"shopping"`` or ``"scholar"``.
        country:
            Two-letter uppercase country code, for example ``"US"``.
        language:
            Interface language code, for example ``"en"``.
        time_range:
            One of ``"hour"``, ``"day"``, ``"week"``, ``"month"``, ``"year"``.
        extract_content:
            Extract the content of each result page on the server side.
        extract_options:
            Options used when ``extract_content`` is true.
        """

        payload = _build_payload(
            unique_id,
            query=query,
            max_results=max_results,
            source=source,
            country=country,
            language=language,
            time_range=time_range,
            extract_content=extract_content,
            extract_options=_compact_mapping(extract_options),
        )
        return self.execute(AIWebOperation.SEARCH, payload)

    def map(
        self,
        unique_id: str,
        url: str,
        *,
        country: str | None = None,
        domain_filter: str | None = None,
        limit: int | None = None,
        sitemap: str | None = None,
    ) -> AIWebResponse:
        """Discover URLs for a site (``POST /map``)."""

        payload = _build_payload(
            unique_id,
            url=url,
            country=country,
            domain_filter=domain_filter,
            limit=limit,
            sitemap=sitemap,
        )
        return self.execute(AIWebOperation.MAP, payload)

    def extract(
        self,
        unique_id: str,
        url: str,
        *,
        formats: Sequence[str] | str | None = None,
        only_main_content: bool | None = None,
        include_tags: Sequence[str] | str | None = None,
        exclude_tags: Sequence[str] | str | None = None,
        headers: Mapping[str, str] | None = None,
        max_age_ms: int | None = None,
        timeout_ms: int | None = None,
        wait_for_ms: int | None = None,
        country: str | None = None,
        advanced_mode: bool | None = None,
    ) -> AIWebResponse:
        """Extract page content (``POST /extract``)."""

        payload = _build_payload(
            unique_id,
            url=url,
            formats=_validate_formats(formats),
            only_main_content=only_main_content,
            include_tags=_validate_string_list("include_tags", include_tags),
            exclude_tags=_validate_string_list("exclude_tags", exclude_tags),
            headers=_validate_headers(headers),
            max_age_ms=max_age_ms,
            timeout_ms=timeout_ms,
            wait_for_ms=wait_for_ms,
            country=country,
            advanced_mode=advanced_mode,
        )
        return self.execute(AIWebOperation.EXTRACT, payload)

    # ------------------------------------------------------------------
    # Dynamic execution
    # ------------------------------------------------------------------
    def execute(self, operation: str, params: Mapping[str, Any]) -> AIWebResponse:
        """Run an operation and normalize ``outputs`` to a list."""

        response = self.execute_raw(operation, params)
        return AIWebResponse(
            request_id=response.request_id,
            outputs=normalize_ai_web_outputs(response.outputs),
        )

    def execute_raw(
        self, operation: str, params: Mapping[str, Any]
    ) -> AIWebResponse:
        """Run an operation and preserve the exact upstream output shape."""

        path = _operation_path(operation)
        payload = _prepare_execute_payload(operation, params)
        data, headers = self._client._post_json_with_headers(
            self._resolve_base_url(), path, payload
        )
        return AIWebResponse(
            request_id=_normalize_request_id(headers.get("x-request-id")),
            outputs=data,
        )

    def download_result(self, task_id: str) -> Any:
        """Download a retained AI Web result by ``task_id`` (``POST /download``)."""

        task_id = _require_string("task_id", task_id)
        data, _headers = self._client._post_json_with_headers(
            self._resolve_base_url(), "/download", {"task_id": task_id}
        )
        return data

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _resolve_base_url(self) -> str:
        base_url = (getattr(self._client, "ai_web_base_url", "") or "").rstrip("/")
        if not base_url:
            raise DataifyMissingAIWebBaseUrlError()
        return base_url


# ----------------------------------------------------------------------
# Validation and payload helpers
# ----------------------------------------------------------------------
def _build_payload(unique_id: str, **fields: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "unique_id": _require_string("unique_id", unique_id)
    }
    for key, value in fields.items():
        if isinstance(value, str):
            value = value.strip()
            if not value:
                continue
        if value is not None:
            payload[key] = value
    return payload


def _compact_mapping(value: Mapping[str, Any] | None) -> dict[str, Any] | None:
    if value is None:
        return None
    if not isinstance(value, Mapping):
        raise TypeError("extract_options must be a mapping")
    return {str(key): item for key, item in value.items() if item is not None}


def _prepare_execute_payload(
    operation: str, params: Mapping[str, Any]
) -> dict[str, Any]:
    if not isinstance(params, Mapping):
        raise TypeError("params must be a mapping")

    payload = dict(params)
    payload["unique_id"] = _require_string("unique_id", payload.get("unique_id"))

    normalized_operation = _normalize_operation(operation)
    if normalized_operation == AIWebOperation.SEARCH:
        payload["query"] = _require_string("query", payload.get("query"))
        if payload.get("extract_options") is not None:
            payload["extract_options"] = _prepare_extract_options(
                payload["extract_options"]
            )
    else:
        payload["url"] = _require_string("url", payload.get("url"))
        if normalized_operation == AIWebOperation.EXTRACT:
            if "formats" in payload:
                payload["formats"] = _validate_formats(payload.get("formats"))
            if "include_tags" in payload:
                payload["include_tags"] = _validate_string_list(
                    "include_tags", payload.get("include_tags")
                )
            if "exclude_tags" in payload:
                payload["exclude_tags"] = _validate_string_list(
                    "exclude_tags", payload.get("exclude_tags")
                )
            if "headers" in payload:
                payload["headers"] = _validate_headers(payload.get("headers"))

    return {key: value for key, value in payload.items() if value is not None}


def _prepare_extract_options(value: Mapping[str, Any]) -> dict[str, Any]:
    options = _compact_mapping(value)
    if options is None:
        return {}
    if "formats" in options:
        options["formats"] = _validate_formats(options.get("formats"))
    return {key: item for key, item in options.items() if item is not None}


def _validate_formats(formats: Any) -> list[str] | None:
    if formats is None:
        return None
    if isinstance(formats, str):
        formats = [formats]
    if not isinstance(formats, Sequence) or isinstance(formats, (bytes, bytearray)):
        raise TypeError("formats must be a sequence of strings")

    values: list[str] = []
    for item in formats:
        if not isinstance(item, str):
            raise TypeError("formats must contain only strings")
        value = item.strip()
        if value not in _AI_WEB_FORMAT_SET:
            raise ValueError(
                "formats must be one of: " + ", ".join(AIWebFormats.ALL)
            )
        values.append(value)

    if len(set(values)) != len(values):
        raise ValueError("formats must not contain duplicates")
    return values


def _validate_string_list(name: str, values: Any) -> list[str] | None:
    if values is None:
        return None
    if isinstance(values, str):
        values = [values]
    if not isinstance(values, Sequence) or isinstance(values, (bytes, bytearray)):
        raise TypeError(f"{name} must be a sequence of strings")

    result: list[str] = []
    for item in values:
        if not isinstance(item, str) or not item.strip():
            raise TypeError(f"{name} must contain non-empty strings")
        result.append(item)
    return result


def _validate_headers(headers: Any) -> dict[str, str] | None:
    if headers is None:
        return None
    if not isinstance(headers, Mapping):
        raise TypeError("headers must be a mapping")
    result: dict[str, str] = {}
    for key, value in headers.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("headers must contain string keys and values")
        result[key] = value
    return result


def _normalize_operation(operation: str) -> str:
    if not isinstance(operation, str):
        raise TypeError("operation must be a string")
    normalized = operation.strip().lower()
    if normalized not in _AI_WEB_PATHS:
        raise ValueError(f"Unsupported AI Web operation: {operation!r}")
    return normalized


def _operation_path(operation: str) -> str:
    return _AI_WEB_PATHS[_normalize_operation(operation)]


def _require_string(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} is required")
    return value.strip()


def _normalize_request_id(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    value = value.strip()
    return value or None
