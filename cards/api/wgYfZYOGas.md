# 更新考勤组

doc_id: wgYfZYOGas
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/modify
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
- op_user_id (String, required): 操作人userId。
- top_group (Object, required): 考勤组信息。
- optional: shift_vo_list(Object[]), id(Number), name(String), positions(Object[]), address(String), corp_id(String), latitude(String), longitude(String), title(String), accuracy(String), offset(Number), enable_face_check(Boolean), manager_list(String[]), enable_camera_check(Boolean), owner(String), disable_check_when_rest(Boolean), skip_holidays(Boolean), enable_outside_check(Boolean), disable_check_without_schedule(Boolean), enable_emp_select_class(Boolean), resource_permission_map(Object), camera_check(String), over_time_rule(String), check_position_type(String), check_time(String), group_type(String), group_member(String), schedule(String), out_side_check(String), workday_class_list(Number[]), open_camera_check(Boolean), open_face_check(Boolean)

## Returns
- optional: result(Object), name(String), id(Number), errmsg(String), errcode(Number), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/attendance-group-update-interface
updated_at: 2026-05-27 13:09:42
