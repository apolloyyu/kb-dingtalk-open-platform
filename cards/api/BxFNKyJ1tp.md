# 创建场景群

doc_id: BxFNKyJ1tp
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/sceneGroup/create
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的accessToken接口获取。 - 第三方企业应用，通过获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- title (String, required): 群名称，最长不超过30字符，建议长度在10字符以内。
- template_id (String, required): 群模板ID，登录开发者后台 > 开放能力 > 场景群 > 群模板查看id。
- owner_user_id (String, required): 群主userId。
- optional: icon(String), user_ids(Array of String), subadmin_ids(Array of String), uuid(String), management_options(Object), mention_all_authority(Integer), show_history_type(Integer), validation_type(Integer), searchable(Integer), chat_banned_type(Integer), management_type(Integer), only_admin_can_ding(Integer), all_members_can_create_mcs_conf(Integer), all_members_can_create_calendar(Integer), group_email_disabled(Integer), only_admin_can_set_msg_top(Integer), add_friend_forbidden(Integer), group_live_switch(Integer), members_to_admin_chat(Integer), not_quit_when_emp_leave(Integer), only_admin_can_add_mem(Integer)

## Returns
- optional: open_conversation_id(String), chat_id(String)

## Limits
- 群名称，最长不超过30字符，建议长度在10字符以内。

source_url: https://open.dingtalk.com/document/development/create-a-scene-group
updated_at: 2026-06-10 18:24:18
