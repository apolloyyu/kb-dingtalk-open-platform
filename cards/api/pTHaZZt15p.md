# 更新假期规则

doc_id: pTHaZZt15p
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/vacation/type/update
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
- op_userid (String, required): 当前企业内拥有**OA审批**应用权限的管理员的userId。
- leave_code (String, required): 接口添加的假期规则标识， **[!NOTE]** leave_code必须是通过添加假期规则接口添加的假期类型。
- optional: leave_name(String), leave_view_unit(String), biz_type(String), natural_day_leave(Boolean), hours_in_per_day(Number), extras(String), leave_certificate(LeaveCertificateVo), leave_certificate.unit(String), leave_certificate.duration(Number), leave_certificate.enable(Boolean), leave_certificate.prompt_information(String), submit_time_rule(SubmitTimeRuleVo), submit_time_rule.time_value(Number), submit_time_rule.time_unit(String), submit_time_rule.time_type(String), submit_time_rule.enable_time_limit(Boolean)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), success(Boolean), result(LeaveTypeVo), leave_name(String), leave_code(String), leave_view_unit(String), leave_certificate(LeaveCertificateVo), leave_certificate.unit(String), leave_certificate.duration(Number), leave_certificate.enable(Boolean), leave_certificate.prompt_information(String), submit_time_rule(SubmitTimeRuleVo), submit_time_rule.time_value(Number), submit_time_rule.time_unit(String), submit_time_rule.time_type(String), submit_time_rule.enable_time_limit(Boolean), biz_type(String), natural_day_leave(Boolean), hours_in_per_day(Number)

## Limits
- 每天折算的工作时长，百分之一。例如：1天=10小时=1000。
- 调休假有效期规则。 - **validity_type**：有效类型 - **absolute_time**：绝对时间 - **relative_time**：相对时间 - **validity_value**：延长日期 - 当validity_type为**absolute_time**该值该值不为空且满足“yy-mm”格式。 - 当validity_type为**relative_time**该值为大于1的整数。
- 限制值。 - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。
- 每天折算的工作时长，百分之一。 例如：1天=10小时=1000。
- 如下图所示，在**考勤应用 > 假期管理 > 假期规则**页面，可以查看共4个假期规则。

source_url: https://open.dingtalk.com/document/development/holiday-type-update
updated_at: 2026-08-25 09:38:03
