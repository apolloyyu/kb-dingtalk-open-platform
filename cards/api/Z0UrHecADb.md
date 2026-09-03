# 获取参与考勤人员的userid

doc_id: Z0UrHecADb
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list
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
- op_user_id (String, required): 操作人userId。
- group_id (Number, required): 考勤组ID。 **[!NOTE]** 如果你使用的是旧考勤组标识即group_key，可以调用groupKey转换为groupId接口将group_key转换为group_id。
- optional: cursor(Number)

## Returns
- optional: request_id(String), errcode(Number), success(Boolean), result(PageResult), has_more(Boolean), cursor(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-attendance-group-personnel-information-in-batches
updated_at: 2026-05-27 13:09:57
