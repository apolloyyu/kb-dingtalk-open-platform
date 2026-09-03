# 通知审批通过

doc_id: Vd5m7BSpe4
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/attendance/approve/finish
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- userid (String, required): 员工的userId。
- biz_type (Number, required): 审批单类型： - **1**：加班 - **2**：出差、外出 - **3**：请假
- from_time (String, required): 开始时间。开始时间不能早于当前时间前31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- to_time (String, required): 结束时间。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 **[!NOTE]** - 结束时间减去开始时间的天数不能超过31天。 - biz_type为1时，结束时间减去开始时间的天数不能超过1天。
- duration_unit (String, required): 时长单位，支持格式如下： - day - halfDay - hour：biz_type为1时仅支持hour。 时间格式必须与时长单位对应： - 2019-08-15对应day - 2019-08-15 AM对应halfDay - 2019-08-15 12:43对应hour
- calculate_model (Number, required): 计算方法： - **0**：按自然日计算 - **1**：按工作日计算
- tag_name (String, required): 审批单类型名称，最大长度20个字符。 支持类型如下： - 请假 - 出差 - 外出 - 加班
- approve_id (String, required): 审批单ID，最大长度100个字符，自定义值。
- jump_url (String, required): 审批单跳转地址，最大长度200个字符。
- optional: sub_type(String), overtime_duration(String), overtime_to_more(Number)

## Returns
- optional: errcode(Number), errmsg(String), result(TopDurationVo), duration(String), durationDetail(TopDayDurationVo[]), date(String)

## Limits
- 开始时间。开始时间不能早于当前时间前31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- 结束时间。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 **[!NOTE]** - 结束时间减去开始时间的天数不能超过31天。 - biz_type为1时，结束时间减去开始时间的天数不能超过1天。
- 审批单类型名称，最大长度20个字符。 支持类型如下： - 请假 - 出差 - 外出 - 加班
- 子类型名称，最大长度20个字符。 **[!NOTE]** 审批单类型biz_type=3时，该参数必传。
- 审批单ID，最大长度100个字符，自定义值。
- 审批单跳转地址，最大长度200个字符。

source_url: https://open.dingtalk.com/document/development/notice-of-approval
updated_at: 2026-08-25 09:38:01
