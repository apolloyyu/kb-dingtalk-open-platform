# 创建角色组

doc_id: skpdJi9CsA
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/role/add_role_group
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_manage_addresslist

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- name (String, required): 角色组名称。

## Returns
- optional: errcode(Number), errmsg(String), groupId(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-a-role-group
updated_at: 2026-05-27 13:09:20
