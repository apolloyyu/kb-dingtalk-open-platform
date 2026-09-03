# 获取入群二维码链接

doc_id: 3wHxW0nbs6
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/chat/qrcode/get
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_chat_base_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- chatid (String, required): 群会话的chatid，可调用创建群会话接口获取chatid参数值。
- userid (String, required): 分享二维码用户的userId。

## Returns
- optional: result(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-a-qr-code-link
updated_at: 2026-07-14 09:22:04
