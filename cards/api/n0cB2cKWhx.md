# 批量删除地点

doc_id: n0cB2cKWhx
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/positions/remove
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
- position_key_list (String, required): 要删除position的key列表，可通过批量查询地点接口获取，每次最多支持删除100个地点信息。
- optional: op_userid(String)

## Returns
- optional: result(Result), success_list(String[]), error_info_list(ErrorInfo[]), failure_list(String[]), msg(String), code(String), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 要删除position的key列表，可通过批量查询地点接口获取，每次最多支持删除100个地点信息。

source_url: https://open.dingtalk.com/document/development/delete-position-in-batches-under-the-attendance-group
updated_at: 2026-05-27 13:10:10
