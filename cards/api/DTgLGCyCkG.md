# 获取课程参与方列表

doc_id: DTgLGCyCkG
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/participant/list
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
- course_code (String, required): 课程唯一编码，调用创建课程接口获取course_code参数值。
- op_userid (String, required): 当前操作人的userId。
- cursor (Number, required): 分页游标，从0开始。
- size (Number, required): 分页大小，取值1~100。

## Returns
- optional: result(ListCourseParticipantResponse), has_more(Boolean), list(CourseParticipantVO[]), role(String), participant_id(String), participant_type(String), participant_corpid(String), next_cursor(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-a-list-of-course-participants
updated_at: 2026-06-08 09:47:46
