# 查询企业考勤排班详情

doc_id: ZaRiz3wUGd
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/listschedule
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- workDate (Date, required): 排班时间，只取年月日部分。
- optional: offset(Number), size(Number)

## Returns
- optional: result(AtScheduleListForTopVo), schedules(AtScheduleForTopVo[]), plan_id(Number), check_type(String), approve_id(Number), userid(String), class_id(Number), class_setting_id(Number), plan_check_time(Date), group_id(Number), changed_check_time(Date), has_more(Boolean), errmsg(String), errcode(Number), request_id(String)

## Limits
- 分页大小，最大值200。
- - 固定班制只能查到未来15天的排班信息。
- - 本接口仅支持企业总人数10000人以下使用。

source_url: https://open.dingtalk.com/document/development/interface-for-daily-full-query-of-attendance-scheduling-information
updated_at: 2026-05-27 17:06:14
