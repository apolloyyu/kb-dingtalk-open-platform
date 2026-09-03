# 服务号菜单更新

doc_id: bt4AXxlQCm
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/serviceaccount/menu/update
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
- name (String, required): 菜单名称。
- enable_input (Boolean, required): 是否允许用户输入： - **true**：允许 - **false**：不允许
- status (Number, required): 状态： - **0**：正常 - **1**：停用
- optional: menu(MenuConfigDTO), button(MenuButtonDTO[]), type(String), key(String), url(String), media_id(String), sub_button(MenuSubButtonDTO[])

## Returns
- optional: errmsg(String), errcode(Number), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/service-number-menu-update
updated_at: 2026-06-01 09:15:49
