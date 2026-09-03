# 查询人与人会话中机器人消息已读列表

doc_id: TgYeILunOm
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/privateChatMessages/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_robot_sendmsg

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processQueryKey (String, required): 消息id，可通过创建并投放卡片接口或人与人会话中机器人发送普通消息接口，获取`processQueryKey`参数值。
- optional: openConversationId(String), robotCode(String), maxResults(Long), nextToken(String)

## Returns
- optional: sendStatus(String), readUserIds(Array of String), nextToken(String), hasMore(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-read-list-of-robot-messages-in-person-to-person-conversations
updated_at: 2026-06-05 13:57:16
