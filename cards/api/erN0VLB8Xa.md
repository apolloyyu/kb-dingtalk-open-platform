# 更新群

doc_id: erN0VLB8Xa
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/chat/update
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
- chatid (String, required): 群会话ID。 - 仅支持通过调用服务端创建群接口获取的chatid参数值。 - 不支持通过调用前端JSAPI获取的chatid。
- optional: name(String), owner(String), ownerType(String), add_useridlist(String[]), del_useridlist(String[]), add_extidlist(String[]), del_extidlist(String[]), icon(String), searchable(Number), validationType(Number), mentionAllAuthority(Number), managementType(Number), chatBannedType(Number), showHistoryType(Number), isBan(boolean)

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- 群名称，长度限制为1~20个字符。
- 添加的群成员列表，每次最多支持40人，群人数上限为1000。 可通过根据手机号查询用户接口获取userId。
- 新成员是否可查看100条历史消息。 - **1**：可查看 - **0**：不可查看 **[!NOTE]** 如果不传值，代表不可查看。

source_url: https://open.dingtalk.com/document/development/modify-a-group-session
updated_at: 2026-08-25 09:37:14
