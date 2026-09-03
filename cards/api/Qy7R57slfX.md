# 获取部门列表

doc_id: Qy7R57slfX
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/department/listsub
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
- optional: dept_id(Number), language(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(DeptBaseResponse[]), dept_id(Number), name(String), parent_id(Number), create_dept_group(Boolean), auto_add_user(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/user-management-acquires-the-list-departments
updated_at: 2026-05-27 13:09:15
