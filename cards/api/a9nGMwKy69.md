# 更新场景群管理员

doc_id: a9nGMwKy69
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroups/subAdmins
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openConversationId (String, required): 群ID，调用创建场景群接口获取`open_conversation_id`参数值。
- role (Long, required): 群成员类型： - **2**：群管理员 - **3**：普通群成员
- optional: userIds(Array of String), unionIds(Array of String)

## Returns
- optional: success(Boolean)

## Limits
- 用户userid列表。 最多传12个。

source_url: https://open.dingtalk.com/document/development/update-group-administrators
updated_at: 2026-08-14 09:41:54
