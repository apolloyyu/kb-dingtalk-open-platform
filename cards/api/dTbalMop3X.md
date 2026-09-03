# 获取微应用后台免登的accessToken

doc_id: dTbalMop3X
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/oauth2/ssoAccessToken
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- corpid (String, required): 企业的corpId。
- ssoSecret (String, required): sso密钥，可以在开发者后台**基本信息**—**开发信息**（**旧版**）页面查看。

## Returns
- optional: accessToken(String), expireIn(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-access-token-of-the-micro-application-background-without-log-on
updated_at: 2026-04-29 22:27:34
