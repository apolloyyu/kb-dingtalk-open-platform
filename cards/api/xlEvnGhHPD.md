# 消息群发

doc_id: xlEvnGhHPD
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/follow/message/send
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_service_account_message

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，企业内部应用调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: unionid(String), is_to_all(Boolean), msg_type(String), uuid(String), text_content(String), is_preview(Boolean), media_id(String), userid_list(Array of String), dep_id_list(Array of Long), roleIds(Array of Long), msg_body(Object), markdown(Object), text(String), title(String), action_card(Object), btn_orientation(String), single_title(String), button_list(Array), action_url(String), single_url(String), link(Object), cover_image_media_id(String), link_url(String), summary(String), open_type(Integer), allow_comment(Boolean), comment_type(Integer), show_homepage(Integer)

## Returns
- optional: errorcode(String), errmsg(String), task_id(String)

## Limits
- 是否预览推送，预览推送只会发给单个用户，并且内容链接24小时后可能会失效。 取值为true时，userid_list不能为空。
- 使用整体跳转ActionCard样式时的标题，最长20个字符。 必须与single_url同时设置。
- 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。
- - 使用dep_id_list或is_to_all方式做大规模人群推送时，选中人数上限为10万人。如果超过此上限，群发失败，群发任务不会执行。

source_url: https://open.dingtalk.com/document/development/api-sendmessage
updated_at: 2026-06-04 19:09:55
