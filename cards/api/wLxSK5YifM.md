# 查询企业机器人群聊消息用户已读状态

doc_id: wLxSK5YifM
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/groupMessages/query
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
- processQueryKey (String, required): 消息唯一标识，通过机器人发送群聊消息接口返回参数processQueryKey字段中获取。
- optional: openConversationId(String), robotCode(String), maxResults(Long), nextToken(String)

## Returns
- optional: sendStatus(String), readUserIds(Array of String), nextToken(String), hasMore(Boolean)

## Limits
- 分页查询每页的数量，最大值200。

source_url: https://open.dingtalk.com/document/development/chatbot-queries-the-read-status-of-a-message
updated_at: 2026-06-05 13:49:01
