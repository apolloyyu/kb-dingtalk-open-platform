# 获取自定义对象的元数据

doc_id: CfRvdjOlwD
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/crm/objectmeta/describe
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_crm_customdata_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- name (String, required): 自定义表单code，进入表单编辑页面，最下方可查看。iShot2022-11-01 20

## Returns
- optional: result(DObject), name(String), customized(Boolean), fields(Fields[]), label(String), type(String), nillable(Boolean), format(String), unit(String), select_options(SelectOptions[]), key(String), value(String), quote(Boolean), reference_to(String), reference_fields(ReferenceFields[]), roll_up_summary_fields(RollUpSummaryFields[]), aggregator(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-metadata-description-of-crm-custom-object
updated_at: 2026-06-08 09:53:19
