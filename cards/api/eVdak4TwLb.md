# 获取企业e签宝微应用状态

doc_id: eVdak4TwLb
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/corps/statuses
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
- none

## Returns
- optional: data(Object), authStatus(String), installStatus(String), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-status-of-enterprise-e-sign-treasure-micro-application
updated_at: 2026-08-25 09:37:26
