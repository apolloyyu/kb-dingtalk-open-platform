# 第三方个人应用发送服务窗单人消息

doc_id: rH3in84zT7
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/officialAccounts/snsMessages/send
api_version: v2-new
app_types: 第三方个人应用
permissions: OfficialAccount.SnsMessage.Send

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，调用获取用户token接口获取。

## Path params
- none

## Query params
- none

## Body
- detail (Object, required): 消息详情。
- msgType (String, required): 消息类型。
- uuid (String, required): 消息发送请求唯一ID，长度不超过128个字符。
- messageBody (Object, required): 消息体。
- bindingToken (String, required): 服务窗与第三方个人应用绑定时生成的授权码，可通过服务窗微应用-开放互联功能进行账号与第三方个人应用的绑定后获取。
- optional: text(Object), content(String), markdown(Object), title(String), link(Object), picUrl(String), messageUrl(String), actionCard(Object), buttonOrientation(String), singleUrl(String), singleTitle(String), buttonList(Array), actionUrl(String), bizId(String)

## Returns
- optional: requestId(String), result(Object), openPushId(String)

## Limits
- 消息发送请求唯一ID，长度不超过128个字符。
- 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。
- 使用整体跳转ActionCard样式时的标题。 必须与**singleUrl**同时设置，最长20个字符。
- 使用独立跳转ActionCard样式时的按钮列表。 必须与**buttonOrientation**同时设置，且长度不超过1000字符。
- 消息推送ID，长度不超过256位字符串，可用于消息发送进度排查。
- - 此接口一天最多允许调用次数等于服务窗粉丝数量。
- - 每位粉丝用户一天最多允许接收三条来自服务窗的消息（包括服务窗后台群发、批量发送接口及单人消息接口）。

source_url: https://open.dingtalk.com/document/development/a-third-party-personal-application-sends-a-message-to-a-single
updated_at: 2026-06-04 19:12:03
