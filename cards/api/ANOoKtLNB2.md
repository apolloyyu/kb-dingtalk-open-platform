# 企业自有系统考勤打卡信息同步到钉钉

doc_id: ANOoKtLNB2
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/v2/user/list
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
- - **低成本快速接入**：仅需调用2个核心API即可完成对接，开发成本低。
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

source_url: https://open.dingtalk.com/document/development/attendance-synchronizes-information
updated_at: 2026-09-21 11:23:55
