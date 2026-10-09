"""Tests that the generated tool layer imports and builds correct requests."""

from __future__ import annotations

import importlib
import json
from pathlib import Path

import pytest

from dataify_sdk import DataifyClient
from tests.conftest import decode_form

TOOLS_DIR = Path(__file__).resolve().parents[2] / "src" / "dataify_sdk" / "tools"


def _all_modules():
    return sorted(
        p.name[:-3] for p in TOOLS_DIR.glob("*.py") if p.name != "__init__.py"
    )


@pytest.mark.parametrize("module", _all_modules())
def test_module_imports(module):
    importlib.import_module(f"dataify_sdk.tools.{module}")


def test_function_count():
    mods = _all_modules()
    assert len(mods) == 71
    import dataify_sdk.tools as pkg

    assert len(pkg.__all__) == 115


def test_amazon_product_by_asin_request(captured_request):
    from dataify_sdk.tools.amazonproduct import amazon_product_by_asin

    amazon_product_by_asin(asin="B0X", client=DataifyClient(token="t"))
    req = captured_request["req"]
    assert req.full_url.endswith("/builder?platform=1")
    form = decode_form(req)
    assert form["spider_id"] == "amazon_product_by-asin"
    assert form["spider_name"] == "amazon.com"
    assert json.loads(form["spider_parameters"]) == [{"asin": "B0X"}]


def test_chatgpt_answer_by_url_request(captured_request):
    from dataify_sdk.tools.chatgptanswer import chatgpt_answer_by_url

    chatgpt_answer_by_url(
        chatgpt_url="https://chatgpt.com/?q=pizza", client=DataifyClient(token="t")
    )
    req = captured_request["req"]
    assert req.full_url.endswith("/builder?platform=1")
    form = decode_form(req)
    assert form["spider_id"] == "chatgpt_answer_by-url"
    assert form["spider_name"] == "chatgpt.com"
    assert json.loads(form["spider_parameters"]) == [
        {"chatgpt_url": "https://chatgpt.com/?q=pizza"}
    ]


def test_chatgpt_answer_by_keywords_request(captured_request):
    from dataify_sdk.tools.chatgptanswer import chatgpt_answer_by_keywords

    chatgpt_answer_by_keywords(search_terms="pizza", client=DataifyClient(token="t"))
    req = captured_request["req"]
    assert req.full_url.endswith("/builder?platform=1")
    form = decode_form(req)
    assert form["spider_id"] == "chatgpt_answer_by-keywords"
    assert form["spider_name"] == "chatgpt.com"
    assert json.loads(form["spider_parameters"]) == [{"search_terms": "pizza"}]


def test_google_search_request(captured_request):
    from dataify_sdk.tools.googlesearch import google_search

    google_search(q="pizza", client=DataifyClient(token="t"))
    req = captured_request["req"]
    assert req.full_url.endswith("/request")
    form = decode_form(req)
    assert form["engine"] == "google"
    assert form["q"] == "pizza"
    assert "gl" not in form  # empty dropped


def test_default_client_uses_env(monkeypatch, captured_request):
    monkeypatch.setenv("DATAIFY_API_TOKEN", "env-token")
    from dataify_sdk.tools.twitterpost import twitter_post_by_profileurl

    # no client passed -> default client reads DATAIFY_API_TOKEN
    twitter_post_by_profileurl(url="https://x.com/foo")
    req = captured_request["req"]
    assert req.full_url.endswith("/builder?platform=1")
    form = decode_form(req)
    assert json.loads(form["spider_parameters"]) == [{"url": "https://x.com/foo"}]
    assert req.get_header("Authorization") == "Bearer env-token"
