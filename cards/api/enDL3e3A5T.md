# 删除用户

doc_id: enDL3e3A5T
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/delete
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_manage_addresslist

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 员工的userid。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-a-user
updated_at: 2026-06-08 09:28:30
