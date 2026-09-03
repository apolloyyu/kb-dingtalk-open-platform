# 获取考勤报表列定义

doc_id: 2vxROY8oRL
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getattcolumns
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- none

## Returns
- optional: request_id(String), errcode(Number), result(AttColumnsForTopVo), columns(ColumnForTopVo[]), id(Number), type(Number), name(String), alias(String), status(Number), sub_type(Number), expression_id(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-enterprise-attendance-report-column
updated_at: 2026-05-27 17:06:18
