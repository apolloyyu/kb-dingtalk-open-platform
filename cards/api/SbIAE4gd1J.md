# 获取图文卡片详情

doc_id: SbIAE4gd1J
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/material/news/get
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
- media_id (String, required): 图文卡片素材id，可以通过查询图文卡片列表接口获取。

## Returns
- optional: errmsg(String), errcode(Number), request_id(String), media_id(String), update_time(Number), articles(ArticleDTO[]), article_id(Number), title(String), content(String), thumb_media_id(String), publish_status(Number), publish_time(Number), user_view_count(Number), total_view_count(Number), create_time(Number), url(String), digest(String)

## Limits
- 发布状态： - **0**：未发布 - **1**：已发布 **[!NOTE]** 文章第一次发布后，状态为1，已发布文章支持修改，修改后此状态保持为1，每次修改文章后需要再次发布内容才会生效。

source_url: https://open.dingtalk.com/document/development/get-message-card-details
updated_at: 2026-06-01 09:15:48
