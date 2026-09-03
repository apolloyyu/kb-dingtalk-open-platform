# 加入课程

doc_id: 7StToH2AKb
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/join
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
- course_code (String, required): 需要加入的课程编码，调用创建课程接口获取course_code参数值。
- op_user_id (String, required): 当前操作用户的userId。

## Returns
- optional: result(JoinCourseResponse), join_url(String), joinable(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/join-course
updated_at: 2026-06-08 09:47:48
