# 企业通讯录部门管理自动化

doc_id: Rqv5HvWlb3
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/v2/department/create
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
- 传统模式下，HR在系统中规划好新的组织架构后，需手动登录钉钉后台逐个创建部门并设置层级关系。千人级企业通常有50-100个部门，手工操作耗时数小时且易出现层级错误。
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - **批量处理效率**：百部门级批量导入应在5分钟内完成，否则检查网络或分批策略。

source_url: https://open.dingtalk.com/document/development/operations-related-to-address-book-departments
updated_at: 2026-09-15 09:36:15
