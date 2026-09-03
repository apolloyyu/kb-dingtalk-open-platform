# 批量撤回人与机器人会话中机器人消息

doc_id: zoPZB7T5hD
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/otoMessages/batchRecall
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
- robotCode (String, required): 机器人的编码，详情参考机器人 ID。 需要与机器人发送群聊消息接口时使用的robotCode一致。
- processQueryKeys (Array of String, required): 消息唯一标识列表，可通过批量发送人与机器人会话中机器人消息接口获取。 - 每次最多传20个。 - 在发送消息24小时内可以通过processQueryKey撤回消息，超过24小时则无法撤回消息。

## Returns
- optional: successResult(Array of String), failedResult(Map<String, String>)

## Limits
- 消息唯一标识列表，可通过批量发送人与机器人会话中机器人消息接口获取。 - 每次最多传20个。 - 在发送消息24小时内可以通过processQueryKey撤回消息，超过24小时则无法撤回消息。
- 用于批量撤回人与机器人会话中机器人消息。调用时通过 POST 请求提交 robotCode、processQueryKeys 等业务字段。本接口适用于企业24小时内撤回错误发送的通知消息等场景。

source_url: https://open.dingtalk.com/document/development/batch-message-recall-chat
updated_at: 2026-06-05 13:49:03
