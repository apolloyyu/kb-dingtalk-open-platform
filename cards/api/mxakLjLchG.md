# 删除群成员

doc_id: mxakLjLchG
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scenegroup/member/delete
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
- user_ids (String, required): 批量删除的成员userid。 **[!NOTE]** 多个userid之间使用英文逗号分隔，最多传100个。

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 批量删除的成员userid。 **[!NOTE]** 多个userid之间使用英文逗号分隔，最多传100个。

source_url: https://open.dingtalk.com/document/development/scene-group-delete
updated_at: 2026-08-25 09:37:18
