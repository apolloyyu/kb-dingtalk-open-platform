# 初始化假期余额

doc_id: 7oXpa5mZAH
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/vacation/quota/init
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
- op_userid (String, required): 当前企业内拥有**OA审批**应用权限的管理员的userId。
- leave_quotas (LeaveQuotas, required): 待初始化的假期余额记录。
- userid (String, required): 员工的userId。
- end_time (Number, required): 额度有效期结束时间，毫秒级时间戳。
- start_time (Number, required): 额度有效期开始时间，毫秒级时间戳。
- leave_code (String, required): 假期类型唯一标识。 **[!NOTE]** - 支持初始化调用添加假期规则接口添加的假期类型。 - 不支持初始化企业自带的假期。
- optional: reason(String), quota_num_per_day(Number), quota_num_per_hour(Number), quota_cycle(String)

## Returns
- optional: result(Result[]), reason(String), quota(Quota), leave_code(String), userid(String), quota_cycle(String), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 额度有效期结束时间，毫秒级时间戳。
- 额度有效期开始时间，毫秒级时间戳。
- 以天计算的额度总数。 **[!NOTE]** 假期类型按天计算时，该值不为空且按百分之一天折算。 例如：1000=10天。
- 以小时计算的额度总数。 **[!NOTE]** 假期类型按小时，计算该值不为空且按百分之一小时折算。 例如：1000=10小时。

source_url: https://open.dingtalk.com/document/development/initialize-holiday-balance
updated_at: 2026-05-27 17:06:27
