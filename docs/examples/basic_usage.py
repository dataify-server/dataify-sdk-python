"""Basic usage examples for the Dataify SDK (direct REST, no MCP)."""

from dataify_sdk import DataifyClient, DataifyAPIError, DataifyConnectionError
from dataify_sdk.tools.amazonproduct import amazon_product_by_asin
from dataify_sdk.tools.googlesearch import google_search
from dataify_sdk.tools.twitterpost import twitter_post_by_profileurl

TOKEN = "your-api-token"  # 也可通过环境变量 DATAIFY_TOKEN 提供


def example_amazon_product():
    """采集 Amazon 产品详情（直接提交 Builder 任务）。"""
    client = DataifyClient(token=TOKEN)
    result = amazon_product_by_asin(asin="B0BZYCJK89", client=client)
    print(result)


def example_google_search():
    """执行 Google 搜索（直接打搜索引擎接口）。"""
    client = DataifyClient(token=TOKEN)
    result = google_search(q="Python 编程", gl="cn", hl="zh-cn", client=client)
    print(result)


def example_twitter_post():
    """采集 Twitter/X 帖子信息。"""
    client = DataifyClient(token=TOKEN)
    result = twitter_post_by_profileurl(url="https://x.com/elonmusk", client=client)
    print(result)


def example_error_handling():
    """错误处理示例。"""
    client = DataifyClient(token=TOKEN)
    try:
        google_search(q="test", client=client)
    except DataifyAPIError as e:
        print(f"上游返回错误 HTTP {e.status_code}: {e.body}")
    except DataifyConnectionError:
        print("无法连接 Dataify 上游")


def main():
    print("=" * 60)
    print("Dataify SDK — 使用示例（直接调用上游 REST，无 MCP）")
    print("=" * 60)
    print("提示: 修改 TOKEN 后运行各示例函数。")
    print("完整参数见 docs/api_reference.md。")


if __name__ == "__main__":
    main()
