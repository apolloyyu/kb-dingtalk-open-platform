# 提交评论

doc_id: 8JSaFLpXZj
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/forms/remarks
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Comment.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- appType (String, required): 应用编码，获取方式如下：
- systemToken (String, required): 应用密钥，获取方式如下：
- formInstanceId (String, required): 实例ID。
- userId (String, required): 评论人的的useid。
- content (String, required): 评论内容。
- optional: replyId(Long), language(String), atUserId(String), formUuid(String), env(String)

## Returns
- optional: result(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/submit-comment
updated_at: 2026-06-02 11:29:56
