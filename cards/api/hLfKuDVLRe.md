# 更新群成员的群昵称

doc_id: hLfKuDVLRe
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/chat/updategroupnick
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_chat_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 要更改群昵称的群成员userId，可通过查询群信息接口获取群成员userId。
- chatid (String, required): 群会话ID，可通过创建群会话接口获取chatid参数值。
- group_nick (String, required): 该成员在群中的昵称。

## Returns
- optional: errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/set-a-group-nickname
updated_at: 2026-07-14 09:22:03
