# 查询文章列表

doc_id: 8Vqt8rPDem
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/material/article/list
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_service_account_materials

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- unionid (String, required): 服务号的unionid，可通过查询服务号列表接口获取。
- page_size (Number, required): 每页条数。
- page_start (Number, required): 页码。
- optional: publishStatus(Number), status(Number)

## Returns
- optional: items(ArticleDTO[]), article_id(Number), title(String), thumb_media_id(String), publish_status(Number), publish_time(Number), create_time(Number), update_time(Number), content(String), url(String), digest(String), total_count(Number), errcode(Number), errmsg(String), item_count(Number), request_id(String)

## Limits
- 发布状态： - **0**：未发布 - **1**：已发布 **[!NOTE]** 文章第一次发布后，状态置为1，已发布文章支持修改，修改后此状态保持为1，每次修改文章后需要再次发布内容才会生效。

source_url: https://open.dingtalk.com/document/development/query-the-article-list
updated_at: 2026-06-01 09:15:41
