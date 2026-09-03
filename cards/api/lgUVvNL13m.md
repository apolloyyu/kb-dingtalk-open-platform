# 变更智能考勤机员工

doc_id: lgUVvNL13m
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/smartDevice/atmachines/users
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_dingtalk_attendance_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: delUserIds(Array of String), deviceIds(Array of String), addUserIds(Array of String), devIds(Array of Long), delDeptIds(Array of Long), addDeptIds(Array of Long)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/change-intelligent-attendance-machine-staff
updated_at: 2026-06-01 16:50:45
