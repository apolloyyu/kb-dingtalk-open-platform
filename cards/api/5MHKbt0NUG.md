# 获取个人或企业客户的元数据

doc_id: 5MHKbt0NUG
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/personalCustomers/objectMeta
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: relationType(String)

## Body
- none

## Returns
- optional: name(String), customized(Boolean), fields(Array), label(String), type(String), nillable(Boolean), format(String), unit(String), selectOptions(Array), key(String), value(String), quote(Boolean), referenceTo(String), referenceFields(Array), rollUpSummaryFields(Array), aggregator(String), status(String), code(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-metadata-of-individual-enterprise-customers
updated_at: 2026-06-04 19:12:05
