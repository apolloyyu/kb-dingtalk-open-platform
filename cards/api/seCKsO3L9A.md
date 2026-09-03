# 获取客户管理全局信息

doc_id: seCKsO3L9A
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/globalInfos
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 用户userId。

## Body
- none

## Returns
- optional: result(Object), oemEnable(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-customer-management-global-information
updated_at: 2026-06-03 09:36:56
