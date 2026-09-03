# 获取应用未激活的企业列表

doc_id: bDd1OaC8fS
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/service/get_unactive_corp
api_version: v1-oapi
app_types: 第三方企业应用
permissions: isvapi_base

## Request headers
- none

## Path params
- none

## Query params
- suite_access_token (String, required): 第三方企业应用的suite_access_token，可调用获取第三方企业应用的suiteAccessToken接口获取凭证。

## Body
- optional: app_id(Number)

## Returns
- optional: app_id(Number), corp_list(String[]), has_more(Boolean), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-enterprises-whose-applications-are-not-activated
updated_at: 2026-07-02 10:35:38
