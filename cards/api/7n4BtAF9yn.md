# 清理审批数据

doc_id: 7n4BtAF9yn
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/clean
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- suite_access_token (String, required): 调用服务端API授权凭证，可通过获取第三方企业应用的suite_access_token接口获取。

## Body
- process_code (String, required): 模板唯一码。
- corpid (String, required): 企业的corpid。

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/clean-up-workflow-data
updated_at: 2026-08-25 09:37:40
