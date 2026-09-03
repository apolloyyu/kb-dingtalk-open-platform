# 获取班级内学生的关系列表

doc_id: yVd6G2j5WY
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/user/relation/list
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
- page_no (Number, required): 页码，从1开始。
- page_size (Number, required): 每页大小，取值1~30。
- class_id (Number, required): 班级ID，可调用获取部门列表接口获取dept_type为class时的dept_id参数值。

## Returns
- optional: result(Result), has_more(Boolean), relations(OpenEduUserRelationDetail[]), class_id(Number), relation_name(String), relation_code(String), from_userid(String), to_userid(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-list-of-relationships
updated_at: 2026-06-08 09:48:07
