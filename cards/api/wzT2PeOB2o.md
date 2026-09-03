# 获取指定用户的所有父部门列表

doc_id: wzT2PeOB2o
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser
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
- userid (String, required): 要查询的用户的userid。

## Returns
- optional: errcode(Number), request_id(String), errmsg(String), result(DeptListParentByUserResponse), parent_list(DeptParentResponse[]), parent_dept_id_list(Number[])

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-list-of-all-parent-departments-of-a-user
updated_at: 2026-05-27 13:09:18
