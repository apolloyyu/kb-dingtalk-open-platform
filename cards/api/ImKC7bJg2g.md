# 批量取消待办

doc_id: ImKC7bJg2g
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/workrecord/taskgroup/cancel
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- request (UpdateTaskRequest, required): 请求对象。
- agentid (Number, required): 应用标识。可在开发者后台的应用详情页获取。 image
- process_instance_id (String, required): 实例ID，由创建实例接口获取。
- activity_id (String, required): 待办组ID，需要在调用查询待办列表接口时，主动设置该值。
- optional: activity_id_list(String[])

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/cancel-multiple-tasks
updated_at: 2026-08-25 09:37:59
