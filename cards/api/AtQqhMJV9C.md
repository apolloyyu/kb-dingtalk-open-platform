# 查询假期规则列表

doc_id: AtQqhMJV9C
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/vacation/type/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_holiday_readonly

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- op_userid (String, required): 当前企业内拥有**OA审批**应用权限的管理员的userId。
- optional: vacation_source(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), success(Boolean), result(Result[]), leave_code(String), leave_name(String), leave_view_unit(String), leave_certificate(LeaveCertificateVo), leave_certificate.unit(String), leave_certificate.duration(Number), leave_certificate.enable(Boolean), leave_certificate.prompt_information(String), submit_time_rule(SubmitTimeRuleVo), submit_time_rule.time_value(Number), submit_time_rule.time_unit(String), submit_time_rule.time_type(String), submit_time_rule.enable_time_limit(Boolean), biz_type(String), natural_day_leave(String), validity_type(String), validity_value(String), hours_in_per_day(Number), source(String)

## Limits
- 限制值。 - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。
- 每天折算的工作时长，百分之一。 例如：1天=10小时=1000。

source_url: https://open.dingtalk.com/document/development/holiday-type-query
updated_at: 2026-05-27 17:06:29
