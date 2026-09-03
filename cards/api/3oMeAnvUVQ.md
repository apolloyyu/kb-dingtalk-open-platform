# 获取部门用户userid列表

doc_id: 3oMeAnvUVQ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/user/listid
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- dept_id (Number, required): 部门deptId，可通过调用获取部门列表获取部门deptId。 **[!NOTE]** 如果是根部门，该参数传1。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(ListUserByDeptResponse), userid_list(String[])

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-list-of-department-userids
updated_at: 2026-06-08 09:28:34
