# 发送服务窗单人消息

doc_id: nRzXacXnOA
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/officialAccounts/oToMessages/send
api_version: v2-new
app_types: 第三方企业应用
permissions: OfficialAccount.Message.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- detail (Object, required): 消息详情。
- msgType (String, required): 消息类型。
- uuid (String, required): 消息发送请求唯一ID，长度不超过128位字符。
- messageBody (Object, required): 消息体。
- content (String, required): 消息内容，建议500字符以内。
- title (String, required): 首屏会话透出的展示内容。
- picUrl (String, required): 图片地址。
- messageUrl (String, required): 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接。
- actionUrl (String, required): 使用独立跳转ActionCard样式时的跳转链接。
- optional: userId(String), unionId(String), text(Object), markdown(Object), link(Object), actionCard(Object), buttonOrientation(String), singleUrl(String), singleTitle(String), buttonList(Array), image(Object), mediaId(String), bizId(String), accountId(String)

## Returns
- optional: requestId(String), result(Object), openPushId(String)

## Limits
- 消息发送请求唯一ID，长度不超过128位字符。
- 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。
- 使用整体跳转ActionCard样式时的标题。 必须与**singleUrl**同时设置，最长20个字符。
- 使用独立跳转ActionCard样式时的按钮列表。 必须与**buttonOrientation**同时设置，且长度不超过1000字符。
- 消息推送ID，长度不超过256位字符串，可用于消息发送进度排查。
- - 此接口一天最多允许调用次数等于服务窗粉丝数量。
- - 每位粉丝用户一天最多允许接收三条来自服务窗的消息（包括服务窗后台群发、批量发送接口及单人消息接口）。

source_url: https://open.dingtalk.com/document/development/sends-a-single-message-from-the-service-window
updated_at: 2026-06-04 19:12:01
