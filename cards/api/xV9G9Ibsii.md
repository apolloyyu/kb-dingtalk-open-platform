# 查询用户考勤节假日信息

doc_id: xV9G9Ibsii
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/holidays
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
- workDateFrom (Long, required): 开始日期。
- workDateTo (Long, required): 结束日期。

## Returns
- optional: result(Array), userId(String), holidays(Array), workDate(Long), holidayName(String), holidayType(String), realWorkDate(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-user-attendance-and-holiday-information
updated_at: 2026-06-01 16:58:45
