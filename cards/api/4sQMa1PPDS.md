# 批量撤回人与人会话中机器人消息

doc_id: 4sQMa1PPDS
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/privateChatMessages/batchRecall
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
- openConversationId (String, required): 会话ID，需要与人与人会话中机器人发送普通消息接口或创建并投放卡片接口使用的openConversationId保持一致。
- robotCode (String, required): 机器人的编码，可参考机器人 ID。 需要与人与人会话中机器人发送普通消息接口使用的robotCode保持一致。
- processQueryKeys (Array of String, required): 消息id。 - 企业内部应用，可通过创建并投放卡片接口或人与人会话中机器人发送普通消息接口，获取`processQueryKey`参数值。

## Returns
- optional: successResult(Array of String), failedResult(Map<String, String>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/batch-withdrawal-of-single-chat-robot-messages-in-person-to-person-conversations
updated_at: 2026-06-05 13:49:04
