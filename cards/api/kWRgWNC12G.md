# 获取课程列表

doc_id: kWRgWNC12G
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/list
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
- op_userid (String, required): 当前操作人的userId。
- cursor (Number, required): 分页游标，从0开始。
- size (Number, required): 分页大小，取值1~100。

## Returns
- optional: request_id(String), success(Boolean), errcode(Number), errmsg(String), result(ListCourseResponse), has_more(Boolean), list(CourseVO[]), biz_key(String), teacher_userid(String), teacher_corpid(String), end_time(Number), start_time(Number), introduce(String), name(String), code(String), next_cursor(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-course-list
updated_at: 2026-06-08 09:47:43
