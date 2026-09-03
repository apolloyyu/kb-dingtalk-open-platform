# 查询考勤写操作权限

doc_id: AA3xzxgBGF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/writePermissions/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Attendance.Permission.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- opUserId (String, required): 员工userId。
- category (String, required): 资源类型： - **GROUP**：考勤组，目前仅支持该值。
- resourceKey (String, required): 权限点： - **GROUP_MEMBER**：设置参与考勤人员 - **GROUP_NAME**：修改考勤组名称 - **GROUP_TYPE**：设置考勤组类型 - **CHECK_TIME**：设置考勤时间 - **SCHEDULE**：员工排班 - **CHECK_POSITION_TYPE**：设置打卡方式 - **OVER_TIME_RULE**：设置加班规则 - **CAMERA_CHECK**：拍照验证规则 - **OUT_SIDE_CHECK**：设置外勤打卡 - **MANAGE**：考勤组子负
- entityIds (Array of Long, required): 资源ID，如果category参数值为GROUP，该参数值传考勤组ID，可通过获取用户考勤组接口获取group_id参数值。

## Returns
- optional: entityPermissionMap(Map<String, Boolean>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/attendance-writing-operation-is-brand-new-query
updated_at: 2026-06-01 16:41:46
