# 配置考勤排班附加信息

doc_id: munK7AQDGM
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/attendance/schedules/additionalInfo
api_version: v2-new
app_types: 企业内部应用
permissions: Pro.AttendanceGroup.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- scheduleInfos (Array, required): 排班信息列表。
- planId (Long, required): 待更新的排班ID，可调用查询企业考勤排班详情接口获取。
- opUserId (String, required): 操作者的userId。
- optional: wifiKeys(Array of String), positionKeys(Array of String), retainAttendanceCheck(Boolean)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/synchronization-scheduling-information
updated_at: 2026-06-15 10:56:03
