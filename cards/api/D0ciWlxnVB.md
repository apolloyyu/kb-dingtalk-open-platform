# 机器人发送群聊消息

doc_id: D0ciWlxnVB
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/groupMessages/send
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
- msgParam (String, required): 消息模板参数，详情参考消息发送与接收类型。长度限制 15000 字节以内。
- msgKey (String, required): 消息模板key，详情参考消息发送与接收类型。
- openConversationId (String, required): 会话ID： - 如果是企业内部群 - 新创建企业内部群，企业内部应用，可调用创建企业内部群接口获取。已存在的企业内部群，可调用chooseChat获取。 - 如果是场景群 - 企业内部应用，可调用创建场景群接口获取。已存在的场景群，可调用 chooseChat 选择会话 JSAPI 获取。
- robotCode (String, required): 机器人的编码，详情参考机器人 ID。
- optional: coolAppCode(String)

## Returns
- optional: processQueryKey(String)

## Limits
- 消息模板参数，详情参考消息发送与接收类型。长度限制 15000 字节以内。

source_url: https://open.dingtalk.com/document/development/the-robot-sends-a-group-message
updated_at: 2026-07-14 09:29:38
