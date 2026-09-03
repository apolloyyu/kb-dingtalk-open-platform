# 搜索考勤组摘要

doc_id: cyLGiHXrgu
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/search
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- op_user_id (String, required): 操作人userId。
- group_name (String, required): 考勤组名称。

## Returns
- optional: result(TopMinimalismGroupVO[]), name(String), id(Number), success(Boolean), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/attendance-group-search
updated_at: 2026-05-27 13:09:45
