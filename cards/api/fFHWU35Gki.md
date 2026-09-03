# 发送文件链接到指定会话

doc_id: fFHWU35Gki
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/convFile/conversations/files/links/send
api_version: v2-new
app_types: 企业内部应用
permissions: ConvFile.File.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取。

## Body
- spaceId (String, required): 文件所在空间ID，调用添加空间接口获取。
- dentryId (String, required): 文件ID，调用获取文件或文件夹列表接口获取id参数值。
- openConversationId (String, required): 目标会话的openConversationId，调用创建群接口获取openConversationId参数值。

## Returns
- optional: file(Object), id(String), conversationId(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), uuid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/send-a-file-link-to-the-specified-session
updated_at: 2026-06-04 10:33:07
