# 获取部门列表

doc_id: cTgeghLflS
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/dept/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_addresslist_edu_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- page_size (Number, required): 每页大小，最大30。
- page_no (Number, required): 页码，从1开始。
- optional: super_id(Number)

## Returns
- optional: result(OpenEduDeptListResponse), details(OpenEduDeptDetails[]), nick(String), chain(String), feature(String), name(String), contact_type(String), dept_type(String), dept_id(Number), has_more(Boolean), super_id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 每页大小，最大30。

source_url: https://open.dingtalk.com/document/development/obtains-the-department-node-list
updated_at: 2026-06-08 09:48:03
