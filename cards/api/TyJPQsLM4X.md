# 获取班次摘要信息

doc_id: TyJPQsLM4X
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/shift/list
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
- optional: cursor(Number)

## Returns
- optional: result(PageResult), has_more(Boolean), cursor(Number), name(String), id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/enterprise-shift-query-in-batches
updated_at: 2026-05-27 17:06:01
