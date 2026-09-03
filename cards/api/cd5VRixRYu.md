# 获取员工离职信息

doc_id: cd5VRixRYu
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/listdimission
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- userid_list (String, required): 要查询的离职员工userid，多个员工用逗号分隔，最大长度50，通过获取离职员工列表接口获取data_list参数值。 如果传入为非离职员工userid，不会返回信息。

## Returns
- optional: result(EmpDimissionInfoVo[]), userid(String), last_work_day(Number), dept_list(EmpDeptVO[]), dept_path(String), dept_id(Number), reason_memo(String), reason_type(Number), pre_status(Number), handover_userid(String), status(Number), main_dept_name(String), main_dept_id(Number), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 要查询的离职员工userid，多个员工用逗号分隔，最大长度50，通过获取离职员工列表接口获取data_list参数值。 如果传入为非离职员工userid，不会返回信息。

source_url: https://open.dingtalk.com/document/development/obtain-multiple-employee-demission-information
updated_at: 2026-08-25 09:39:10
