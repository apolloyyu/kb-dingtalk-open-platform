# 查询是否启用智能统计报表

doc_id: 7i62hcupfY
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/isopensmartreport
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
- optional: result(IsOpenSmartReportForTopVo), smart_report(Boolean), request_id(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/determine-whether-to-enable-attendance-intelligent-report
updated_at: 2026-05-27 17:06:15
