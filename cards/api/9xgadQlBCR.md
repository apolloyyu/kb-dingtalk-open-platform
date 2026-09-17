# 考勤组管理自动化

doc_id: 9xgadQlBCR
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/shift/add
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
- 传统模式下，HR在系统中规划好新的考勤规则后，需手动登录钉钉后台逐个创建考勤组、设置班次、添加成员。千人级企业通常有20-50个考勤组，手工操作耗时数小时且容易出现班次错误或人员遗漏。
- - **审计留痕**：每次API调用均记录操作人、时间戳、考勤组ID、员工userId等详细信息,满足企业合规审计与追溯要求。
- - **审计日志完整**：每次API调用均记录操作人、时间戳、变更内容，满足企业合规审计与追溯要求。
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

source_url: https://open.dingtalk.com/document/development/operation-related-to-attendance-group
updated_at: 2026-09-17 09:36:36
