# 人与人会话中机器人发送普通消息

doc_id: njGIKh1vi0
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/privateChatMessages/send
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
- msgParam (String, required): 消息模板参数，详情参考消息发送与接收类型。
- msgKey (String, required): 消息模板key，详情参考消息发送与接收类型。
- openConversationId (String, required): 会话ID，可通过批量安装酷应用到单聊会话或监听单聊酷应用事件获取OpenConversationId参数值。
- robotCode (String, required): 机器人编码，该参数使用企业机器人的robotCode，详情参考机器人 ID。
- coolAppCode (String, required): 酷应用编码。 image

## Returns
- optional: processQueryKey(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/the-robot-sends-ordinary-messages-in-a-person-to-person-conversation
updated_at: 2026-07-14 09:29:37
