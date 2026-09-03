# 更新角色名称

doc_id: LeDSh2tuq3
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/role/update_role
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
- roleId (Number, required): 要更新的角色ID，可以调用获取角色列表接口获取。 “默认”分组内的角色不支持修改，包括：负责人、主管、主管理员、子管理员。
- roleName (String, required): 修改的角色名称。

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-the-character-name
updated_at: 2026-05-27 13:09:21
