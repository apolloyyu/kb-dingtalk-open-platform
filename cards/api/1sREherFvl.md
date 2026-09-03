# 批量删除员工角色

doc_id: 1sREherFvl
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/role/removerolesforemps
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
- roleIds (String, required): 角色roleId列表，可调用获取角色列表接口获取。 最大列表长度为20，多个roleId用英文逗号（,）分隔。
- userIds (String, required): 员工的userid，可通过调用根据手机号查询用户获取userId。 最大列表长度为100，多个userId用英文逗号（,）分隔。

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- 角色roleId列表，可调用获取角色列表接口获取。 最大列表长度为20，多个roleId用英文逗号（,）分隔。
- 员工的userid，可通过调用根据手机号查询用户获取userId。 最大列表长度为100，多个userId用英文逗号（,）分隔。

source_url: https://open.dingtalk.com/document/development/delete-the-color-information-of-employee-corners-in-batches
updated_at: 2026-05-27 13:09:24
