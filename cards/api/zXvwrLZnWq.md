# 根据手机号查询用户

doc_id: zXvwrLZnWq
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/getbymobile
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_get_member_by_mobile

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- mobile (String, required): 用户的手机号。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(Object), userid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-users-by-phone-number
updated_at: 2026-06-08 09:28:38
