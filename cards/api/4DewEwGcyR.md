# 获取部门下人员列表

doc_id: 4DewEwGcyR
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/industry/user/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_industry_info_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- dept_id (Number, required): 部门id，可调用获取部门列表接口获取dept_id参数值。
- size (Number, required): 分页查询的大小，最大值1000。
- optional: role(String), cursor(Number)

## Returns
- optional: result(ResultWrapper), has_more(Boolean), next_cursor(Number), details(OpenIndustryEmp[]), feature(String), roles(OpenRole[]), name(String), id(Number), userid(String), unionid(String), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 分页查询的大小，最大值1000。

source_url: https://open.dingtalk.com/document/development/obtains-the-list-of-people-under-a-department
updated_at: 2026-05-27 13:09:38
