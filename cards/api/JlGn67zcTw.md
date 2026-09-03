# 获取日志评论详情

doc_id: JlGn67zcTw
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/comment/list
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
- report_id (String, required): 日志ID，可通过获取用户发送日志的概要信息或获取用户发出的日志列表接口获取report_id参数值。
- optional: offset(Number), size(Number)

## Returns
- optional: result(ReportPageVo), comments(ReportCommentVo[]), create_time(Date), content(String), userid(String), has_more(Boolean), next_cursor(Number), errcode(Number), request_id(String), success(Boolean)

## Limits
- 分页参数，每页大小，最多传20，默认值为20。

source_url: https://open.dingtalk.com/document/development/queries-log-comment-details
updated_at: 2026-05-27 13:10:21
