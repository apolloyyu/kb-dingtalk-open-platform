# 使用服务助手推送消息

doc_id: IYcbGPvGJD
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/smartbot/msg/push
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- msg (Msg, required): 消息内容，最长不超过2048个字节。消息类型和样例参考消息类型与数据格式。
- msgtype (String, required): 消息类型，支持如下消息类型。 - **text**：文本消息。 - **markdown**：Markdown消息。 - **action_card**：卡片消息。
- optional: text(Text), content(String), markdown(Markdown), title(String), action_card(ActionCard), btn_json_list(BtnJson[]), action_url(String), btn_orientation(String), single_url(String), single_title(String), user_id_list(String), chat_id_list(String), to_all_user(Boolean)

## Returns
- optional: task_id(String), errcode(Number), errmsg(String), request_id(String)

## Limits
- 消息内容，最长不超过2048个字节。消息类型和样例参考消息类型与数据格式。
- 使用独立跳转**ActionCard**样式时的按钮列表，必须与**btn_orientation**同时设置，且长度不超过1000字符。 **[!NOTE]** 如果是独立跳转的**ActionCard**样式，则**btn_json_list**和**btn_orientation**必须设置。
- 使用独立跳转**ActionCard**样式时的跳转链接，最长500个字符。
- 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 消息链接跳转，请参考消息链接说明。
- 使用整体跳转ActionCard样式时的标题。必须与single_url同时设置，最长20个字符。 **[!NOTE]** 如果是整体跳转的ActionCard样式，则**single_title**和**single_url**必须设置。
- 接收者的userid列表，最大用户列表长度100。
- 接收者的会话chatid列表，最大会话列表长度10。

source_url: https://open.dingtalk.com/document/development/the-message-pushing-interface-of-the-assistant
updated_at: 2026-08-27 14:20:53
