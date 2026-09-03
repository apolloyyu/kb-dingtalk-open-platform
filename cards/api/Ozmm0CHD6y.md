# 通知审批撤销

doc_id: Ozmm0CHD6y
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/approve/cancel
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
- userid (String, required): 员工的userId。
- approve_id (String, required): 审批ID，来自通知审批通过接口自定义的参数approve_id。

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/notify-the-attendance-to-modify-the-punch-result-when-the
updated_at: 2026-05-27 17:06:21
