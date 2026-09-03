# 获取课堂概要数据

doc_id: fKxD2K6Cpe
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/summadata/list
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
- cursor (Number, required): 分页游标，从0开始。
- size (Number, required): 分页大小。
- course_code (String, required): 课程唯一编码，调用创建课程接口获取course_code参数值。
- op_userid (String, required): 当前操作人的userId。
- category_codes (String[], required): 数据类别编码数组，可参考数据类别介绍。

## Returns
- optional: result(PageQueryResponse), next_cursor(Number), has_more(Boolean), list(CourseSummaryDataDTO[]), category_code(String), category_biz_key(String), data(Json), course_code(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-course-summary-data
updated_at: 2026-07-20 09:21:45
