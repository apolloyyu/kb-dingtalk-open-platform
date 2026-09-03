# 获取部门列表

doc_id: rcKzSW9wpT
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/industry/department/list
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
- dept_id (Number, required): 父部门ID，行业根部门传1。
- size (Number, required): 分页查询的大小，最大值1000。
- optional: cursor(Number)

## Returns
- optional: result(ResultWrapper), details(OpenIndustryDeptInfo[]), feature(String), contact_type(String), dept_type(String), name(String), dept_id(Number), next_cursor(Number), has_more(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 分页查询的大小，最大值1000。

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-industry-departments
updated_at: 2026-05-27 13:09:36
