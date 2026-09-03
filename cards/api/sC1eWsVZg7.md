# 查询用户是否参与企业步数排行榜

doc_id: sC1eWsVZg7
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/health/stepinfo/getuserstatus
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_health_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 要查询的用户userId。

## Returns
- optional: errcode(Number), request_id(String), status(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/check-whether-dingtalk-is-enabled
updated_at: 2026-06-01 09:15:27
