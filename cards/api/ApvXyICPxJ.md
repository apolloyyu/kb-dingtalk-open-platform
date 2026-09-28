# 签到数据自动采集：从钉钉签到到业务系统实时同步

doc_id: ApvXyICPxJ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/checkin/record/get
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
- - **签到数据自动回写**：销售人员完成签到后1分钟内自动同步至CRM系统，无需手动录入拜访记录。
- - **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - `userid_list`：**重点参数**，需要查询的用户列表，最大列表长度为10。
- **注意**：如果是取1个人的数据，时间范围最大10天，如果是取多个人的数据，时间范围最大1天
- - `size`：分页查询的每页大小，最大100。
- - `userid_list`：需要查询的用户列表，最多10个用户ID。
- - `start_time` / `end_time`：查询的时间范围（Unix时间戳，毫秒）。单人查询最多10天，多人查询最多1天。

source_url: https://open.dingtalk.com/document/development/obtain-check-in-information
updated_at: 2026-09-23 12:04:38
