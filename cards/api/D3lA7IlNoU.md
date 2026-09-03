# 更新群

doc_id: D3lA7IlNoU
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scenegroup/update
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
- open_conversation_id (String, required): 群ID，调用创建群接口获取`open_conversation_id`参数值。
- optional: title(String), owner_user_id(String), icon(String), mention_all_authority(Number), show_history_type(Number), validation_type(Number), searchable(Number), chat_banned_type(Number), management_type(Number), only_admin_can_ding(Number), all_members_can_create_mcs_conf(Number), all_members_can_create_calendar(Number), group_email_disabled(Number), only_admin_can_set_msg_top(Number), add_friend_forbidden(Number), group_live_switch(Number), members_to_admin_chat(Number), plugin_customize_verify(Number)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String)

## Limits
- 群名称。 **[!NOTE]** 最长不超过30字符，建议长度在10字符以内。

source_url: https://open.dingtalk.com/document/development/scene-group-update
updated_at: 2026-08-25 09:37:16
