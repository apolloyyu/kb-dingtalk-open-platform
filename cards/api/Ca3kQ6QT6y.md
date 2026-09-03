# 查询群发消息详情

doc_id: Ca3kQ6QT6y
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/follow/message/getMsgRecordDetail
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_service_account_message

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- unionid (String, required): 服务号的unionid。
- task_id (String, required): 群发消息任务id，通过分页查询指定群发消息记录或者群发消息后获取到。

## Returns
- optional: errorcode(String), errmsg(String), result(Object), task_id(String), send_time(Long), create_time(Long), msg_type(String), title(String), operator_user_id(String), is_to_all(Boolean), userid_list(Array of String), dep_id_list(Array of String), roleIdList(Array of String), allow_forward(Boolean), allow_comment(Boolean), view_scope_type(String), mediaId(String), textContent(String), articles(Array), article_id(Long), thumb_media_id(String), publish_status(Long), publish_time(Long), update_time(Long), content(String), url(String), digest(String), link(Object), summary(String), link_url(String), open_type(Integer), cover_image_media_id(String), markdown(Object), text(String), action_card(Object), bnt_orientation(String), single_url(String), single_title(String), button_list(Array), action_url(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/service-account-msg-record-detail
updated_at: 2026-06-02 19:13:04
