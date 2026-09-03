# 更新员工花名册

doc_id: QSOMK1JTw8
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/update
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端接口的授权凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- param (UnionExportParam, required): 修改员工信息。
- userid (String, required): 员工userid。
- agentid (Number, required): 应用的AgentID，可在开发者后台的应用详情页获取应用ID。
- optional: groups(GroupMetaInfo[]), group_id(String), sections(EmpListFieldVO[]), section(EmpFieldVo[]), value(String), field_code(String)

## Returns
- optional: result(Boolean), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-employee-roster
updated_at: 2026-08-25 09:39:07
