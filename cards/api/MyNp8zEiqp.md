# 校验用户是否在当前考勤组

doc_id: MyNp8zEiqp
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- op_user_id (String, required): 操作人userId。
- group_id (Number, required): 考勤组ID。 **[!NOTE]** 如果你使用的是旧考勤组标识即group_key，可以调用groupKey转换为groupId接口将group_key转换为group_id。
- member_ids (String, required): 成员ID，可以是userId或者deptId，多个ID之间使用英文逗号分割，每次调用最多支持传20个元素值。
- member_type (Number, required): 成员类型： - **0**：员工 - **1**：部门

## Returns
- optional: request_id(String), errmsg(String), errcode(Number), success(Boolean), result(String[])

## Limits
- 成员ID，可以是userId或者deptId，多个ID之间使用英文逗号分割，每次调用最多支持传20个元素值。

source_url: https://open.dingtalk.com/document/development/query-members-by-id
updated_at: 2026-05-27 13:10:02
