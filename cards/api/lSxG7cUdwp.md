# 删除考勤组

doc_id: lSxG7cUdwp
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/delete
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
- optional: op_userid(String)

## Returns
- optional: result(String), success(Boolean), errmsg(String), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-attendance-group
updated_at: 2026-05-27 13:09:44
