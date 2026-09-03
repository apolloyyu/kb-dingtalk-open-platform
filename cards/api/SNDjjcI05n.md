# 批量查询员工假期余额变更记录

doc_id: SNDjjcI05n
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/vacation/record/list
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
- leave_code (String, required): 假期类型唯一标识，通过查询假期规则列表接口获取leave_code参数值。
- userids (String, required): 待查询员工ID列表，每次调用最多传50个userId。
- offset (Number, required): 分页页码，从0开始非负整数。
- size (Number, required): 分页大小，最大200。

## Returns
- optional: result(OapiLeaveRecordListVo), has_more(Boolean), leave_records(OapiLeaveRecordVo[]), userid(String), leave_code(String), record_id(String), quota_id(String), start_time(Number), end_time(Number), leave_view_unit(String), cal_type(String), leave_reason(String), leave_status(String), leave_record_type(String), record_num_per_day(Number), record_num_per_hour(Number), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 待查询员工ID列表，每次调用最多传50个userId。
- 分页大小，最大200。
- 额度有效期开始时间，毫秒级时间戳。
- 额度有效期结束时间，毫秒级时间戳。
- 以天计算的消费额度。 **[!NOTE]** 假期类型按天计算时，该值不为空且按百分之一天折算。 例如：1000=10天。
- 以小时计算的消费额度。 **[!NOTE]** 假期类型按小时，计算该值不为空且按百分之一小时折算。 例如：1000=10小时。

source_url: https://open.dingtalk.com/document/development/query-holiday-consumption-records
updated_at: 2026-08-25 09:38:04
