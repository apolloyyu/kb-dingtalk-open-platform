# 企业自有假勤审批同步到钉钉

doc_id: qieVTeeppo
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/approve/cancel
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
- - **时长计算复杂**：不同日期的排班时长不同（如工作日8小时、周末4小时），人工计算可请假时长容易出错，且无法动态适配排班调整。
- - **轻量级接入**：无需改造业务系统前端，仅需调用3个核心API即可完成集成，开发成本低。
- - **排班时长预计算**：根据员工排班情况，智能计算可提交的请假时长上限，避免超期申请或资源浪费。
- 同时，不同日期的排班时长不同（如工作日8小时、周末4小时），HR需人工计算每个员工的可请假时长，耗时且容易出错。审批通过后，钉钉考勤无法自动感知，需人工干预同步，进一步增加了管理成本。
- - **智能时长预计算**：根据排班自动计算最大可请假时长，避免超期申请，减少HR审核工作量。
- - **低成本接入**：仅需调用3个核心API，开发周期缩短70%，快速上线。
- 员工请假跨越多个工作日，且每日排班时长不同（如小明10月15日排班8小时，10月16日排班4小时）。传统方式需人工累加各天排班时长，容易出错且效率低。当员工请假时间跨度较大（如一周）时，HR需逐一查询每天的排班规则，耗时且容易遗漏。
- - **自动累加排班**：调用预计算接口，自动返回跨天请假的最大可提交时长，消除人工计算错误。

source_url: https://open.dingtalk.com/document/development/enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays
updated_at: 2026-09-21 11:23:53
