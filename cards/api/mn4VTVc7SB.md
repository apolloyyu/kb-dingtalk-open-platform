# 查询假期余额

doc_id: mn4VTVc7SB
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/vacation/quota/list
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
- leave_code (String, required): 假期类型唯一标识，可通过查询假期规则列表接口获取leave_code参数值。
- op_userid (String, required): 当前企业内拥有**OA审批**应用权限的管理员的userId。
- userids (String, required): 待查询的员工ID列表。
- offset (Number, required): 分页偏移，从0开始的非负整数。
- size (Number, required): 分页偏移，最大50。

## Returns
- optional: result(OapiLeaveQuotaUserListVo), has_more(Boolean), leave_quotas(Leavequotas[]), userid(String), leave_code(String), quota_cycle(String), quota_id(String), start_time(Number), end_time(Number), quota_num_per_hour(Number), quota_num_per_day(Number), used_num_per_day(Number), used_num_per_hour(Number), errcode(Number), errmsg(String), success(Boolean)

## Limits
- 分页偏移，最大50。
- 假期有效期开始时间，毫秒级时间戳。
- 额度有效期结束时间，毫秒级时间戳。
- 以小时计算的额度总数。 **[!NOTE]** 假期类型按小时，计算该值不为空且按百分之一小时折算。 例如：1000=10小时。
- 以天计算的额度总数。 **[!NOTE]** 假期类型按天计算时，该值不为空且按百分之一天折算。 例如：1000=10天。
- 以天计算的使用额度。 **[!NOTE]** 假期类型按天计算时，该值不为空且按百分之一天折算。 例如：100=1天。
- 以小时计算的使用额度。 **[!NOTE]** 假期类型按小时计算时，该值不为空且按百分之一小时折算。 例如：1000=10小时。
- 调用本接口，根据企业或员工分页获取假期余额信息，每次返回50条数据。

source_url: https://open.dingtalk.com/document/development/query-holiday-balance
updated_at: 2026-05-27 17:06:30
