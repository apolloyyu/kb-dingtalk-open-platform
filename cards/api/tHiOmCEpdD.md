# 更新场景群成员的群昵称

doc_id: tHiOmCEpdD
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroups/members/groupNicks
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
- openConversationId (String, required): 群ID，可调用创建群接口获取`open_conversation_id`参数值。
- userId (String, required): 用户的userid，可通过获取部门用户userid列表接口获取。
- groupNick (String, required): 用户群昵称，最长不超过30字符，建议长度在10字符以内。

## Returns
- optional: success(Boolean)

## Limits
- 用户群昵称，最长不超过30字符，建议长度在10字符以内。

source_url: https://open.dingtalk.com/document/development/update-group-nicknames
updated_at: 2026-08-14 09:42:00
