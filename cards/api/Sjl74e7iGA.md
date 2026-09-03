# 获取微应用后台免登的access_token

doc_id: Sjl74e7iGA
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/sso/gettoken
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- corpid (String, required): 企业的corpid。
- corpsecret (String, required): 可以在钉钉开发者后台的**基本信息 > 开发信息（旧版**）页面获取**微应用管理后台SSOSecret**。 如下图所示：SSO获取途径

## Body
- none

## Returns
- optional: access_token(String), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-ssotoken-for-micro-application-background-logon-free
updated_at: 2026-08-25 09:36:33
