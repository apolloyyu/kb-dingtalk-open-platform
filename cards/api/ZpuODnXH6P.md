# 获取学生ID列表

doc_id: ZpuODnXH6P
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/class/studentid/get
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_homework_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- class_id (Number, required): 班级ID，调用获取部门列表接口获取dept_type为class时的dept_id参数值。
- app_id (Number, required): 应用ID，可在开发者后台的**应用信息**页面查看。image
- userid (String, required): 教师userId。

## Returns
- optional: result(OpenEduSelectStudentIdResponse), class_id(Number), student_ids(String[]), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/retrieve-student-based-class
updated_at: 2026-06-08 09:48:18
