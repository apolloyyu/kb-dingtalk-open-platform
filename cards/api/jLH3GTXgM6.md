# 查询企业下用户待办列表

doc_id: jLH3GTXgM6
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/workrecord/getbyuserid
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 要查询的用户userid。
- offset (Number, required): 分页游标，从0开始，如返回结果中has_more为true，则表示还有数据，offset再传上一次的offset+limit。
- limit (Number, required): 分页大小，最多50。
- status (Number, required): 待办任务状态： - **0**：未完成 - **1**：完成

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), records(PageResult), has_more(Boolean), list(WorkRecordVo[]), record_id(String), create_time(Number), title(String), url(String), forms(FormItemVo[]), content(String)

## Limits
- 分页大小，最多50。

source_url: https://open.dingtalk.com/document/development/get-the-user-s-to-do-items
updated_at: 2026-08-25 09:38:12
