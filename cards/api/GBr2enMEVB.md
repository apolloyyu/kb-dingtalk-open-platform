# 获取部门详情

doc_id: GBr2enMEVB
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/dept/get
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
- dept_id (Number, required): 家校部门ID，可调用获取部门列表接口获取dept_id参数值。

## Returns
- optional: result(Result), detail(OpenEduDeptDetail), nick(String), chain(String), feature(String), name(String), contact_type(String), dept_type(String), dept_id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-queries-department-details
updated_at: 2026-07-20 09:21:48
