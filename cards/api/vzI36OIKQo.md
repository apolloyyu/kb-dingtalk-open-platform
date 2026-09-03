# 获取部门详情

doc_id: vzI36OIKQo
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/department/get
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_department_list

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- dept_id (Number, required): 部门ID，根部门ID为1，可调用获取部门列表接口获取dept_id参数值。
- optional: language(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(DeptGetResponse), dept_id(Number), name(String), parent_id(Number), source_identifier(String), create_dept_group(Boolean), auto_add_user(Boolean), tags(String), from_union_org(Boolean), order(Number), dept_group_chat_id(String), group_contain_sub_dept(Boolean), org_dept_owner(String), dept_manager_userid_list(String[]), outer_dept(Boolean), outer_permit_depts(Number[]), outer_permit_users(String[]), user_permits(String[]), hide_dept(Boolean), dept_permits(Number[]), auto_approve_apply(Boolean), code(String), member_count(Number), owning_member_count(Number), union_dept_ext(Object), deptId(Number), corpId(String)

## Limits
- 是否限制本部门成员查看通讯录： - **true**：开启限制。开启后本部门成员**只能看到指定部门/人**的通讯录 - **false**：不限制图片
- 配置的部门员工可见部门Id列表。 **[!NOTE]** 企业设置限制本部门成员查看通讯录，即返回**outer_dept**值。图片 - **限制本部门成员查看通讯录**（即**outer_dept**为**true**）：outer_permit_depts表示设置的**只能看到指定部门/人**的**部门Id列表**。 **[!NOTE]** 例如，企业开启了限制本部门成员查看通讯录，本部门成员设置了只能看到指定的2个部门、2位员工的通讯录，其中测试部门1的部门Id为1，
- 配置的部门员工可见员工userId列表。 **[!NOTE]** 企业设置限制本部门成员查看通讯录，即返回**outer_dept**值。图片 - **限制本部门成员查看通讯录**（即**outer_dept**为**true**）：outer_permit_users表示设置的**只能看到指定部门/人**的**员工userId列表**。 **[!NOTE]** 例如，企业开启了限制本部门成员查看通讯录，本部门成员设置了只能看到指定的2个部门、2位员工的通讯录，其中员工小钉1
- 隐藏部门的员工userId列表。 **[!NOTE]** 企业开启隐藏本部门，即返回**hide_dept**值。 EE5D7BF8-88D1-4084-B369-F908A75D7333 - **开启隐藏本部门**（即hide_dept为true）：user_permits表示设置的**允许指定部门/人可见**的**员工userId列表。** **[!NOTE]** 例如，企业开启了隐藏本部门，且分别设置2个部门、2位员工允许指定部门/人可见，其中员工小钉1的userId为
- 隐藏部门的部门Id列表。 **[!NOTE]** 企业开启隐藏本部门，即返回**hide_dept**值。EE5D7BF8-88D1-4084-B369-F908A75D7333 - **开启隐藏本部门**（即hide_dept为true）：dept_permits表示设置的**允许指定部门/人可见**的**部门Id列表。** **[!NOTE]** 例如，企业开启了隐藏本部门，且分别设置2个部门、2位员工允许指定部门/人可见，其中测试部门1的部门Id为1，测试部门2的部门I

source_url: https://open.dingtalk.com/document/development/query-department-details0-v2
updated_at: 2026-06-08 09:22:39
