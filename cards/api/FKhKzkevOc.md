# 批量拉取考勤组蓝牙设备

doc_id: FKhKzkevOc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/group/bledevices/query
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: result(Array), deviceId(Long), deviceName(String), sn(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/attendance-group-bluetooth-devices
updated_at: 2026-10-28 11:14:27
