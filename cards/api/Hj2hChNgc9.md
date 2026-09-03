# 注册互动卡片回调地址

doc_id: Hj2hChNgc9
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scencegroup/interactivecard/callback/register
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- callback_url (String, required): 回调URL地址。 **[!NOTE]** URL地址不支持携带参数，
- optional: api_secret(String), callbackRouteKey(String), forceUpdate(Boolean)

## Returns
- optional: result(Json), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/registration-card-interaction-callback-address-1
updated_at: 2026-08-25 09:37:08
