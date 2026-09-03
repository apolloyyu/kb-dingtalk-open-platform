# 更新钉钉待办任务

doc_id: jvZjcwNuS9
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/workrecord/update
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- userid (String, required): 任务执行人的userid。
- record_id (String, required): 待办任务唯一ID，可使用新增钉钉待办任务中传入的biz_id，也可以使用返回中的record_id。

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-to-do-status
updated_at: 2026-08-25 09:38:11
