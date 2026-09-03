# 获取学生信息

doc_id: dP2tYxPqgo
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/class/studentinfo/get
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
- app_id (Number, required): 应用ID，可在开发者后台的**应用信息**页面查看。 image
- userid (String, required): 学生的userId。

## Returns
- optional: result(OpenStudentSelectDto), userid(String), student_num(String), name(String), class_id(Number), avatar(String), guardians(OpenPatriarchSelectDto[]), relation(String), relation_name(String), is_active(Boolean), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-student-information
updated_at: 2026-06-08 09:48:19
