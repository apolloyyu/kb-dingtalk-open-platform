# 添加假期规则

doc_id: 62jlhMFgNi
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/vacation/type/create
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
- leave_name (String, required): 假期名称。
- leave_view_unit (String, required): 请假时长单位。 - **day**：天 - **halfDay**：半天 - **hour**：小时
- biz_type (String, required): 假期类型。 - **general_leave**：普通假期 - **lieu_leave**：加班转调休 **[!NOTE]** 一个企业全局只允许存在一个加班转调休的假期类型。
- natural_day_leave (Boolean, required): 是否按照自然日统计请假时长。 - **true**：按照自然日统计请假时长 - **false**：不按照自然日统计请假时长 **[!NOTE]** 当为**false**的时候，用户发起请假时，会根据用户在请假时间段内的排班情况来计算请假时长。
- op_userid (String, required): 当前企业内拥有**OA审批**应用权限的管理员的userId，否则接口会报错**部门的管理员不存在**。
- hours_in_per_day (Number, required): 每天折算的工作时长，百分之一。例如：1天=10小时=1000。 该参数值一般与企业员工排班工作时长保持一致。
- optional: extras(String), submit_time_rule(Object), time_unit(String), time_value(Number), time_type(String), enable_time_limit(Boolean), leave_certificate(Object), unit(String), duration(Number), enable(Boolean), prompt_information(String)

## Returns
- optional: errcode(Number), errmsg(String), success(Boolean), result(Object), leave_name(String), leave_code(String), leave_view_unit(String), biz_type(String), natural_day_leave(Boolean), hours_in_per_day(Number), submit_time_rule(Object), time_value(Number), time_unit(String), time_type(String), enable_time_limit(Boolean), leave_certificate(Object), unit(String), duration(Number), enable(Boolean), prompt_information(String)

## Limits
- 每天折算的工作时长，百分之一。例如：1天=10小时=1000。 该参数值一般与企业员工排班工作时长保持一致。
- 调休假有效期规则 - **validity_type**：有效类型 - **absolute_time**：绝对时间 - **relative_time**：相对时间 - **validity_value**：延长日期 - 当validity_type为**absolute_time**该值该值不为空且满足“yy-mm”格式。 - 当validity_type为**relative_time**该值为大于1的整数。 **[!NOTE]** 假期类型biz_type值为lieu
- 限制值。 - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。
- 每天折算的工作时长，百分之一。 例如：1天=10小时=1000。

source_url: https://open.dingtalk.com/document/development/holiday-type-added
updated_at: 2026-08-25 09:38:02
