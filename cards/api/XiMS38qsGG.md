# 获取实例详情

doc_id: XiMS38qsGG
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/collection/instance/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- formInstance_id (String, required): 表单实例ID，可调用获取填表实例数据接口获取。
- optional: biz_type(Number)

## Returns
- optional: errcode(Number), errmsg(String), result(FormInstanceVo), form_code(String), title(String), creator(String), create_time(Date), modify_time(Date), form_list(FormData[]), label(String), key(String), value(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-collection-form-instance-details
updated_at: 2026-08-25 09:39:19
