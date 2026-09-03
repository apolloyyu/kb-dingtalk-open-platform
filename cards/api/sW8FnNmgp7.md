# 获取企业客户的元数据

doc_id: sW8FnNmgp7
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectmeta/customer/describe
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- none

## Returns
- optional: result(DObject), name(String), customized(Boolean), fields(Fields[]), label(String), type(String), nillable(Boolean), format(String), unit(String), select_options(SelectOptions[]), key(String), value(String), quote(Boolean), reference_to(String), reference_fields(ReferenceFields[]), roll_up_summary_fields(RollUpSummaryFields[]), aggregator(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-metadata-description-of-crm-customer-object
updated_at: 2026-08-28 10:27:03
