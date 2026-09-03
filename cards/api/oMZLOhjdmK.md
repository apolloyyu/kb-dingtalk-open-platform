# 发送服务群消息

doc_id: oMZLOhjdmK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/messages/send
api_version: v2-new
app_types: 企业内部应用
permissions: ServiceGroup.Message.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- targetOpenConversationId (String, required): 开放群ID，可调用创建场景服务群接口获取openConversationId参数值。
- title (String, required): 发送消息的标题。
- content (String, required): 发送消息的内容。
- messageType (String, required): 消息类型，取值。 - **MARKDOWN**：markdown消息 - **ACTIONCARD**：卡片消息 markdown消息不能使用消息按钮。
- optional: isAtAll(Boolean), atMobiles(Array of String), atDingtalkIds(Array of String), atUnionIds(Array of String), receiverMobiles(Array of String), receiverDingtalkIds(Array of String), receiverUnionIds(Array of String), btnOrientation(String), btns(Array), actionURL(String), hasContentLinks(Boolean)

## Returns
- optional: openMsgTaskId(String)

## Limits
- 消息内容是否含有链接。 - **false**：当btns只有1个按钮，移动端点击消息卡片的任意内容将只会跳转到按钮的链接。 - **true**：无论btns多少，内容中的链接与按钮链接互不影响。

source_url: https://open.dingtalk.com/document/development/service-group-message-sending-interface
updated_at: 2026-06-04 19:11:22
