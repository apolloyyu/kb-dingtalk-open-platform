# 获取审批中创建与CRM客户关联的TAB表单元数据

doc_id: 3nHvbYlut9
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/formRelatedTabs/meta/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_customdata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- formCode (String, required): 个人客户或者企业客户的表单代码 。
- viewUserId (String, required): 企业内的用户 userid。

## Returns
- optional: results(Array), formCode(String), relateComponentId(String), tabTitle(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getrelatedviewtabmeta
updated_at: 2026-06-03 09:36:58
