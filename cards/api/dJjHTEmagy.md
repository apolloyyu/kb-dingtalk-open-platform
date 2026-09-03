# 获取日志相关人员列表

doc_id: dJjHTEmagy
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/statistics/listbytype
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
- type (Number, required): 查询类型： - **0**：已读人员列表 - **1**：评论人员列表 - **2**：点赞人员列表
- optional: offset(Number), size(Number)

## Returns
- optional: success(Boolean), request_id(String), errcode(Number), result(ReportPageVo), next_cursor(Number), has_more(Boolean), userid_list(String[])

## Limits
- 分页参数，每页大小，最多传100，默认值为100。

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-log-related-personnel-by-type
updated_at: 2026-05-27 13:10:18
