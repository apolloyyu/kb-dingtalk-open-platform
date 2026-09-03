# 获取用户日志未读数

doc_id: 9ZE3KRgQ3Q
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/getunreadcount
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_report_query

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 要获取的员工userId。

## Returns
- optional: count(Number), request_id(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/querying-the-employee-s-log-is-not-reading
updated_at: 2026-05-27 13:10:22
