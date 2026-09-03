# 创建自定义校区或部门

doc_id: TullpvkW0n
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/edu/customDepts
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_edu_safe

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- customDept (Object, required): 自定义校区或部门信息。
- type (String, required): 部门类型。 - **custom_campus**：自定义校区 - **custom_dept**：自定义部门
- name (String, required): 自定义校区或部门名称。
- superId (Long, required): 上级部门ID。 - 当**type**取值为**custom_campus**时，必须为-**7**。 - 当**type**取值为**custom_dept**时：调用获取部门列表接口获取dept_id参数值。
- operator (String, required): 操作人userId。

## Returns
- optional: success(Boolean), result(Object), deptId(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-custom-campus-or-department
updated_at: 2026-06-04 19:11:29
