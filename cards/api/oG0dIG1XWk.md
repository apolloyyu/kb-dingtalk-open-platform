# 获取日志统计数据

doc_id: oG0dIG1XWk
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/report/statistics
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- report_id (String, required): 日志ID。调用获取用户发送日志的概要信息或获取用户发出的日志列表接口获取report_id参数值。

## Returns
- optional: result(ReportStatisticsVo), read_num(Number), comment_num(Number), comment_user_num(Number), like_num(Number), errcode(Number), request_id(String), success(Boolean)

## Limits
- > 为统一数据资产管理体验，钉钉数据资产平台已整合原分散的数据服务。本接口及另外 60 个数据资产类OpenAPI 已停止新权限申请，本文档同步迁入「历史文档」目录。

source_url: https://open.dingtalk.com/document/development/query-log-statistics
updated_at: 2026-08-25 09:38:08
