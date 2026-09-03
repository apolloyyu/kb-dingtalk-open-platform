# 查询历史班次

doc_id: 27rEmb6iBd
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/shift/history/query
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_attendance_group_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- op_user_id (String, required): 操作者userId。
- shift_id (Number, required): 班次ID，可通过获取班次摘要信息接口获取id参数值。
- version (Number, required): 班次版本，可通过批量查询人员排班信息接口获取shift_version参数值。

## Returns
- optional: result(TopShiftVo), shift_group_name(String), corp_id(String), shift_setting(TopShiftSettingVo), shift_id(Number), gmt_modified(Date), is_deleted(String), work_time_minutes(Number), id(Number), attend_days(String), gmt_create(Date), name(String), sections(TopSectionVo[]), punches(TopPunchVo[]), check_type(String), end_min(Number), across(Number), check_time(Date), permit_minutes(Number), free_check(Boolean), begin_min(Number), rests(TopRestVo[]), shift_group_id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-history-shifts
updated_at: 2026-05-27 17:05:59
