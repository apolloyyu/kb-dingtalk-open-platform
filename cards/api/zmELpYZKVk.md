# 发送群助手消息

doc_id: zmELpYZKVk
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_chat_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- target_open_conversation_id (String, required): 群ID，调用创建场景群接口获取`open_conversation_id`参数值。
- msg_template_id (String, required): 消息模板ID，详情参见下文场景群通用消息模板。
- robot_code (String, required): 机器人编码，登录开发者后台 > 开放能力 > 场景群 > 机器人查看id。
- optional: msg_param_map(String), msg_media_id_param_map(String), receiver_user_ids(String[]), receiver_union_ids(String), receiver_mobiles(String), at_mobiles(String), at_users(String), is_at_all(Boolean)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), open_msg_id(String), request_id(String)

## Limits
- @人的手机号列表，调用查询用户详情接口获取`mobile`参数值。 **[!NOTE]** 一次调用最多支持50人。
- @人的userid列表，调用查询群成员接口获取`member_user_ids`参数值。 **[!NOTE]** 一次调用最多支持50人。

source_url: https://open.dingtalk.com/document/development/group-template-robot-message
updated_at: 2026-07-14 09:22:07
