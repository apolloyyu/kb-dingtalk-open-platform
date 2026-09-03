# 激活应用

doc_id: cFUFmjZjB5
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/service/activate_suite
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- suite_access_token (String, required): 第三方应用的suite_access_token，可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- suite_key (String, required): 第三方应用的SuiteKey。 可在钉钉开发者后台的第三方应用详情页面获取。
- auth_corpid (String, required): 授权企业的CorpId。 HTTP回调事件中推送的CorpId。
- permanent_code (Sting, required): 授权企业的永久授权码。 通过获取授权企业的永久授权码接口获取。

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/activate-suite
updated_at: 2026-09-02 18:13:44
