# 批量发送服务窗消息

doc_id: lW4pHmRFUI
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/officialAccounts/oToMessages/batchSend
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
- uuid (String, required): 消息请求唯一ID。长度不超过128位字符。
- messageBody (Object, required): 消息体。
- content (String, required): 文本消息内容，建议500字符以内。
- title (String, required): 首屏会话透出的展示内容。
- picUrl (String, required): 图片地址。
- messageUrl (String, required): 消息链接地址，当发送消息为小程序时支持小程序跳转链接。
- actionUrl (String, required): 使用独立跳转ActionCard样式时的跳转链接。
- optional: bizRequestId(String), userIdList(Array of String), text(Object), markdown(Object), link(Object), actionCard(Object), buttonOrientation(String), singleUrl(String), singleTitle(String), buttonList(Array), sendToAll(Boolean), bizId(String), accountId(String)

## Returns
- optional: result(Object), openPushId(String), requestId(String)

## Limits
- 消息请求唯一ID。长度不超过128位字符。
- 消息接收人列表，最多支持1000人。 值为服务窗粉丝userid，可以通过粉丝关注事件获取对应的userid。
- 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。
- 使用整体跳转ActionCard样式时的标题。 必须与**singleUrl**同时设置，最长20个字符。
- 使用独立跳转ActionCard样式时的按钮列表。 必须与**buttonOrientation**同时设置，且长度不超过1000字符。
- 消息推送ID，长度不超过256位，可用于消息发送进度排查。
- - 目前此接口每天最多允许调用100次。
- - 每位粉丝用户一天内最多允许收到三条来自同一服务窗的消息（包括服务窗后台群发、批量接口及单发接口）。

source_url: https://open.dingtalk.com/document/development/batch-sending-of-service-window-messages
updated_at: 2026-06-04 19:12:00
