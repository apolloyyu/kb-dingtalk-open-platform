# 企业自有假勤审批同步到钉钉

doc_id: qieVTeeppo
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: false
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/approve/duration/calculate
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
- > 例如，小明在10月15日的排班是8小时，10月16日的排班是4小时，如果正常上班，小明在10月15日、16日这2天的工作时间是12小时。
- > - 情况一，选择请假开始时间是10月15日，结束时间是10月15日；调用预计算时长接口，获取的可提交请假时长最大是8小时。
- > - 情况二，选择请假开始时间是10月15日，结束时间是10月16日，调用预计算时长接口，获取的可提交请假时长最大是12小时。

source_url: https://open.dingtalk.com/document/development/enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays
updated_at: 2026-07-02 10:36:13
