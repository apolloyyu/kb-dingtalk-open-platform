# 获取班次详情

doc_id: 6QEvezLhmC
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/shift/query
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
- op_user_id (String, required): 操作者的userId。
- shift_id (Number, required): 班次ID，可通过获取班次摘要信息接口获取id参数值。

## Returns
- optional: result(TopShiftVo), shift_group_name(String), corp_id(String), shift_setting(TopShiftSettingVo), shift_id(Number), gmt_modified(Date), work_time_minutes(Number), id(Number), attend_days(String), gmt_create(Date), name(String), sections(TopSectionVo[]), punches(TopPunchVo[]), check_type(String), end_min(Number), across(Number), check_time(Date), permit_minutes(Number), free_check(Boolean), begin_min(Number), absenteeism_late_minutes(String), serious_late_minutes(String), rests(TopRestVo[]), shift_group_id(Number), owner(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/shift-query
updated_at: 2026-05-27 17:06:03
