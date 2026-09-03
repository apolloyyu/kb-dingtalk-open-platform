# groupKey转换为groupId

doc_id: s82TAy4EGU
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/groups/keytoid
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
- group_key (String, required): 考勤组ID，旧考勤组标识，可调用批量获取考勤组详情接口获取group_id参数值。

## Returns
- optional: result(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/convert-groupkey-to-groupid
updated_at: 2026-05-27 13:09:48
