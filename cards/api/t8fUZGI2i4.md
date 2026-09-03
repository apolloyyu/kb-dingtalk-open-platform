# 创建课程

doc_id: t8fUZGI2i4
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/create
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
- op_userid (String, required): 当前用户的userId。
- teacher_corpid (String, required): 老师的组织的corpId。CorpId
- teacher_userid (String, required): 老师的userId。
- introduce (String, required): 课程介绍。
- biz_key (String, required): 业务唯一键，用于保证课程的唯一性，防止重复创建。
- name (String, required): 课程名称。
- optional: start_time(Number), end_time(Number)

## Returns
- optional: course_code(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-course
updated_at: 2026-06-08 09:47:39
