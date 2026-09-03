# 创建群会话

doc_id: bVZ7zI1LZf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/group/create
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 群名称，长度限制为1~20个字符。
- owner (String, required): 群主的userId，可通过根据手机号查询用户接口获取userId。
- useridlist (Array of String, required): 用户的StaffId。
- optional: ownerType(String), conversationTag(Long), extidlist(Array of String), icon(String), managementOptions(Object), mentionAllAuthority(Integer), showHistoryType(Integer), validationType(Integer), searchable(Integer), chatBannedType(Integer), managementType(Integer)

## Returns
- optional: conversationTag(Long), openConversationId(String), chatid(String)

## Limits
- 群名称，长度限制为1~20个字符。
- 新成员是否可查看100条历史消息，如果不传值，代表不可查看。 - **1**：可查看 - **0**：不可查看

source_url: https://open.dingtalk.com/document/development/create-common-group-new-version-v2
updated_at: 2026-06-04 19:09:49
