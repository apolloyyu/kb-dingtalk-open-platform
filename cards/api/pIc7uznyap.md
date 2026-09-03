# 获取用户可见的日志模板

doc_id: pIc7uznyap
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/template/listbyuserid
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_report_statistics, qyapi_report_query

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- optional: userid(String), offset(Number), size(Number)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(HomePageReportTemplateVo), template_list(ReportTemplateTopVo[]), name(String), icon_url(String), report_code(String), url(String), next_cursor(Number)

## Limits
- 分页大小，最大可设置成100。

source_url: https://open.dingtalk.com/document/development/obtains-the-list-of-visible-log-templates-based-on-the
updated_at: 2026-05-27 13:10:23
