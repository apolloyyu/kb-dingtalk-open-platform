# 获取群存储空间信息

doc_id: 9wzsNj8pi8
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/convFile/conversations/spaces/query
api_version: v2-new
app_types: 企业内部应用
permissions: ConvFile.Space.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取。

## Body
- openConversationId (String, required): 会话openConversationId，可调用创建群接口获取openConversationId参数值。

## Returns
- optional: space(Object), spaceId(String), corpId(String), createTime(String), modifiedTime(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-group-storage-space-information
updated_at: 2026-07-14 09:21:52
