# 解散场景群

doc_id: MfTls3182y
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/chat/scenegroup/disband
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openConversationId (String, required): 群ID，调用创建场景群接口获取`open_conversation_id`参数值。

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-dsbandopenscenegroup
updated_at: 2026-08-14 09:41:50
