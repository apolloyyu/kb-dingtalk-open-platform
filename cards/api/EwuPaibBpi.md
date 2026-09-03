# 获取花名册元数据

doc_id: EwuPaibBpi
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_hrm_read_user

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- agentid (Number, required): 应用的AgentID。 - 企业内部应用，可在开发者后台的应用详情页获取应用ID。image - 第三方企业应用，通过获取企业授权信息接口获取agentid参数值。

## Returns
- optional: result(GroupMetaInfo[]), group_name(String), group_id(String), field_meta_info_list(FieldMetaInfo[]), field_name(String), field_code(String), derived(Boolean), detail(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-roster-metadata-query
updated_at: 2026-05-29 09:13:55
