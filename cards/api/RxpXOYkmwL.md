# 获取第三方个人应用的access_token

doc_id: RxpXOYkmwL
completeness: full
archived: false
method: GET
endpoint: https://oapi.dingtalk.com/sns/gettoken
api_version: v1-oapi
app_types: 第三方个人应用
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- appid (String, required): 创建的第三方个人应用的标识，详情参考创建和配置应用。
- appsecret (String, required): 创建的第三方个人应用的密钥。appid和appsecret可在钉钉开发者后台的应用详情页面获取。

## Returns
- optional: access_token(String), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-personal-application
updated_at: 2026-04-29 22:27:40
