# 根据手机号查询用户

doc_id: JrHCzSHRjF
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/get_by_mobile
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。
- mobile (String, required): 要获取的用户手机号。

## Body
- none

## Returns
- optional: userid(String), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/retrieve-userid-from-mobile-phone-number
updated_at: 2026-08-25 09:36:56
