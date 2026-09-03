# 获取子部门ID列表

doc_id: ovdZVoq8Pa
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/department/list_ids
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- id (String, required): 部门ID，查询根部门输入1。

## Body
- none

## Returns
- optional: sub_dept_id_list(Number[]), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-a-sub-department-id-list
updated_at: 2026-08-25 09:37:00
