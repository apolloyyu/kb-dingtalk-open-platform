# 通过免登码获取用户信息（不推荐）

doc_id: n1Al2zCrny
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/getuserinfo
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。
- code (String, required): 免登授权码。

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String), userid(String), name(String), deviceId(String), is_sys(Boolean), sys_level(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-user-userid-through-login-free-code
updated_at: 2026-08-25 09:36:35
