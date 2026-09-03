# 获取管理员列表

doc_id: I7F8cy4Y1o
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/user/listadmin
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- none

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(ListAdminResponse[]), userid(String), sys_level(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-administrator-list
updated_at: 2026-06-08 09:28:40
