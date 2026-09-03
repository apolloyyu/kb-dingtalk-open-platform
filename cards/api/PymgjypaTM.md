# 设定角色成员管理范围

doc_id: PymgjypaTM
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/role/scope/update
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
- userid (String, required): 员工在企业中的userId。
- role_id (Number, required): 角色ID，可以调用获取角色列表接口获取id参数值。
- optional: dept_ids(String)

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- 部门ID列表，多个部门id之间使用逗号分隔。 最多支持50个部门ID，不传则设置范围为所有人。

source_url: https://open.dingtalk.com/document/development/update-role-member-management-department-scope
updated_at: 2026-05-27 13:09:25
