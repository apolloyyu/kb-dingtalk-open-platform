# 查询指定用户的封账规则

doc_id: lAWfGwjzvn
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/closingAccounts/rules/query
api_version: v2-new
app_types: 企业内部应用
permissions: Pro.AttendanceAccounts.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userIds (Array of String, required): 人员userId列表。

## Returns
- optional: result(Array), userId(String), switchOn(Boolean), closingAccountModel(Object), closingDay(Integer), closingHourMinutes(Long), startMonth(Integer), startDay(Integer), endMonth(Integer), endDay(Integer), unsealClosingAccountModel(Object), invalidTimeStamp(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/encapsulate-account-sealing-and-unsealing-rules
updated_at: 2026-06-08 11:46:50
