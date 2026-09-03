# 获取日志接收人员列表

doc_id: haid495lC3
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/receiver/list
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
- report_id (String, required): 日志ID，可通过获取用户发送日志的概要信息或获取用户发出的日志列表接口获取report_id参数值。
- optional: offset(Number), size(Number)

## Returns
- optional: result(ReportPageVo), has_more(Boolean), next_cursor(Number), userid_list(String[]), errcode(Number), errmsg(String), success(Boolean)

## Limits
- 分页参数，每页大小，最多传100，默认值为100。

source_url: https://open.dingtalk.com/document/development/queries-log-sharing-personnel
updated_at: 2026-05-27 13:10:19
