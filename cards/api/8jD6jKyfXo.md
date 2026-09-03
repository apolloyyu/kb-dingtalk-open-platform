# 以应用身份发送文件给指定用户

doc_id: 8jD6jKyfXo
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/convFile/apps/conversations/files/send
api_version: v2-new
app_types: 第三方企业应用
permissions: ConvFile.File.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 接收文件的用户unionId，可调用查询用户详情接口获取。

## Body
- spaceId (String, required): 文件所在空间ID，调用添加空间接口获取id参数值。
- dentryId (String, required): 文件ID，可调用获取文件或文件夹列表接口获取id参数值。

## Returns
- optional: file(Object), id(String), conversationId(String), spaceId(String), parentId(String), type(String), name(String), size(Long), path(String), version(Long), status(String), extension(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), uuid(String)

## Limits
- 文件类型。 - **FILE**：文件 - **FOLDER**：文件夹 本接口只能发送文件。

source_url: https://open.dingtalk.com/document/development/sends-a-storage-file-to-a-specified-user
updated_at: 2026-06-04 19:09:29
