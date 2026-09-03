# 获取学科实例详情

doc_id: X2oMw3wfnN
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/subject/get
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_maindata_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- operator_userid (String, required): 用户的userId。
- period_code (String, required): 学段编码，调用获取学段元数据列表接口获取period_code参数值。
- optional: subject_code(String), subject_name(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), result(SubjectInstanceDTO), subject_code(String), period_code(String), subject_name(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-dingtalk-education-subject-instances
updated_at: 2026-06-08 09:47:36
