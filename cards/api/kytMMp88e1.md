# 获取用户授权的持久授权码

doc_id: kytMMp88e1
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/sns/get_persistent_code
api_version: v1-oapi
app_types: 第三方个人应用
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- optional: access_token(unknown)

## Body
- optional: tmp_auth_code(String)

## Returns
- optional: persistent_code(String), openid(String), unionid(String), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/persistent-authorization-code
updated_at: 2026-06-30 16:49:02
