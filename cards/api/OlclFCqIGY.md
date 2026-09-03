# 查询服务号列表

doc_id: OlclFCqIGY
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/serviceaccount/list
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_service_account_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- optional: pageStart(Number), pageSize(Number)

## Returns
- optional: request_id(String), errmsg(String), errcode(Number), total_count(Number), item_count(Number), items(PublisherDTO[]), desc(String), preview_media_id(String), brief(String), avatar_media_id(String), name(String), status(String), unionid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-service-number-list
updated_at: 2026-06-01 09:15:32
