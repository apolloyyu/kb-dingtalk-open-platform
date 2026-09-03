# groupId转换为groupKey

doc_id: uqXy4szXgc
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/groups/idtokey
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
- group_id (Number, required): 考勤组ID，可调用批量获取考勤组详情接口获取group_id参数值。
- optional: op_user_id(String)

## Returns
- optional: result(String), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/groupid-to-groupkey
updated_at: 2026-05-27 13:09:49
