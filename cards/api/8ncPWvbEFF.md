# 设置场景群成员禁言状态

doc_id: 8ncPWvbEFF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroups/muteMembers/set
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userIdList (Array of String, required): 需要禁言或取消禁言的群成员userId列表。 - 群主和群管理员无法被设置禁言。 - 最多传999个。
- openConversationId (String, required): 群ID，通过创建场景群接口获取`open_conversation_id`参数值。
- muteStatus (Integer, required): 禁言状态： - **0**：取消禁言 - **1**：禁言
- muteDuration (Long, required): 禁言持续时长，单位：毫秒。

## Returns
- none

## Limits
- 需要禁言或取消禁言的群成员userId列表。 - 群主和群管理员无法被设置禁言。 - 最多传999个。

source_url: https://open.dingtalk.com/document/development/set-group-members-access-control
updated_at: 2026-08-14 09:41:59
