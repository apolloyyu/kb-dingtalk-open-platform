# 批量查询成员排班概要信息

doc_id: SPTRTU9cJH
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/schedule/shift/listbydays
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- op_user_id (String, required): 操作者的userId。
- userids (String, required): 需要查询的用户userId列表，多个userId之间使用逗号分隔，且每次查询最多不能超过20。
- from_date_time (Number, required): 开始日期的Unix时间戳，单位毫秒。 **[!NOTE]** 时间跨度不能超过7天。
- to_date_time (Number, required): 结束日期的Unix时间戳，单位毫秒。 **[!NOTE]** 时间跨度不能超过7天。

## Returns
- optional: result(TopDayScheduleShiftVo[]), work_date(Date), shift_names(String[]), userid(String), shift_versions(Number[]), shift_ids(Number[]), group_id(Number), corp_id(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 需要查询的用户userId列表，多个userId之间使用逗号分隔，且每次查询最多不能超过20。
- 开始日期的Unix时间戳，单位毫秒。 **[!NOTE]** 时间跨度不能超过7天。
- 结束日期的Unix时间戳，单位毫秒。 **[!NOTE]** 时间跨度不能超过7天。

source_url: https://open.dingtalk.com/document/development/query-scheduling-summary-information
updated_at: 2026-05-27 17:06:13
