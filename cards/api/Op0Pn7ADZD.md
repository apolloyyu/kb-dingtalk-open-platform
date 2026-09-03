# 批量查询人员排班信息

doc_id: Op0Pn7ADZD
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/schedule/listbyusers
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- op_user_id (String, required): 操作人userId。
- userids (String, required): 要查询的人员userId列表，多个userId用逗号分隔，一次最多可传50个。
- from_date_time (Number, required): 起始日期，Unix时间戳，单位毫秒。 **[!NOTE]** - 开始时间和结束时间的间隔不能超过7天。 - 查询时间限制距今180天内。
- to_date_time (Number, required): 结束日期，Unix时间戳，单位毫秒。 **[!NOTE]** - 开始时间和结束时间的间隔不能超过7天。 - 查询时间限制距今180天内。

## Returns
- optional: result(TopScheduleVo[]), check_type(String), plan_check_time(Date), group_id(Number), userid(String), approve_id(Number), work_date(Date), id(Number), shift_version(Number), shift_id(Number), is_rest(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 要查询的人员userId列表，多个userId用逗号分隔，一次最多可传50个。
- 起始日期，Unix时间戳，单位毫秒。 **[!NOTE]** - 开始时间和结束时间的间隔不能超过7天。 - 查询时间限制距今180天内。
- 结束日期，Unix时间戳，单位毫秒。 **[!NOTE]** - 开始时间和结束时间的间隔不能超过7天。 - 查询时间限制距今180天内。

source_url: https://open.dingtalk.com/document/development/query-batch-scheduling-information
updated_at: 2026-05-27 17:06:10
