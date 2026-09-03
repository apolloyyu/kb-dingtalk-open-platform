# 批量查询人与机器人会话机器人消息是否已读

doc_id: krEOXw2dkH
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/robot/oToMessages/readStatus
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_robot_sendmsg

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- robotCode (String, required): 机器人的编码，详情参考机器人 ID。
- processQueryKey (String, required): 消息唯一标识，可通过批量发送人与机器人会话中机器人消息接口返回参数中`processQueryKey`字段获取。 在发送消息24小时内可以通过processQueryKey查询消息已读状态，超过24小时则无法查询。

## Body
- none

## Returns
- optional: sendStatus(String), messageReadInfoList(Array), name(String), userId(String), readStatus(String), readTimestamp(Long)

## Limits
- 消息唯一标识，可通过批量发送人与机器人会话中机器人消息接口返回参数中`processQueryKey`字段获取。 在发送消息24小时内可以通过processQueryKey查询消息已读状态，超过24小时则无法查询。
- 调用本接口，批量查询人与机器人会话时，机器人消息是否已读，适用于企业内部沟通中24小时内需要确认消息是否被阅读的场景。
- - 一次最多可以查询一条单聊信息20名接收者的消息是否已读数据。

source_url: https://open.dingtalk.com/document/development/chatbot-batch-query-the-read-status-of-messages
updated_at: 2026-06-05 13:41:56
