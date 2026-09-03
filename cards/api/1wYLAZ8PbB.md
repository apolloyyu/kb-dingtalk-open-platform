# 获取应用管理后台免登的用户信息

doc_id: 1wYLAZ8PbB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/oauth2/ssoUserInfo
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_omp_sso_userinfo

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，这里需要使用微应用后台免登的access_token，可以通过调用获取微应用后台免登的accessToken接口获取。

## Path params
- none

## Query params
- code (String, required): 临时授权码，管理员在钉钉管理后台，跳转到应用管理页面时，该授权码会附带在URL中。

## Body
- none

## Returns
- optional: corpId(String), corpName(String), userId(String), email(String), userName(String), avatar(String), isAdmin(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-identity-of-an-application-administrator
updated_at: 2026-04-29 22:27:35
