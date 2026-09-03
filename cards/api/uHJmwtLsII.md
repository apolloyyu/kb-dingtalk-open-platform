# 自定义机器人发送群消息

doc_id: uHJmwtLsII
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/robot/send
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 自定义机器人调用接口的凭证。 自定义机器人安装后webhook地址中的access_token值。详情参考获取自定义机器人 Webhook 地址。

## Body
- msgtype (String, required): 消息类型，自定义机器人可发送的消息类型参见消息发送与接收类型。
- optional: msgUuid(String), text(Object), content(String), at(Object), isAtAll(Boolean), atMobiles(String[]), atUserIds(String[]), link(Object), messageUrl(String), title(String), picUrl(String), markdown(Object), actionCard(Object), hideAvatar(String), btnOrientation(String), singleURL(String), singleTitle(String), btns(Object[]), actionURL(String), feedCard(Object), links(Object[]), picURL(String), messageURL(String)

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- 被@的群成员userId。 **[!NOTE]** 在@群成员时，最多只能@50个。
- - **每个机器人每分钟最多发送20条消息到群里，如果超过20条，会限流10分钟。**

source_url: https://open.dingtalk.com/document/development/custom-robots-send-group-messages
updated_at: 2026-07-14 09:21:57
