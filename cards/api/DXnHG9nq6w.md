# 通知自动发布：从自有系统到钉钉公告的触达闭环

doc_id: DXnHG9nq6w
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/blackboard/create
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
- - **公告自动发布**：OA系统创建公告后1秒内自动发布至钉钉公告模块，无需手动重新编辑。
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

source_url: https://open.dingtalk.com/document/development/create-and-delete-announcements
updated_at: 2026-09-23 12:04:36
