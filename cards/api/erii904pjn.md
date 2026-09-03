# 预计算时长

doc_id: erii904pjn
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
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
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- userid (String, required): 员工的userId。
- biz_type (Number, required): 审批单类型： - **1**：加班 - **2**：出差 - **3**：请假
- from_time (String, required): 开始时间。开始时间不能早于当前时间前31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- to_time (String, required): 结束时间。 - biz_type为1时，结束时间减去开始时间不能超过1天。 - biz_type为2或3时，结束时间减去开始时间的天数不能超过31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- duration_unit (String, required): 时长单位，支持格式如下： - day - halfDay - hour：biz_type为1时仅支持hour。 时间格式必须与时长单位对应： - 2019-08-15对应day - 2019-08-15 AM对应halfDay - 2019-08-15 12:43对应hour
- calculate_model (Number, required): 计算方法： - **0**：按自然日计算 - **1**：按工作日计算

## Returns
- optional: errcode(Number), errmsg(String), result(TopDurationVo), duration(String), duration_details(TopDayDurationVo[]), date(String)

## Limits
- 开始时间。开始时间不能早于当前时间前31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- 结束时间。 - biz_type为1时，结束时间减去开始时间不能超过1天。 - biz_type为2或3时，结束时间减去开始时间的天数不能超过31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43

source_url: https://open.dingtalk.com/document/development/calculate-duration-based-on-attendance-scheduling
updated_at: 2026-08-25 09:38:00
