# ISV服务商数据初始化

doc_id: 75pQ3ufnaI
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/developers/create
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: redirectUrl(String)

## Returns
- optional: code(Integer), message(String), data(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/offline-isv-service-provider-data-initialization
updated_at: 2026-08-25 09:37:24
