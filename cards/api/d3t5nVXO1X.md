# 跟进记录管理：销售拜访数据自动归档与智能查询

doc_id: d3t5nVXO1X
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe
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
- - **批量高效获取**：单次最多获取200条跟进记录，大幅降低接口调用次数与等待时间。
- 某制造企业销售团队每月产生超过500条客户拜访记录，目前依赖Excel手工汇总，存在以下问题：
- - **批量数据高效获取**：单次接口最多返回200条记录，配合分页游标可完整拉取历史数据。
- - 客服主管无法实时掌握团队跟进进度，只能在月度复盘时才发现积压工单。
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - `page_size`：分页大小，单次最多200条。

source_url: https://open.dingtalk.com/document/development/crm-follow-up-record-data-operation-process
updated_at: 2026-10-22 17:12:13
