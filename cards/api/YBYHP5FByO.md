# 通过Agoal系统账号发送消息

doc_id: YBYHP5FByO
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/agoal/messages/send
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.Message.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- templateId (String, required): 消息模板id。
- params (String, required): 模板参数。
- mobileUrl (String, required): 移动端链接。
- pcUrl (String, required): PC端链接。
- sourceDingUserId (String, required): 发送人dingUserId。
- targetDingUserIds (Array of String, required): 接收人dingUserId。

## Returns
- optional: requestId(String), success(Boolean), content(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalsendmessage
updated_at: 2026-06-15 10:38:54
