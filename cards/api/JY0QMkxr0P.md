# 查询服务号菜单

doc_id: JY0QMkxr0P
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/serviceaccount/menu/get
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_service_account_menu

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- unionid (String, required): 服务号的unionid，可通过查询服务号列表接口获取。

## Returns
- optional: errmsg(String), errcode(Number), request_id(String), menu(MenuConfigDTO), button(MenuButtonDTO[]), name(String), type(String), key(String), url(String), media_id(String), sub_button(MenuSubButtonDTO[]), enable_input(Boolean), status(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-service-number-menu-1
updated_at: 2026-06-01 09:15:50
