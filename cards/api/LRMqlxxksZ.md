# 获取花名册字段组详情

doc_id: LRMqlxxksZ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/field/grouplist
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_hrm_read_user

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- agentid (Number, required): 应用AgentId，可在钉钉开发者后台的应用详情页获取。 iShot2022-10-21_14

## Returns
- optional: request_id(String), errmsg(String), errcode(Number), success(Boolean), result(GroupMetaInfo[]), group_id(String), has_detail(Boolean), field_list(FieldMetaInfo[]), field_type(String), field_name(String), field_code(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-roster-field-group-details
updated_at: 2026-05-29 09:13:53
