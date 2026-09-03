# 发送普通消息

doc_id: c3wFqfxHQD
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/message/send_to_conversation
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用，可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，可通服务商获取第三方应用授权企业的access_token接口获取。

## Body
- sender (String, required): 消息发送者的userid。
- cid (String, required): 群会话或者个人会话的id，通过JSAPI接口唤起联系人界面选择会话获取会话cid。
- msg (JSON Object, required): 消息内容，可参考消息通知类型，最长不超过2048个字节。

## Returns
- optional: receiver(String), errmsg(String), errcode(Number)

## Limits
- 消息内容，可参考消息通知类型，最长不超过2048个字节。
- > - 获取到的会话cid只能使用一次，且有效期为24小时。

source_url: https://open.dingtalk.com/document/development/send-normal-messages-1
updated_at: 2026-08-25 09:37:21
