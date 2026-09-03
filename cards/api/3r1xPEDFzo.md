# 获取学科实例列表

doc_id: 3r1xPEDFzo
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/subject/list
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
- cursor (Number, required): 游标，从0开始。
- size (Number, required): 每页数据条数。
- operator_userid (String, required): 用户的userId。
- period_code (String, required): 学段编码，调用获取学段元数据列表接口获取period_code参数值。
- optional: data_order_type(Number), sort_type(Number), subject_code_list(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), result(PageQueryResponse), next_cursor(Number), has_more(Boolean), list(SubjectInstanceDTO[]), subject_code(String), subject_name(String), period_code(String), total_count(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-the-list-of-subject-examples
updated_at: 2026-06-08 09:47:37
