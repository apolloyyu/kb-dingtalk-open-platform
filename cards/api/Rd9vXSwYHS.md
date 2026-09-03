# 创建群

doc_id: Rd9vXSwYHS
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scenegroup/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- title (String, required): 群名称。 **[!NOTE]** 最长不超过30字符，建议长度在10字符以内。
- template_id (String, required): 群模板ID，登录开发者后台 > 开放能力 > 场景群 > 群模板查看id。image
- owner_user_id (String, required): 群主的userid。
- optional: user_ids(String), subadmin_ids(String), uuid(String), icon(String), mention_all_authority(Number), show_history_type(Number), validation_type(Number), searchable(Number), chat_banned_type(Number), management_type(Number), only_admin_can_ding(Number), all_members_can_create_mcs_conf(Number), all_members_can_create_calendar(Number), group_email_disabled(Number), only_admin_can_set_msg_top(Number), add_friend_forbidden(Number), group_live_switch(Number), members_to_admin_chat(Number)

## Returns
- optional: result(OpenSceneGroupCreateResponse), open_conversation_id(String), chat_id(String), success(Boolean), errmsg(String), errcode(Number), request_id(String)

## Limits
- 群名称。 **[!NOTE]** 最长不超过30字符，建议长度在10字符以内。
- 群成员userid列表。 **[!NOTE]** 最多传999个。

source_url: https://open.dingtalk.com/document/development/create-a-scene-group-v2
updated_at: 2026-08-25 09:37:16
