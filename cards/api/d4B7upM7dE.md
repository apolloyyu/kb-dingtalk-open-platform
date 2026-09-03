# 获取管理员列表

doc_id: d4B7upM7dE
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/get_admin
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- none

## Returns
- optional: errmsg(String), errcode(Number), adminList(AdminList[]), sys_level(Number), userid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-administrators
updated_at: 2026-08-25 09:36:57
