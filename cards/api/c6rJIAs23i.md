# 获取联系人的元数据

doc_id: c6rJIAs23i
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectmeta/contact/describe
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- none

## Returns
- optional: result(DObject), name(String), customized(Boolean), fields(Fields[]), label(String), type(String), nillable(Boolean), format(String), unit(String), select_options(SelectOptions[]), key(String), value(String), quote(Boolean), reference_to(String), reference_fields(ReferenceFields[]), roll_up_summary_fields(RollUpSummaryFields[]), aggregator(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/gets-the-metadata-description-of-a-crm-contact-object
updated_at: 2026-06-08 09:53:26
