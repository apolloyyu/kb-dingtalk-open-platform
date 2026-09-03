# 查询场景群简要信息

doc_id: oMZn2ooR6S
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroups/query
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
- openConversationId (String, required): 群ID： - 基于群模板创建的群：调用创建场景群接口获取`open_conversation_id`参数值。 - 安装群聊酷应用的群：通过群内安装酷应用事件获取回调参数`OpenConversationId`参数值。
- optional: coolAppCode(String)

## Returns
- optional: success(Boolean), openConversationId(String), templateId(String), title(String), ownerUserId(String), icon(String), groupUrl(String), status(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-group-information
updated_at: 2026-08-14 09:41:56
