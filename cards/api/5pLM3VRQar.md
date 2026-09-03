# 查询场景群禁言状态

doc_id: 5pLM3VRQar
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroups/muteSettings
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_chat_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 群成员userId。
- openConversationId (String, required): 群ID，通过创建场景群接口获取`open_conversation_id`字段值。

## Body
- none

## Returns
- optional: groupMuteMode(Boolean), userMuteResult(Object), userMuteMode(Boolean), muteStartTime(Long), muteEndTime(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-group-silence-status
updated_at: 2026-08-14 09:41:55
