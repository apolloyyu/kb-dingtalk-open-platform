# 设置禁止群成员私聊

doc_id: 0s8TsaLqIS
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update
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
- chatid (String, required): 企业会话ID。可以通过以下方式获取。 - 调用服务端创建群会话接口获取chatid参数值。 - 调用客户端chooseChat获取chatId参数值。
- is_prohibit (Boolean, required): 是否开启禁止开关。 - **true**：开启禁止开关 - **false**：关闭禁止开关

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/set-private-chat
updated_at: 2026-07-14 09:22:03
