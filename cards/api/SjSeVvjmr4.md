# 获取个人或企业客户查重字段

doc_id: SjSeVvjmr4
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/relationUkSettings
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- relationType (String, required): 客户类型。 - **crm_customer**：企业客户 - **crm_customer_personal**：个人客户

## Body
- none

## Returns
- optional: result(Array), fieldId(String), bizAlias(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-duplicate-check-fields
updated_at: 2026-06-04 19:12:10
