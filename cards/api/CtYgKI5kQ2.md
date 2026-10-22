# 自定义对象管理：个性化业务数据全生命周期管理

doc_id: CtYgKI5kQ2
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectmeta/describe
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
- - **高效批量操作**：单次最多获取200条记录，配合分页游标可完整拉取历史数据。
- - **批量数据高效获取**：单次接口最多返回200条记录，配合分页游标可完整拉取历史项目台账。
- - 管理层无法实时掌握设备分布与使用状态，只能在年度盘点时才发现账实不符。
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

source_url: https://open.dingtalk.com/document/development/crm-custom-object-data-operation-process
updated_at: 2026-10-22 17:12:15
