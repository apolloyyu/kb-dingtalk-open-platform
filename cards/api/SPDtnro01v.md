# 计算请假时长

doc_id: SPDtnro01v
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 员工在企业内的userId，企业用来唯一标识用户的字段。
- from_date (Date, required): 请假开始时间。
- to_date (Date, required): 请假结束时间。

## Returns
- optional: result(ApproveDurationForTopVo), duration_in_minutes(Number), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/calculate-leave-duration
updated_at: 2026-05-27 17:06:24
