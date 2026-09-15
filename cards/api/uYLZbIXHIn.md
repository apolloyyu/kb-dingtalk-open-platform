# 企业OA系统与钉钉通讯录双向同步

doc_id: uYLZbIXHIn
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
- 传统模式下，OA系统中规划好新的组织架构后，需手动在钉钉后台逐层创建部门和添加员工。千人级企业通常有50-100个部门、数百名员工，手工操作耗时数天且易出现层级错误。
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增。
- - **同步延迟：**从变更发生到同步完成的平均延迟（目标<5秒）。
- - **回调超时：**OA系统处理逻辑应在3秒内完成，否则钉钉会认为超时并重试。
- - ✅ 钉钉中变更后，OA系统在5秒内收到回调并更新。
- - ✅ OA系统中变更后，钉钉在10秒内完成同步。

source_url: https://open.dingtalk.com/document/development/synchronization-between-enterprise-oa-system-and-dingtalk-address-book
updated_at: 2026-09-15 09:36:12
