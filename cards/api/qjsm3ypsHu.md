# 发送工作通知

doc_id: qjsm3ypsHu
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- agent_id (Long, required): 发送消息时使用的微应用的AgentID。 - 企业内部应用可在开发者后台的应用详情页面查看。 - 第三方企业应用可调用获取企业授权信息接口获取。
- msg (JSON Object, required): 消息内容，最长不超过2048个字节，支持以下消息通知类型，msgtype 包括： **[!IMPORTANT]** 发送消息时，不支持同时发送多种消息类型。 - text：文本消息 - image：图片消息 - voice：语音消息 - file：文件消息 - link：链接消息 - oa：OA消息 **[!NOTE]** OA消息支持通过`status_bar`参数设置消息状态文案和颜色，发送后可通过更新工作通知状态栏接口更新消息状态和颜色。 - markdown：Markdown消息 - action_card
- optional: userid_list(String), dept_id_list(String), to_all_user(Boolean)

## Returns
- optional: request_id(String), errmsg(String), errcode(Number), task_id(Number)

## Limits
- 接收者的userid列表，最大用户列表长度100。
- 接收者的部门id列表，最大列表长度20。 接收者是部门ID时，包括子部门下的所有用户。
- 消息内容，最长不超过2048个字节，支持以下消息通知类型，msgtype 包括： **[!IMPORTANT]** 发送消息时，不支持同时发送多种消息类型。 - text：文本消息 - image：图片消息 - voice：语音消息 - file：文件消息 - link：链接消息 - oa：OA消息 **[!NOTE]** OA消息支持通过`status_bar`参数设置消息状态文案和颜色，发送后可通过更新工作通知状态栏接口更新消息状态和颜色。 - markdown：Mark
- - 企业内部应用发送消息单次最多只能给5000人发送，第三方企业应用发送消息单次最多能给1000人发送。
- - 给同一员工一天只能发送一条内容相同的消息通知。
- - 企业内部应用每天给每个员工最多可发送500条消息通知，第三方企业应用最多可发送100条。
- - 企业内部应用或第三方企业应用发送消息时，每分钟最多有5000人可以接收到消息。

source_url: https://open.dingtalk.com/document/development/asynchronous-sending-of-enterprise-session-messages
updated_at: 2026-05-29 09:13:40
