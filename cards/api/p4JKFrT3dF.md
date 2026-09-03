# 删除班次

doc_id: p4JKFrT3dF
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/shift/delete
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
- op_user_id (String, required): 操作人userId。
- shift_id (Number, required): 班次ID，可通过获取班次摘要信息接口获取id参数值。

## Returns
- optional: errmsg(String), errcode(Number), success(Boolean), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-shift
updated_at: 2026-07-02 10:36:15
