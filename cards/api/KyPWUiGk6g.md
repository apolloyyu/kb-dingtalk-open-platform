# 企业大屏展示员工考勤

doc_id: KyPWUiGk6g
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/detail/batchquery
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
- 传统模式下，车间主任需每2小时人工统计一次各产线在岗人数，耗时30分钟且数据滞后。当发生突发缺勤时，无法及时调整生产计划，导致产能损失。
- - **秒级更新**：员工打卡后1秒内大屏数据刷新，管理层实时掌握人力分布。
- - **预测性调度**：基于历史数据预测未来2小时人力需求，提前调整排班。
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。
- - **轮询拉取**：企业服务器定时调用API查询打卡记录，存在延迟（通常5-15分钟），且频繁调用易触发限流。
- - **Stream推送**：钉钉在员工打卡后主动推送至企业指定URL，延迟<1秒，无需主动查询，适合实时大屏场景。
- - **迟到**：员工有打卡记录，但打卡时间晚于排班规定的上班时间+迟到阈值（通常10-30分钟，可在考勤组配置中设置）。

source_url: https://open.dingtalk.com/document/development/the-enterprise-big-screen-displays-the-attendance-of-employees
updated_at: 2026-09-20 09:32:32
