# 删除H5微应用

doc_id: 04ZuBzGhPg
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/microapp/delete
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端接口的授权凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- agentId (Number, required): H5微应用的agentid。企业只能删除自建H5微应用。

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- H5微应用的agentid。企业只能删除自建H5微应用。

source_url: https://open.dingtalk.com/document/development/delete-an-h5-microapplication
updated_at: 2026-08-25 09:39:05
