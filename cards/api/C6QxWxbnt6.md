# 创建群

doc_id: C6QxWxbnt6
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/chat/create
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
- name (String, required): 群名称，长度限制为1~20个字符。
- owner (String, required): 群主的userId，可通过根据手机号查询用户接口获取userid参数值。 **[!NOTE]** 该员工必须为会话**useridlist**的成员之一。
- useridlist (String[], required): 群成员列表，每次最多支持40人，群人数上限为1000。 可通过根据手机号查询用户接口获取userid参数值。
- optional: showHistoryType(Number), searchable(Number), validationType(Number), mentionAllAuthority(Number), managementType(Number), chatBannedType(Number)

## Returns
- optional: openConversationId(String), chatid(String), conversationTag(Number), errmsg(String), errcode(Number)

## Limits
- 群名称，长度限制为1~20个字符。
- 群成员列表，每次最多支持40人，群人数上限为1000。 可通过根据手机号查询用户接口获取userid参数值。
- 新成员是否可查看100条历史消息： - **1**：可查看 - **0**：不可查看 **[!NOTE]** 如果不传值，代表不可查看。

source_url: https://open.dingtalk.com/document/development/session-management-creates-groups
updated_at: 2026-08-25 09:37:13
