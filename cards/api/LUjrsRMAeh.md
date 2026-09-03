# 删除假期规则

doc_id: LUjrsRMAeh
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/vacation/type/delete
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_holiday_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- leave_code (String, required): 假期规则唯一标识，可通过查询假期规则列表接口获取leave_code参数值。
- op_userid (String, required): 当前企业内拥有**OA审批**应用权限的管理员的userId。

## Returns
- optional: result(LeaveTypeVo), leave_code(String), leave_name(String), leave_view_unit(String), biz_type(String), natural_day_leave(Boolean), hours_in_per_day(Number), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 每天折算的工作时长，百分之一。 例如：1天=10小时=1000。

source_url: https://open.dingtalk.com/document/development/api-for-deleting-holiday-types
updated_at: 2026-05-27 17:06:26
