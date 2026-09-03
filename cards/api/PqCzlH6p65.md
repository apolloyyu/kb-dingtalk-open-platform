# 查询场景群成员

doc_id: PqCzlH6p65
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroups/members/batchQuery
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
- openConversationId (String, required): 群ID： - 基于群模板创建的群，可调用创建群接口获取`open_conversation_id`参数值。 - 安装群聊酷应用的群，通过安装酷应用入群获取返回参数`openConversationId`参数值。
- maxResults (Long, required): 分页大小。 接口返回结果可能会大于或小于maxResults，以实际返回结果为准。如果群成员数量不超过1000，而直接一次性返回全部群成员；如果群成员数量大于1000，则按照分页大小分批次返回。
- optional: coolAppCode(String), nextToken(String)

## Returns
- optional: success(Boolean), memberUserIds(Array of String), hasMore(Boolean), nextToken(String), unionIdList(Array of String), staffIdNickMap(Map<String, String>), unionIdNickMap(Map<String, String>)

## Limits
- 分页大小。 接口返回结果可能会大于或小于maxResults，以实际返回结果为准。如果群成员数量不超过1000，而直接一次性返回全部群成员；如果群成员数量大于1000，则按照分页大小分批次返回。

source_url: https://open.dingtalk.com/document/development/query-group-members
updated_at: 2026-08-14 09:41:53
