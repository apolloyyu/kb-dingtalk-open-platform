# 删除课程

doc_id: fzJfty5DI8
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/delete
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_course_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- course_code (String, required): 课程唯一编码，调用创建课程接口获取course_code参数值。
- op_userid (String, required): 当前操作人的userId。

## Returns
- optional: request_id(String), result(Boolean), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-course
updated_at: 2026-06-08 09:47:41
