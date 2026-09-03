# 获取企业的e签宝微应用状态

doc_id: vCZUym0oJa
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/esign/corps/appStatus
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: installStatus(String), authStatus(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-current-status-of-the-company-s-e-sign-micro-application
updated_at: 2026-06-04 19:11:07
