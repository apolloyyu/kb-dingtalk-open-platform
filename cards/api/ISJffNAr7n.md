# 添加假期规则

doc_id: ISJffNAr7n
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/leaves/types
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_holiday_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- opUserId (String, required): 管理员userId，同时该管理员需拥有OA审批应用的管理权限。 **[!NOTE]** 如果不满足条件，接口会报错，提示部门的管理员不存在。

## Body
- leaveName (String, required): 假期规则名称。
- leaveViewUnit (String, required): 请假时长单位。 - **day**：天 - **halfDay**：半天 - **hour**：小时
- bizType (String, required): 假期类型。 - **general_leave**：普通假期 - **lieu_leave**：加班转调休 **[!NOTE]** 一个企业只能存在一个加班转调休的假期规则。
- naturalDayLeave (Boolean, required): 是否按照自然日统计请假时长。 - **true**：是 - **false**：否 **[!NOTE]** 例如，员工小明提交请假审批单，开始时间是2022年4月11日上午9:30，结束时间是2022年4月18日下午18:30，其中4月16和4月17为周六日休息。 - 当该参数传true时，小明发起该请假审批单后，计入的请假天数为8天。包含员工未排班的休息日或者法定节假日。 - 当该参数传false时，小明发起该请假审批单后，计入的请假天数为6天。不包含员工未排班的休息日或者法定节假日。
- hoursInPerDay (Long, required): 每天折算的工作时长，为参数值的百分之一。 **[!NOTE]** 例如，某企业员工所在的班次工时是8小时，则该参数值为8\*100=800。
- optional: extras(String), paidLeave(Boolean), visibilityRules(Array), visible(Array of String), type(String), whenCanLeave(String), leaveTimeCeilMinUnit(String), leaveTimeCeil(Boolean), minLeaveHour(double), submitTimeRule(Object), timeValue(Long), timeUnit(String), timeType(String), enableTimeLimit(Boolean), leaveCertificate(Object), unit(String), duration(double), enable(Boolean), promptInformation(String), maxLeaveTime(Long), leaveHourCeil(String), freedomLeave(Boolean)

## Returns
- optional: result(Object), leaveName(String), leaveCode(String), leaveViewUnit(String), bizType(String), naturalDayLeave(Boolean), hoursInPerDay(Long), visibilityRules(Array), visible(Array of String), type(String), submitTimeRule(Object), timeValue(Long), timeUnit(String), timeType(String), enableTimeLimit(Boolean), leaveCertificate(Object), unit(String), duration(double), enable(Boolean), promptInformation(String)

## Limits
- 假期类型。 - **general_leave**：普通假期 - **lieu_leave**：加班转调休 **[!NOTE]** 一个企业只能存在一个加班转调休的假期规则。
- 是否按照自然日统计请假时长。 - **true**：是 - **false**：否 **[!NOTE]** 例如，员工小明提交请假审批单，开始时间是2022年4月11日上午9:30，结束时间是2022年4月18日下午18:30，其中4月16和4月17为周六日休息。 - 当该参数传true时，小明发起该请假审批单后，计入的请假天数为8天。包含员工未排班的休息日或者法定节假日。 - 当该参数传false时，小明发起该请假审批单后，计入的请假天数为6天。不包含员工未排班的休息日或者
- 每天折算的工作时长，为参数值的百分之一。 **[!NOTE]** 例如，某企业员工所在的班次工时是8小时，则该参数值为8\*100=800。
- 调休假有效期规则。 - **validity_type**：有效类型 - **absolute_time**：绝对时间 - **relative_time**：相对时间 - **validity_value**：延长日期 - 当validity_type为**absolute_time**，该值不为空且满足“yy-mm”格式。 - 当validity_type为**relative_time**，该值为大于1的整数。 **[!NOTE]** 假期类型biz_type值为**l
- 请假时长向上取整时的最小时长单位。 **[!NOTE]** 第三方企业应用专属字段。 - **hour** 小时，不足1小时按照1小时计算 - **halfHour** 半小时，不足半小时按照半小时计算
- 限制值。 - 当timeUnit为day时，有效值范围是0至30天。 - 当timeUnit为hour时，有效值范围是0至24小时。
- 最大请假时长（请假单位为hour或day时生效）。 **[!NOTE]** 第三方企业应用专属字段。
- 每天折算的工作时长，为参数值的百分之一。 例如，某企业每天的工作时长设置为10小时，则该参数值为10\*100=1000。

source_url: https://open.dingtalk.com/document/development/add-holiday-rules
updated_at: 2026-06-01 16:58:42
