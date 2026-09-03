# 发送消息到企业群

doc_id: rHnemLx0Rn
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/chat/send
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
- chatid (String, required): 群会话的ID。 - 服务端API获取，调用创建群接口的返回chatid字段。 - 前端API获取，小程序调用选择会话，微应用调用根据corpid选择会话。
- msg (JSON Object, required): 消息内容，最长不超过2048个字节，消息类型和样例参考消息通知类型。

## Returns
- optional: errcode(Number), errmsg(String), messageId(String)

## Limits
- 消息内容，最长不超过2048个字节，消息类型和样例参考消息通知类型。

source_url: https://open.dingtalk.com/document/development/send-group-messages
updated_at: 2026-08-25 09:37:19
