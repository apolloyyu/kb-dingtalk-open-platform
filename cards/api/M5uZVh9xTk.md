# 删除图文卡片

doc_id: M5uZVh9xTk
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/material/news/delete
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
- optional: errmsg(String), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-message-card
updated_at: 2026-06-01 09:15:44
