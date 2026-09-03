# 修改打卡时段设置

doc_id: 7xGAIG6OZo
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/shift/updatepunches
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- op_user_id (String, required): 操作者的userId。
- id (Number, required): 卡点ID， 可通过获取班次详情接口获取id参数值。
- free_check (Boolean, required): 是否无需打卡。 - **true**：开启无需打卡。 - **false**：关闭无需打卡。
- shift_id (Number, required): 班次ID， 可通过获取班次摘要信息接口获取id参数值。
- optional: punches(TopPunchVO[])

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/modify-card-settings
updated_at: 2026-05-27 17:05:57
