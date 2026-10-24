"""Tests for the AI Web service."""

from __future__ import annotations

import io
import json
import urllib.error
import urllib.request
from types import SimpleNamespace

import pytest

from dataify_sdk import (
    AI_WEB_UNIQUE_IDS,
    DEFAULT_AI_WEB_BASE_URL,
    DataifyAPIError,
    DataifyClient,
    DataifyMissingAIWebBaseUrlError,
    normalize_ai_web_outputs,
)


class _FakeResponse:
    def __init__(self, body: str | bytes, headers: dict[str, str] | None = None) -> None:
        self._body = body.encode("utf-8") if isinstance(body, str) else body
        self.headers = headers or {}

    def read(self) -> bytes:
        return self._body

    def __enter__(self) -> "_FakeResponse":
        return self

    def __exit__(self, *exc: object) -> bool:
        return False


@pytest.fixture
def ai_web_server(monkeypatch):
    calls: list[urllib.request.Request] = []
    responses: list[tuple[str | bytes, dict[str, str]]] = []

    def _fake_urlopen(req: urllib.request.Request, timeout: int | None = None):
        calls.append(req)
        body, headers = responses.pop(0) if responses else ('{"ok": true}', {})
        return _FakeResponse(body, headers)

    monkeypatch.setattr(urllib.request, "urlopen", _fake_urlopen)
    return SimpleNamespace(calls=calls, responses=responses)


def _client(**kwargs) -> DataifyClient:
    return DataifyClient(
        token="api-key",
        ai_web_base_url="https://ai-web.example",
        **kwargs,
    )


def _body(req: urllib.request.Request) -> dict:
    assert req.data is not None
    return json.loads(req.data.decode("utf-8"))


def test_search_posts_json_and_normalizes_response(ai_web_server):
    ai_web_server.responses.append(
        ('[{"title": "OpenAI"}]', {"X-Request-Id": " req-1 "})
    )

    response = _client().ai_web.search(
        AI_WEB_UNIQUE_IDS.SEARCH_NEWS,
        "OpenAI",
        max_results=3,
        source="news",
        extract_options={
            "formats": ["markdown"],
            "only_main_content": True,
        },
    )

    req = ai_web_server.calls[0]
    assert req.full_url == "https://ai-web.example/search"
    assert req.get_header("Authorization") == "Bearer api-key"
    assert req.get_header("Content-type") == "application/json"
    assert _body(req) == {
        "unique_id": "search_news",
        "query": "OpenAI",
        "max_results": 3,
        "source": "news",
        "extract_options": {
            "formats": ["markdown"],
            "only_main_content": True,
        },
    }
    assert response.request_id == "req-1"
    assert response.outputs == [{"title": "OpenAI"}]


def test_web_search_uses_search_web_identity(ai_web_server):
    ai_web_server.responses.append(("[]", {}))

    result = _client().ai_web.search(
        AI_WEB_UNIQUE_IDS.SEARCH_WEB,
        "OpenAI",
        source="web",
    )

    assert AI_WEB_UNIQUE_IDS.search_web == "search_web"
    assert result.outputs == []
    assert _body(ai_web_server.calls[0]) == {
        "unique_id": "search_web",
        "query": "OpenAI",
        "source": "web",
    }


def test_map_and_extract_normalize_null_and_object(ai_web_server):
    ai_web_server.responses.extend(
        [
            ("null", {}),
            (
                '{"markdown": "# Example", "links": ["https://example.com"]}',
                {},
            ),
        ]
    )

    client = _client()
    map_response = client.ai_web.map(
        AI_WEB_UNIQUE_IDS.MAP, "https://example.com", limit=100
    )
    extract_response = client.ai_web.extract(
        AI_WEB_UNIQUE_IDS.EXTRACT,
        "https://example.com/article",
        formats=["markdown", "links"],
    )

    assert map_response.request_id is None
    assert map_response.outputs == []
    assert extract_response.outputs == [
        {"markdown": "# Example", "links": ["https://example.com"]}
    ]
    assert ai_web_server.calls[0].full_url == "https://ai-web.example/map"
    assert ai_web_server.calls[1].full_url == "https://ai-web.example/extract"


