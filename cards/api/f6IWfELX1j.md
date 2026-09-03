# 更新群会话

doc_id: f6IWfELX1j
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/group/update
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
- chatid (String, required): 群会话ID，可通过调用创建群会话接口获取的chatid参数值。 **[!NOTE]** 不支持通过调用前端JSAPI获取的chatid。
- optional: name(String), owner(String), ownerType(String), add_useridlist(Array of String), del_useridlist(Array of String), add_extidlist(Array of String), del_extidlist(Array of String), icon(String), managementOptions(Object), mentionAllAuthority(Integer), showHistoryType(Integer), validationType(Integer), searchable(Integer), chatBannedType(Integer), managementType(Integer)

## Returns
- optional: success(Boolean)

## Limits
- 群名称，长度限制为1~20个字符。
- 新成员是否可查看100条历史消息。 - **1**：可查看 - **0**：不可查看 **[!NOTE]** 如果不传值，代表不可查看。

source_url: https://open.dingtalk.com/document/development/api-updategroup
updated_at: 2026-06-02 19:00:12
