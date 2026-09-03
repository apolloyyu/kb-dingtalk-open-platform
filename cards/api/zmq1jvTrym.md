# 批量新增参与考勤人员

doc_id: zmq1jvTrym
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/users/add
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
- group_key (String, required): 考勤组ID。 **[!NOTE]** 如果你使用的考勤组标识是group_id，可以调用groupId转换为groupKey接口将group_id转换为group_key。
- user_id_list (String[], required): 用户列表，最大值100。
- optional: op_userid(String)

## Returns
- optional: result(Result), error_info_list(ErrorInfo[]), failure_list(String[]), msg(String), code(String), success_list(String[]), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 用户列表，最大值100。

source_url: https://open.dingtalk.com/document/development/batch-add-employees-under-the-attendance-group
updated_at: 2026-05-27 13:09:53
