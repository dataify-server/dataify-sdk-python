"""AI Web search, map, extract, and download example.

Set ``DATAIFY_API_TOKEN`` before running. AI Web defaults to
``https://aiwebapi.dataify.com``; set ``AI_WEB_API_BASE_URL`` only to override it:

    python examples/ai_web.py
"""

from __future__ import annotations

import os

from dataify_sdk import AI_WEB_UNIQUE_IDS, DataifyClient


def main() -> None:
    client = DataifyClient(token=os.environ.get("DATAIFY_API_TOKEN"))
    query = os.environ.get("DATAIFY_TEST_QUERY", "OpenAI")
    url = os.environ.get("DATAIFY_TEST_URL", "https://example.com")

    search = client.ai_web.search(
        AI_WEB_UNIQUE_IDS.SEARCH_WEB,
        query,
        max_results=3,
        source="web",
    )
    print("search request_id:", search.request_id)
    print("search outputs:", search.outputs)

    mapping = client.ai_web.map(AI_WEB_UNIQUE_IDS.MAP, url, limit=10)
    print("map request_id:", mapping.request_id)
    print("map outputs:", mapping.outputs)

    extract = client.ai_web.extract(
        AI_WEB_UNIQUE_IDS.EXTRACT,
        url,
        formats=["markdown"],
    )
    print("extract request_id:", extract.request_id)
    print("extract outputs:", extract.outputs)

    if extract.request_id:
        downloaded = client.ai_web.download_result(extract.request_id)
        print("downloaded:", downloaded)


if __name__ == "__main__":
    main()
