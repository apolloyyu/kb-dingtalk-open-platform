# 企业机器人撤回内部群消息

doc_id: QrSBdVpLIE
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/groupMessages/recall
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
- openConversationId (String, required): 群ID，可通过客户端 chooseChat获取群会话 openConversationId。 需要与机器人发送群聊消息接口时使用的openConversationId一致。
- robotCode (String, required): 机器人的编码，可参考机器人 ID。 需要与机器人发送群聊消息接口时使用的robotCode一致。
- processQueryKeys (Array of String, required): 消息ID列表，可通过机器人发送群聊消息接口返回参数processQueryKey字段中获取。

## Returns
- optional: successResult(Array of String), failedResult(Map<String, String>)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/enterprise-chatbot-withdraws-internal-group-messages
updated_at: 2026-06-05 13:49:05
