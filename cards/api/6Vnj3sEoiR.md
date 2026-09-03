# 获取人员列表

doc_id: 6Vnj3sEoiR
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/user/list
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
- page_size (Number, required): 每页大小，取值1~30。
- page_no (Number, required): 页码，从1开始。
- role (String, required): 家校人员角色。 - **teacher**：老师 - **guardian**：监护人 - **student**：学生
- class_id (Number, required): 班级ID，可调用获取部门列表接口获取dept_type为class时的dept_id参数值。

## Returns
- optional: result(Result), has_more(Boolean), details(OpenEduUserDetail[]), class_id(Number), role(String), feature(String), is_adviser(String), student_no(String), name(String), unionid(String), userid(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-home-school-user-identities
updated_at: 2026-06-08 09:48:04
