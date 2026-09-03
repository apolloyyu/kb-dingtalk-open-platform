# 发送文件更改的评论

doc_id: OGfhlbLWav
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/comments/send
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- fileId (String, required): 钉盘文件ID。可以调用JSAPI获取：唤起钉盘选择器。
- spaceId (String, required): 钉盘空间ID，可以调用JSAPI获取：唤起钉盘选择器。
- operatorUnionId (String, required): 操作人的unionId，可通过以下两种方式获取： - 可以调用通过免登码获取用户信息接口获取。 - 可调用查询用户详情接口获取。
- optional: operateType(String)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/send-comments-on-file-changes
updated_at: 2026-06-04 19:09:59
