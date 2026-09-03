# 获取管理员通讯录权限范围

doc_id: Cc3Z5oksvb
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/user/get_admin_scope
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
- userid (String, required): 管理员的userid，可调用获取管理员列表接口获取当前企业下的管理员ID。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), dept_ids(Number[])

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-permissions-of-the-administrator-address-book
updated_at: 2026-06-08 09:28:41
