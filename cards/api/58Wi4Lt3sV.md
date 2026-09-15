# 企业通讯录员工管理自动化

doc_id: 58Wi4Lt3sV
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/v2/user/create
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
- - 批量处理效率：千人级批量导入应在30分钟内完成，否则检查网络或分批策略。

source_url: https://open.dingtalk.com/document/development/address-book-employee-operations
updated_at: 2026-09-15 09:36:19
