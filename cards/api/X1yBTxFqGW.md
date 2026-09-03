# 更新部门

doc_id: X1yBTxFqGW
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/department/update
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
- dept_id (Number, required): 部门ID，可通过获取部门列表接口获取dept_id参数值。
- optional: parent_id(Number), hide_dept(Boolean), dept_permits(String), user_permits(String), create_dept_group(Boolean), order(Number), name(String), source_identifier(String), outer_dept(Boolean), outer_permit_users(String), outer_permit_depts(String), outer_dept_only_self(Boolean), language(String), auto_add_user(Boolean), auto_approve_apply(Boolean), dept_manager_userid_list(String), group_contain_sub_dept(Boolean), group_contain_outer_dept(Boolean), group_contain_hidden_dept(Boolean), org_dept_owner(String), force_update_fields(String), code(String)

## Returns
- optional: errcode(Number), errmsg(String), request_id(String)

## Limits
- 部门名称，长度限制为1~64个字符，不允许包含字符‘-’‘，’以及‘,’。
- 是否限制本部门成员查看通讯录： - **true**：开启限制。开启后本部门成员只能看到限定范围内的通讯录 - **false**：不限制 不传值，则保持不变。
- 本部门成员是否只能看到所在部门及下级部门通讯录： - **true**：只能看到所在部门及下级部门通讯录 - **false**：不能查看所有通讯录，在通讯录中仅能看到自己 当**outer_dept**为**true**时，此参数生效。 不传值，则保持不变。
- 部门编码，最多30个字符。 **[!NOTE]** 该字段只能通过本接口进行设置。

source_url: https://open.dingtalk.com/document/development/address-book-update-department
updated_at: 2026-06-08 09:23:10
