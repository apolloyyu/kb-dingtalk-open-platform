# 批量发送人与机器人会话中机器人消息

doc_id: yeB1dR8qqc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend
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
- robotCode (String, required): 机器人的编码，该参数必须使用企业内部应用机器人的robotCode，详情参考机器人 ID。
- userIds (Array of String, required): 接收消息的用户userId列表，每次最多传20个，可通过查询用户详情或获取部门用户userid列表接口获取。
- msgKey (String, required): 消息模板key，详情参考消息发送与接收类型。
- msgParam (String, required): 消息模板参数，消息模板参数，详情参考消息发送与接收类型。

## Returns
- optional: processQueryKey(String), invalidStaffIdList(Array of String), flowControlledStaffIdList(Array of String)

## Limits
- 接收消息的用户userId列表，每次最多传20个，可通过查询用户详情或获取部门用户userid列表接口获取。
- 调用本接口，批量发送人与机器人会话（人与机器人单聊）中机器人消息。适用于需要向多个用户（最多20个）批量发送机器人消息的场景，如企业通知、系统告警推送等场景。

source_url: https://open.dingtalk.com/document/development/chatbots-send-one-on-one-chat-messages-in-batches
updated_at: 2026-07-14 09:29:36
