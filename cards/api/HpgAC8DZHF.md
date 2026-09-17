# 考勤组成员管理自动化

doc_id: HpgAC8DZHF
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/users/add
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
- 企业日常运营中，员工入职、离职、调岗、部门调整等组织变动频繁发生。每次变动都需要HR或管理员手动在钉钉后台逐一调整考勤组成员名单：新增员工加入考勤组、离职员工移除、调岗员工切换考勤组。对于千人级企业，每月可能有数十至上百人次的组织变动，手工操作不仅耗时耗力，还容易出现遗漏或错误，导致员工打卡异常、考勤数据不准确等问题。
- 传统模式下，HR在新员工入职当天需手动登录钉钉后台，查找对应部门的考勤组，逐个添加新员工到考勤组。若企业每日有5-10人入职，HR需重复操作多次，且容易遗漏或选错考勤组，导致新员工无法正常打卡。
- - **审计留痕**：每次操作记录操作人、时间戳、考勤组ID，满足合规要求。
- - **审计日志完整**：每次移除操作均记录详细信息，满足合规审计与追溯要求。
- - **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- - **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

source_url: https://open.dingtalk.com/document/development/attendance-group-member-operations
updated_at: 2026-09-17 09:36:38
