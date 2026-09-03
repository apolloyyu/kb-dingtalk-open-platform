# 获取用户待审批数量

doc_id: hy9R3UELUe
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/gettodonum
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 要查询的用户userid。

## Returns
- optional: count(Number), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-number-of-tasks-to-be-approved-by-me
updated_at: 2026-08-25 09:37:45
