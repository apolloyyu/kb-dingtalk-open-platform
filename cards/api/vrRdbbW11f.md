# 获取学科元数据列表

doc_id: vrRdbbW11f
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/subject/metadata/list
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
- cursor (Number, required): 分页游标，从0开始。
- operator_userid (String, required): 用户的userId。
- period_code (String, required): 学段编码，调用获取学科元数据列表接口获取period_code参数值。
- area_code (String, required): 地区编码。
- size (Number, required): 每页数据条数。
- optional: level(Number), parent_id(Number), data_order_type(Number), sort_type(Number)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), result(PageQueryResponse), next_cursor(Number), has_more(Boolean), list(SubjectMetadataDTO[]), id(Number), area_code(String), period_code(String), parent_id(Number), level(Number), subject_name(String), subject_code(String), total_count(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject
updated_at: 2026-06-08 09:47:38
