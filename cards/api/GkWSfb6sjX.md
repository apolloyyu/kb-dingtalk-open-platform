# 获取公告ID列表

doc_id: GkWSfb6sjX
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/blackboard/listids
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_blackboard_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- query_request (OapiBlackboardQueryVo, required): 请求对象。
- operation_userid (String, required): 操作人userId，必须是公告管理员。
- page_size (Number, required): 分页大小，从1开始不超过30，且必须为正整数。
- page (Number, required): 页码，从1开始且必须为正整数。
- optional: start_time(Date), end_time(Date), category_id(String)

## Returns
- optional: result(String[]), success(Boolean), errcode(Number), request_id(String)

## Limits
- 分页大小，从1开始不超过30，且必须为正整数。
- 开始时间。 - 如果只传**start_time**，**start_time**距当前时间不能超过180天。 - 如果传**start_time**和**end_time**，时间间隔不能超过180天。 - 如果不传**start_time**和**end_time**，默认获取近一个月内的公告信息。
- 结束时间。 - 如果只传**start_time**，**start_time**距当前时间不能超过180天。 - 如果传**start_time**和**end_time**，时间间隔不能超过180天。 - 如果不传**start_time**和**end_time**，默认获取近一个月内的公告信息。

source_url: https://open.dingtalk.com/document/development/obtains-the-id-list-of-announcements-that-are-not-deleted
updated_at: 2026-05-29 09:13:32
