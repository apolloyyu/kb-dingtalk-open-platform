# 查询用户某段时间内是否处于封账状态

doc_id: 8mCM14ZVFw
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/closingAccounts/status/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userIds (Array of String, required): 员工列表。
- userTimeRange (Array, required): 时间段。
- startTime (Long, required): 开始日期，Unix时间戳，单位毫秒。
- endTime (Long, required): 结束日期，Unix时间戳，单位毫秒。
- bizCode (String, required): 情景： - **BOSS_CHECK**：老板改签 - **SCHEDULE**：排班 - **APPROVE**：补卡 - **SPECIAL_DAYS**：特殊日期修改

## Returns
- optional: mesage(String), code(String), pass(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/checks-whether-a-user-has-blocked-accounts-within-a-specified
updated_at: 2026-06-02 09:24:49
