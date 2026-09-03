# 批量获取考勤组详情

doc_id: 9xG00GMLmL
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getsimplegroups
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
- optional: offset(Number), size(Number)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(AtGroupListForTopVo), has_more(Boolean), groups(AtGroupForTopVo[]), group_id(Number), is_default(Boolean), group_name(String), selected_class(AtClassVo[]), enable_emp_select_class(Boolean), disable_check_without_schedule(Boolean), disable_check_when_rest(Boolean), setting(ClassSettingVo), class_setting_id(Number), rest_begin_time(AtTimeVo), check_time(Date), permit_late_minutes(Number), work_time_minutes(Number), rest_end_time(AtTimeVo), absenteeism_late_minutes(Number), serious_late_minutes(Number), is_off_duty_free_check(String), class_id(Number), sections(AtSectionVo[]), times(SetionTimeVO[]), check_type(String), across(Number), class_name(String), type(String), member_count(Number), default_class_id(Number), work_day_list(String[]), classes_list(String[]), manager_list(String[]), dept_name_list(String[]), owner_user_id(String)

## Limits
- 分页大小，最大10。

source_url: https://open.dingtalk.com/document/development/batch-obtain-attendance-group-details
updated_at: 2026-05-27 13:09:51
