# 获取考勤组详情

doc_id: jN14RqfFQy
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/query
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
- group_id (Number, required): 考勤组ID，可调用批量获取考勤组详情接口获取group_id参数值。 **[!NOTE]** 如果是旧考勤组标识即group_key，可调用groupKey转换为groupId接口将group_key转换为group_id。

## Returns
- optional: result(TopSimpleGroupVO), name(String), shift_ids(Number[]), id(Number), wifis(String[]), address_list(String[]), work_day_list(Number[]), member_count(Number), type(String), url(String), manager_list(String), owner_user_id(String), success(Boolean), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-a-single-attendance-group
updated_at: 2026-05-27 13:09:46
