# 查询场景群基本信息

doc_id: 610NIo2cBV
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scenegroup/get
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_chat_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- open_conversation_id (String, required): 群ID，调用创建场景群接口获取`open_conversation_id`参数值。

## Returns
- optional: result(DecorationGroupQueryResponse), icon(String), management_options(ManagementOptions), chat_banned_type(String), searchable(String), validation_type(String), mention_all_authority(String), management_type(String), show_history_type(String), title(String), template_id(String), open_conversation_id(String), sub_admin_staff_ids(String[]), owner_staff_id(String), group_url(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-basic-information-of-a-scenario-group
updated_at: 2026-08-14 09:41:58
