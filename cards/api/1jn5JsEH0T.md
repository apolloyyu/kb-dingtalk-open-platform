# 消息群发

doc_id: 1jn5JsEH0T
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/message/mass/send
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- unionid (String, required): 服务号的unionid，可通过查询服务号列表接口获取。
- is_to_all (Boolean, required): 是否群发给组织下所有人： - **true**：是 - **false**：否
- msg_type (String, required): 消息类型： - **text**：文本类型，文本内容填在text_content字段中 - **news_card**：消息卡片，可以通过查询图文卡片列表接口获取media_id - **image**：图片类型，可以通过上传媒体文件接口获media_id - **markdown**：markdown消息，需要设置msg_body中markdown对象的相关参数 - **action_card**：action_card卡片消息，需要设置msg_body中action_card对象的相关参数 - **single
- uuid (String, required): 调用时填写随机生成的UUID，防止消息重复发送。
- optional: media_id(String), text_content(String), userid_list(String), dep_id_list(String), roleIds(String), allow_comment(Boolean), comment_type(Number), show_homepage(Number), is_preview(Boolean), msg_body(MessageBody), markdown(Markdown), text(String), title(String), action_card(ActionCard), btn_orientation(String), single_title(String), button_list(Button[]), action_url(String), single_url(String)

## Returns
- optional: errmsg(String), errcode(Number), task_id(String), request_id(String)

## Limits
- 接收者的用户userid列表，列表最大长度1000。
- 接收者的部门id列表，接收者是部门id下（包括子部门下）的所有用户，列表最大长度1000。
- 接收者角色roleId列表，列表最大长度1000。
- 是否预览推送，预览推送只会发给单个用户，并且内容链接24小时后可能会失效。 **[!NOTE]** 取值为**true**时，**userid_list**不能为空。
- 使用整体跳转ActionCard样式时的标题，最长20个字符。 **[!NOTE]** 必须与single_url同时设置。
- 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。
- > - 使用dep_id_list或is_to_all方式做大规模人群推送时，选中人数上限为10万人。如果超过此上限，群发失败，群发任务不会执行。

source_url: https://open.dingtalk.com/document/development/interactive-service-window-group-message-sending-interface
updated_at: 2026-08-25 09:39:20