def test_execute_raw_preserves_upstream_shape(ai_web_server):
    ai_web_server.responses.append(('{"markdown": "# Example"}', {"x-request-id": "req-raw"}))

    response = _client().ai_web.execute_raw(
        "extract",
        {
            "unique_id": AI_WEB_UNIQUE_IDS.EXTRACT,
            "url": "https://example.com",
        },
    )

    assert response.request_id == "req-raw"
    assert response.outputs == {"markdown": "# Example"}


def test_download_result_posts_task_id_with_bearer_auth(ai_web_server):
    ai_web_server.responses.append(('{"markdown": "# Downloaded"}', {}))

    response = _client().ai_web.download_result(" task-123 ")

    req = ai_web_server.calls[0]
    assert req.full_url == "https://ai-web.example/download"
    assert req.get_header("Authorization") == "Bearer api-key"
    assert _body(req) == {"task_id": "task-123"}
    assert response == {"markdown": "# Downloaded"}


def test_invalid_operation_and_missing_required_fields():
    client = _client()

    with pytest.raises(ValueError, match="Unsupported AI Web operation"):
        client.ai_web.execute("unknown", {"unique_id": "x"})

    with pytest.raises(ValueError, match="query is required"):
        client.ai_web.search(AI_WEB_UNIQUE_IDS.SEARCH_NEWS, "   ")

    with pytest.raises(ValueError, match="url is required"):
        client.ai_web.extract(AI_WEB_UNIQUE_IDS.EXTRACT, "")

    with pytest.raises(ValueError, match="formats must be one of"):
        client.ai_web.extract(
            AI_WEB_UNIQUE_IDS.EXTRACT,
            "https://example.com",
            formats=["pdf"],
        )


def test_ai_web_defaults_to_production_base_url(monkeypatch, ai_web_server):
    monkeypatch.delenv("AI_WEB_API_BASE_URL", raising=False)
    ai_web_server.responses.append(("[]", {}))

    client = DataifyClient(token="api-key")
    client.ai_web.search(AI_WEB_UNIQUE_IDS.SEARCH_NEWS, "OpenAI")

    assert client.ai_web_base_url == DEFAULT_AI_WEB_BASE_URL
    assert ai_web_server.calls[0].full_url == "https://aiwebapi.dataify.com/search"


def test_empty_ai_web_base_url_raises_before_request(monkeypatch):
    monkeypatch.delenv("AI_WEB_API_BASE_URL", raising=False)
    client = DataifyClient(token="api-key")
    client.ai_web_base_url = ""

    with pytest.raises(DataifyMissingAIWebBaseUrlError):
        client.ai_web.search(AI_WEB_UNIQUE_IDS.SEARCH_NEWS, "OpenAI")


def test_ai_web_base_url_defaults_and_overrides(monkeypatch):
    monkeypatch.delenv("AI_WEB_API_BASE_URL", raising=False)
    assert DataifyClient(token="t").ai_web_base_url == DEFAULT_AI_WEB_BASE_URL

    monkeypatch.setenv("AI_WEB_API_BASE_URL", "https://env-ai-web.example/")
    assert DataifyClient(token="t").ai_web_base_url == "https://env-ai-web.example"

    assert (
        DataifyClient(
            token="t", ai_web_base_url="https://explicit.example/"
        ).ai_web_base_url
        == "https://explicit.example"
    )


def test_normalize_ai_web_outputs():
    assert normalize_ai_web_outputs(None) == []
    assert normalize_ai_web_outputs([1, 2]) == [1, 2]
    assert normalize_ai_web_outputs({"a": 1}) == [{"a": 1}]


def test_ai_web_http_error_propagates(monkeypatch):
    def _raise_http_error(req: urllib.request.Request, timeout: int | None = None):
        raise urllib.error.HTTPError(
            req.full_url,
            401,
            "Unauthorized",
            {},
            io.BytesIO(b'{"message": "invalid"}'),
        )

    monkeypatch.setattr(urllib.request, "urlopen", _raise_http_error)
    client = _client()

    with pytest.raises(DataifyAPIError) as exc:
        client.ai_web.search(AI_WEB_UNIQUE_IDS.SEARCH_NEWS, "OpenAI")

    assert exc.value.status_code == 401
