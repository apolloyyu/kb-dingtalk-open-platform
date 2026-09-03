# 获取群内机器人列表

doc_id: aWHs68krUU
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/robot/groups/robots/query
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
- openConversationId (String, required): 群ID：基于群模板创建的群，调用创建群接口获取`open_conversation_id`参数值。

## Returns
- optional: chatbotInstanceVOList(Array), robotCode(String), name(String), downloadIconURL(String), openRobotType(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-list-of-robots-in-the-group
updated_at: 2026-06-05 13:49:07
