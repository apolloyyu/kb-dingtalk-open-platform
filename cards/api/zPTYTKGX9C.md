# 查询成员排班信息

doc_id: zPTYTKGX9C
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday
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
- op_user_id (String, required): 操作人的userId。
- user_id (String, required): 要查询的人员userId。
- date_time (Number, required): 查询的时间，Unix时间戳，单位毫秒。

## Returns
- optional: result(TopScheduleVo[]), check_type(String), approve_type(String), gmt_modified(Date), gmt_create(Date), corp_id(String), check_date_time(Date), group_id(Number), class_name(String), user_id(String), approve_biz_type(Number), approve_id(Number), class_setting_id(Number), approve_tag_name(String), features(String), class_id(Number), check_status(String), work_date(Date), check_end_time(Date), is_rest(String), check_begin_time(Date), real_plan_time(Date), id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-scheduling-for-a-day
updated_at: 2026-07-08 14:13:46
