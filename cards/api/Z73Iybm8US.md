# 开始课程

doc_id: Z73Iybm8US
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/start
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
- course_code (String, required): 需要开始的课程编码，调用创建课程接口获取course_code参数值。
- op_user_id (String, required): 操作用户的userId。
- optional: start_option(StartOption), b_allow_join_in_advance(Boolean)

## Returns
- optional: result(StartCourseResponse), target_type(Number), target_id(String), is_reuse(Boolean), success(Boolean), errcode(Number), errmsg(String)

## Limits
- 是否允许提前进入课堂。 - **true**：表明生成的课堂可以允许学生最多提前30分钟进入 - **false**（默认）：不允许学生提前进入课堂，只有老师发起后才可进入。

source_url: https://open.dingtalk.com/document/development/start-course
updated_at: 2026-06-08 09:47:50
