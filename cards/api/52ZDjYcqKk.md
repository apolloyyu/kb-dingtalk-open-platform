# 根据groupKey查询考勤组信息

doc_id: 52ZDjYcqKk
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/get
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
- group_key (String, required): 考勤组groupKey。 **[!NOTE]** 如果你使用的考勤组标识是group_id，可以调用groupId转换为groupKey接口将group_id转换为group_key。
- optional: op_userid(String)

## Returns
- optional: result(Object), name(String), ext(String), location_offset(Number), group_key(String), enable_face_check(Boolean), enable_face_beauty(Boolean), enable_camera_check(Boolean), enable_outside_check(Boolean), enable_outside_apply(Boolean), outside_check_approve_mode(Number), enable_outside_remark(Boolean), enable_outside_camera_check(Boolean), forbid_hide_outside_address(Boolean), enable_outside_update_normal_check(Boolean), enable_trim_distance(Boolean), trim_distance(Number), errmsg(String), success(Boolean), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-attendance-group-information-by-id
updated_at: 2026-05-27 13:09:47
