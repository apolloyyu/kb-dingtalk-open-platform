# 更新参与考勤人员

doc_id: 5KKDOYZw53
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/member/update
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- op_user_id (String, required): 操作人userId。
- group_id (Number, required): 考勤组ID。 **[!NOTE]** 如果你使用的是旧考勤组标识即group_key，可以调用groupKey转换为groupId接口将group_key转换为group_id。
- schedule_flag (Number, required): 从哪天开始排班。 - **0**：从今天开始排班 - **1**：从明天开始排班
- update_param (TopGroupMemberUpdateParam, required): 更新考勤组信息。
- optional: remove_extra_users(String[]), remove_depts(String[]), remove_users(String[]), add_depts(String[]), add_users(String[]), add_extra_users(String[])

## Returns
- optional: request_id(String), errcode(Number), success(Boolean)

## Limits
- 删除无需考勤的成员，没有的话，无需赋值，每次调用最多传20个userId。
- 删除考勤部门，没有的话，无需赋值，每次调用最多传20个部门ID。
- 删除考勤人员，没有的话，无需赋值，每次调用最多传20个userId。
- 添加考勤部门，没有的话，无需赋值，每次调用最多传20个部门ID。
- 添加考勤人员，没有的话，无需赋值，每次调用最多传20个userId。
- 添加无需考勤的人员，没有的话，无需赋值，每次调用最多传20个userId。

source_url: https://open.dingtalk.com/document/development/attendance-group-member-update
updated_at: 2026-05-27 13:09:55
