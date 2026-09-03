# 发布文章

doc_id: MILeA9RcEe
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/material/article/publish
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
- article_id (Number, required): 文章id，可以通过查询文章列表接口获取。

## Returns
- optional: url(String), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/article-publishing-interface-1
updated_at: 2026-06-01 09:15:43
