# 重新授权未激活应用的企业

doc_id: YdbBqjemf4
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/service/reauth_corp
api_version: v1-oapi
app_types: 第三方企业应用
permissions: isvapi_base

## Request headers
- none

## Path params
- none

## Query params
- suite_access_token (String, required): 第三方企业应用的suite_access_token，可调用获取第三方企业应用的suite_access_token接口获取。

## Body
- optional: app_id(String), corpid_list(String[])

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/re-authorize-enterprises-whose-applications-are-not-activated
updated_at: 2026-04-29 22:27:46
