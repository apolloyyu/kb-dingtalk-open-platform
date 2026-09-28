# 补卡自动同步：审批通过实时更新钉钉考勤状态

doc_id: nTMMOfrMW3
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday
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
- - **审计留痕**：每次同步/撤销操作记录操作人、时间戳、审批单ID，满足合规要求。
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- 1. **分批处理**：每次批量不超过50人，避免单次请求超时。
- - `网络超时`：自动重试3次，间隔递增（1s/2s/4s）。
- 3. **异常监控**：对连续3次同步失败的员工触发告警，通知HR管理员手动核查（可能原因：员工离职未移除考勤组、排班未配置等）。

source_url: https://open.dingtalk.com/document/development/the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized
updated_at: 2026-09-23 12:04:28
