# 获取应用管理后台免登的用户信息

doc_id: mtvC5AWzKo
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/sso/getuserinfo
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- code (String, required): 通过Oauth认证给URL带上的code。
- access_token (String, required): 调用该API的应用凭证，可调用获取微应用后台免登的accessToken接口获取。

## Body
- none

## Returns
- optional: user_info(UserInfo), avatar(String), email(String), name(String), userid(String), corp_info(CorpInfo), corp_name(String), corpid(String), is_sys(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/exchange-code-for-the-identity-information-of-a-microapplication-administrator
updated_at: 2026-08-25 09:36:34
