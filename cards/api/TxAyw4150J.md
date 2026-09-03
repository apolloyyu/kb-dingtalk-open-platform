# 获取指定部门的所有父部门列表

doc_id: TxAyw4150J
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/department/listparentbydept
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
- dept_id (Number, required): 要查询的部门ID，可调用获取部门列表接口获取dept_id参数值。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(DeptListParentByDeptIdResponse), parent_id_list(Number[])

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-list-of-all-parent-departments-of-a-department
updated_at: 2026-05-27 13:09:17
