# 更新假期规则

doc_id: srZ9Fyuwom
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/attendance/leaves/types
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_holiday_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- opUserId (String, required): 操作者userId。

## Body
- leaveViewUnit (String, required): 请假单位。 - **day**：天 - **halfDay**：半天 - **hour**：小时
- bizType (String, required): 假期类型。 - **general_leave**：普通假期 - **lieu_leave**：加班转调休
- leaveCode (String, required): 接口添加的假期规则标识，leave_code必须是通过接口添加的假期类型。 - 企业内部应用，调用添加假期规则接口获取的leave_code参数值。 - 第三方企业应用，调用添加假期规则接口获取的leave_code参数值。
- optional: leaveName(String), naturalDayLeave(Boolean), hoursInPerDay(Long), extras(String), visibilityRules(Array), visible(Array of String), type(String), submitTimeRule(Object), timeValue(Long), timeUnit(String), timeType(String), enableTimeLimit(Boolean), leaveCertificate(Object), unit(String), duration(double), enable(Boolean), promptInformation(String)

## Returns
- optional: result(Object), leaveName(String), leaveCode(String), leaveViewUnit(String), bizType(String), naturalDayLeave(Boolean), hoursInPerDay(Long), visibilityRules(Array), visible(Array of String), type(String), submitTimeRule(Object), timeValue(Long), timeUnit(String), timeType(String), enableTimeLimit(Boolean), leaveCertificate(Object), unit(String), duration(double), enable(Boolean), promptInformation(String)

## Limits
- 是否按照自然日统计请假时长。 - **true**：是 - **false**：否 例如，员工小明提交请假审批单，开始时间是2022年4月11日上午9:30，结束时间是2022年4月18日下午18:30，其中4月16和4月17为周六日休息。 - 当该参数传true时，小明发起该请假审批单后，计入的请假天数为8天。包含员工未排班的休息日或者法定节假日。 - 当该参数传false时，小明发起该请假审批单后，计入的请假天数为6天。不包含员工未排班的休息日或者法定节假日。
- 每天折算的工作时长，为参数值的百分之一。 例如，某企业员工所在的班次工时是8小时，则该参数值为8\*100=800。
- 调休假有效期规则。 - **validity_type**：有效类型 - **absolute_time**：绝对时间 - **relative_time**：相对时间 - **validity_value**：延长日期 - 当validity_type为**absolute_time**，该值不为空且满足“yy-mm”格式。 - 当validity_type为**relative_time**，该值为大于1的整数。
- 限制值。 - 当timeUnit为**day**时，有效值范围是0至30天。 - 当timeUnit为**hour**时，有效值范围是0至24小时。
- 是否按照自然日统计请假时长。 - **true**：是 - **false**：否 例如,员工小明提交请假审批单，开始时间是2022年4月11日上午9:30，结束时间是2022年4月18日下午18:30，其中4月16和4月17为周六日休息。 - 当该参数传true时，小明发起该请假审批单后，计入的请假天数为8天。包含员工未排班的休息日或者法定节假日。 - 当该参数传false时，小明发起该请假审批单后，计入的请假天数为6天。不包含员工未排班的休息日或者法定节假日。
- 每天折算的工作时长，为参数值的百分之一。 例如，某企业员工所在的班次工时是8小时，则该字段值为8\*100=800。
- 限制值。 - 当timeUnit为**day**时，有效值范围是0至30天； - 当timeUnit为**hour**时，有效值范围是0至24小时。
- 如下图所示，在**考勤应用** > **假期管理** > **假期规则**页面，可以查看共4个假期规则。

source_url: https://open.dingtalk.com/document/development/update-holiday-rules
updated_at: 2026-06-02 09:24:53
