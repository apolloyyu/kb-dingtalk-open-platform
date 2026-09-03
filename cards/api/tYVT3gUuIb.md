# 获取群会话的OpenConversationId

doc_id: tYVT3gUuIb
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/chat/{chatId}/convertToOpenConversationId
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_chat_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- chatId (String, required): 群会话chatId： - **服务端**：通过创建群会话接口获取。 - **客户端**：通过chooseChatJSAPI获取。

## Query params
- none

## Body
- none

## Returns
- optional: openConversationId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-group-openconversationid
updated_at: 2026-08-13 09:03:31
