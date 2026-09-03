# 创建角色

doc_id: IzZ9nGx5sJ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/role/add_role
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
- roleName (String, required): 角色名称。
- groupId (Number, required): 角色组ID。 - 如果要加入的角色组已存在，调用获取角色列表接口获取。 - 如果尚未创建角色组，先调用创建角色组接口创建角色组，并获取角色组ID。

## Returns
- optional: roleId(Number), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/address-book-add-role
updated_at: 2026-05-27 13:09:19
