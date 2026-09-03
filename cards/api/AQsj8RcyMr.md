# 创建部门

doc_id: AQsj8RcyMr
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/department/create
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
- name (String, required): 部门名称。 长度限制为1~64个字符，不允许包含字符"-"","以及","。
- parent_id (Number, required): 父部门ID，根部门ID为1。
- optional: hide_dept(Boolean), dept_permits(String), user_permits(String), outer_dept(Boolean), outer_dept_only_self(Boolean), outer_permit_users(String), outer_permit_depts(String), create_dept_group(Boolean), auto_approve_apply(Boolean), order(Number), source_identifier(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(DeptCreateResponse), dept_id(Number)

## Limits
- 部门名称。 长度限制为1~64个字符，不允许包含字符"-"","以及","。
- 是否限制本部门成员查看通讯录： - **true**：开启限制。开启后本部门成员只能看到限定范围内的通讯录 - **false（默认值）**：不限制
- 本部门成员是否只能看到所在部门及下级部门通讯录： - **true**：只能看到所在部门及下级部门通讯录 - **false**：不能查看所有通讯录，在通讯录中仅能看到自己 当**outer_dept**为**true**时，此参数生效。

source_url: https://open.dingtalk.com/document/development/address-book-creation-department-established-department
updated_at: 2026-05-27 13:09:10
