# 查询群信息

doc_id: nqDZ6FziCZ
completeness: full
archived: false
method: GET
endpoint: https://oapi.dingtalk.com/chat/get
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_chat_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。
- chatid (String, required): 群会话的ID。 - 仅支持通过调用服务端创建群会话接口获取的chatid参数值。 - 不支持通过调用前端JSAPI获取的chatid。

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String), chat_info(ChatInfo), name(String), owner(String), useridlist(String[]), conversationTag(Number), chatBannedType(Number), searchable(Number), validationType(Number), mentionAllAuthority(Number), managementType(Number), showHistoryType(Number), icon(String), status(Number)

## Limits
- 新成员是否可查看100条历史消息： - **1**：可查看 - **0**：不可查看 如果不传值，代表不可查看。

source_url: https://open.dingtalk.com/document/development/obtain-a-group-session
updated_at: 2026-06-08 09:21:15
