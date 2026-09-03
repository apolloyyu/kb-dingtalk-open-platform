# 查询排班打卡结果

doc_id: EQlywHegFv
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/schedule/result/listbyids
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- op_user_id (String, required): 操作人userId。
- schedule_ids (String, required): 排班ID，通过查询企业考勤排班详情接口获取plan_id参数值。多个排班ID之间用逗号分割，每次调用最多支持100个排班ID，

## Returns
- optional: result(TopScheduleResultVo[]), check_type(String), gmt_modified(Date), plan_check_time(Date), corp_id(String), base_check_time(Date), group_id(Number), gmt_create(Date), user_id(String), work_date(Date), id(Number), location_result(String), is_legal(String), time_result(String), record_id(Number), user_check_time(Date), schedule_id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 排班ID，通过查询企业考勤排班详情接口获取plan_id参数值。多个排班ID之间用逗号分割，每次调用最多支持100个排班ID，

source_url: https://open.dingtalk.com/document/development/query-the-results-of-a-batch-of-tasks
updated_at: 2026-05-27 17:06:11
