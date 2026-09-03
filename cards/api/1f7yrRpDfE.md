# 删除用户

doc_id: 1f7yrRpDfE
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/delete
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API授权凭证，通过获取企业内部应用的access_token接口获取。
- userid (String, required): 员工唯一标识userid，可通过根据手机号查询用户接口获取userid。

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-a-member
updated_at: 2026-08-25 09:36:50
