# 制造业订单交付管理：产供销全链路数据协同与实时追踪

doc_id: tfPnxoWIdU
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/user/listsimple
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
- 某中型装备制造企业拥有8条自动化产线，日均处理200+销售订单，过去依赖人工传递纸质单据协调生产与采购，原有流程存在以下问题：
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - `size`：分页长度，最大值100。
- 若**accessToken**过期，可重新调用获取`accessToken`接口并更新缓存。建议在缓存中设置7000秒过期时间（早于官方7200秒），提前刷新避免业务中断。
- 权限添加后需等待1-2分钟生效；若仍报错，请检查是否使用了正确的`accessToken`（旧令牌不会自动继承新权限），重新获取令牌后再试。

source_url: https://open.dingtalk.com/document/development/management-of-order-delivery-in-the-manufacturing-industry
updated_at: 2026-10-16 09:23:19
