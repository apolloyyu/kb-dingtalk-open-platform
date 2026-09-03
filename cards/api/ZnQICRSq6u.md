# 删除部门

doc_id: ZnQICRSq6u
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/department/delete
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。
- id (String, required): 部门ID，可调用获取部门列表接口获取。 **[!NOTE]** 以下情况无法删除部门： - 不能删除根部门，即部门ID为1。 - 部门或子部门内还有未删除的员工。

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-a-department
updated_at: 2026-08-25 09:37:03
