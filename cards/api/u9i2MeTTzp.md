# 考勤数据抽查：跨部门考勤核查与异常预警

doc_id: u9i2MeTTzp
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/isopensmartreport
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- none

## Limits
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - `size`：分页大小，最大100。
- - `column_id_list`：报表列ID，多值用英文逗号分隔，每次最多传20个。
- - `to_date`：结束时间，与开始时间间隔不超过31天。
- 结束时间减去开始时间必须在31天以内。如需获取更长时间范围的数据，需分段多次调用，每次查询不超过31天。
- - **Q4：columnIdList参数最多支持多少个列ID？**
- 每次最多传20个列ID，多个列ID用英文逗号分隔。如需查询超过20个列的数据，需分多次调用。

source_url: https://open.dingtalk.com/document/development/hidden-common-callback-events
updated_at: 2026-11-06 11:34:15
