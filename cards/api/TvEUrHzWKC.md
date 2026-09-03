# 更新文章

doc_id: TvEUrHzWKC
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/material/article/update
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
- article (ArticleCreateDTO, required): 文章参数对象。
- content (String, required): 文章内容（html格式）。
- title (String, required): 文章标题。
- article_id (Number, required): 文章id，可以通过查询文章列表接口获取。
- optional: thumb_media_id(String), digest(String)

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/save-article-details-1
updated_at: 2026-06-01 09:15:45
