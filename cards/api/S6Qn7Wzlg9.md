# 创建学科实例

doc_id: S6Qn7Wzlg9
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/subject/create
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_maindata_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- operator_userid (String, required): 操作人的userId。
- period_code (String, required): 学段编码，调用获取学段元数据列表接口获取period_code参数值。
- subject_code (String, required): 学科编码，调用获取学科元数据列表接口获取subject_code参数值。
- subject_name (String, required): 学科名称。

## Returns
- optional: result(String), success(Boolean), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-dingtalk-education-subject-instance
updated_at: 2026-06-08 09:47:31
