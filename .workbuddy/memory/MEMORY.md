# dataify-sdk-python 项目长期记忆

## 项目定位
- 这是 Dataify 的 Python SDK，**直接调用 Dataify 上游 REST 接口**，不走 MCP 协议。
- 参考实现（唯一真相源）：Go 服务 `C:\dataify\dataify_mcp_api`（internal/tools 与 internal/service）。

## 关键约定（稳定）
- 包名：`dataify_sdk`（源码在 `src/dataify_sdk/`）。旧 `src/dataify_mcp`（MCP 协议方向错误）已删除，勿再创建。
- 上游基址写死 `https://scraperapi.dataify.com`；token 经构造函数或环境变量 `DATAIFY_TOKEN` 注入。
- 仅标准库依赖（urllib），**无第三方运行时依赖**。HTTP 为同步。
- 采集类走 `POST /builder?platform=1`；搜索类走 `POST /request`。均带 `Authorization: Bearer <token>`。
- **所有需连接数据库的工具都不做**（task_status / user* / scraper* 统计 / web_unlocker / auth）。
- API 风格：每个 `spider_id` 一个独立 Python 函数；函数签名+docstring 暴露全部上游参数与中文描述。

## 工具生成
- 不要手改 `src/dataify_sdk/tools/*.py`；它们由 `src/dataify_sdk/_codegen/generate.py` 从 Go 项目生成。
- 重新生成：`python scripts/codegen.py`。参数手册输出到 `docs/api_reference.md`。

## 测试
- pytest（开发依赖）。`DataifyClient._post_form` 是 mock 切入点；真实过滤/鉴权逻辑在 `_post_form` 内，
  测试应 mock `urllib.request.urlopen` 而非 `_post_form`。
