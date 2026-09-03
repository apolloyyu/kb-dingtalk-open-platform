# 查询参与考勤人员列表

doc_id: Cq9F8lSUPe
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/users/query
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
- cursor (String, required): 上一批次最后一个userid，传null、空值表示从头开始查。
- group_key (String, required): 考勤组ID。 **[!NOTE]** 如果你使用的考勤组标识是group_id，可以调用groupId转换为groupKey接口将group_id转换为group_key。
- optional: size(Number), op_userid(String)

## Returns
- optional: request_id(String), result(DingOpenResult), user_list(String[]), has_more(String), errcode(Number), errmsg(String), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/batch-query-of-employees-in-the-attendance-group
updated_at: 2026-05-27 13:10:00
