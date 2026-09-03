# 取消日程

doc_id: I92rWRpY8n
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/calendar/v2/event/cancel
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- calendar_id (String, required): 日历ID。 目前仅支持传**primary**表示修改当前用户“我的日程”下的日程。
- event_id (String, required): 加密后的日程ID。
- optional: agentid(Number)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 调用该接口取消日程，只能取消通过**创建日程**接口创建的日程。

source_url: https://open.dingtalk.com/document/development/schedule-2-0-cancel-schedule
updated_at: 2026-08-25 09:38:07
