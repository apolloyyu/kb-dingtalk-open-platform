# 批量增加员工角色

doc_id: 6ImP1pWE1K
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/role/addrolesforemps
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
- roleIds (String, required): 角色roleId列表，可调用获取角色列表接口获取。 多个roleId用英文逗号（,）分隔，最多可传20个。
- userIds (String, required): 员工的userId，可通过调用根据手机号查询用户获取。 多个userId用英文逗号（,）分隔，最多可传20个。

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- 角色roleId列表，可调用获取角色列表接口获取。 多个roleId用英文逗号（,）分隔，最多可传20个。
- 员工的userId，可通过调用根据手机号查询用户获取。 多个userId用英文逗号（,）分隔，最多可传20个。

source_url: https://open.dingtalk.com/document/development/add-role-information-to-employees-in-batches
updated_at: 2026-05-27 13:09:22
