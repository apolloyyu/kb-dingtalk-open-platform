# 新增图文卡片

doc_id: zFrsUpiT4s
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/material/news/add
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
- articles (ArticleDTO[], required): 文章列表。
- article_id (Number, required): 文章id，可以通过查询文章列表接口获取。

## Returns
- optional: errmsg(String), media_id(String), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/new-message-card-1
updated_at: 2026-06-03 09:48:37
