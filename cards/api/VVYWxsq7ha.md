# 更新群管理员

doc_id: VVYWxsq7ha
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/chat/subadmin/update
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
- chatid (String, required): 群会话ID，可通过创建群接口获取chatid参数值。
- userids (String, required): 群成员userId，可通过根据手机号查询用户接口获取userId参数值。
- role (Number, required): - **2**：添加为管理员。 - **3**：删除该管理员。

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/set-chat-admin
updated_at: 2026-08-25 09:37:15
