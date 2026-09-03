# 修改课程

doc_id: p0azO2ae6O
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/update
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
- introduce (String, required): 课程介绍。
- name (String, required): 课程名称。
- op_userid (String, required): 当前用户的userId。
- optional: teacher_corpid(String), teacher_userid(String), start_time(Number), end_time(Number)

## Returns
- optional: request_id(String), result(Boolean), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/modify-course
updated_at: 2026-06-08 09:47:40
