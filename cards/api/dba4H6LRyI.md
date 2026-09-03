# 回放课程

doc_id: dba4H6LRyI
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/replay
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_course_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- course_code (String, required): 需要回放的课程编码，调用创建课程接口获取course_code参数值。
- op_user_id (String, required): 操作用户的userId。

## Returns
- optional: result(ReplayCourseResponse), replayable(Boolean), replay_urls(String[]), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/replay-course
updated_at: 2026-06-08 09:47:52
