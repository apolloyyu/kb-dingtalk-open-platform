# 获取审批实例ID列表

doc_id: TG2aHOIvY1
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/processinstance/listids
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
- process_code (String, required): 审批流的唯一码。 process_code在审批模板编辑页面的URL中获取。
- start_time (Number, required): 审批实例开始时间。Unix时间戳，单位毫秒。 例如：获取审批单发起时间在2020.4.10-2020.4.14之间审批单，该值传2020.4.10 00:00:00对应的时间戳1586448000000。
- optional: end_time(Number), size(Number), cursor(Number), userid_list(String)

## Returns
- optional: result(PageResult), list(String[]), next_cursor(Number), errcode(Number), errmsg(String), request_id(String)

## Limits
- 分页参数，每页大小，最多传20。
- 发起userid列表，最大列表长度为10。
- - 如果只传了**start_time**参数，这个时间距离当前时间不能超过120天，**end_time**不传则默认取当前时间。
- - 如果传了**start_time**和**end_time**，时间范围不能超过120天，同时**start_time**时间距当前时间不能超过365天。
- - 批量获取的实例ID个数（循环获取），最多不能超过10000个。

source_url: https://open.dingtalk.com/document/development/operation-to-retrieve-a-list-of
updated_at: 2026-08-25 09:37:44
