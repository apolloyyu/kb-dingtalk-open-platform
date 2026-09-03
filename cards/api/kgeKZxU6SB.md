# 获取指定部门的所有父部门列表

doc_id: kgeKZxU6SB
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/department/list_parent_depts_by_dept
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- optional: id(String)

## Body
- none

## Returns
- optional: parentIds(Number[]), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-all-parent-departments-of-a-department
updated_at: 2026-08-25 09:37:00
