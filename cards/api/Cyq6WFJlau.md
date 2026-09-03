# 通知审批通过

doc_id: Cyq6WFJlau
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/approvals/finish
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过以下方式获取： - 企业内部应用可调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用可调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: userId(String)

## Body
- optional: topCalculateApproveDurationParam(Object), bizType(Long), fromTime(String), toTime(String), durationUnit(String), calculateModel(Long), leaveCode(String), tagName(String), subType(String), approveId(String), jumpUrl(String), overtimeDuration(String), overTimeToMore(Long)

## Returns
- optional: result(Object), duration(double), durationDetail(Array), date(String), success(Boolean)

## Limits
- 开始时间。开始时间不能早于当前时间前31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- 结束时间。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 - 结束时间不能早于开始时间； - 时间跨度不能超过360天； - 结束时间减去开始时间的天数不能超过31天； - `biz_type`为1时，结束时间减去开始时间的天数不能超过1天。
- 审批单类型名称，最大长度20个字符，支持类型：请假、出差、外出、加班。
- 子类型名称，最大长度64个字符。 审批单类型biz_type=3时，该参数必传。
- 审批单ID，最大长度100个字符，自定义值。 第三方企业应用需要自行保存，通知审批撤销时需要使用参数。approveId不变的情况下再次调用本接口是更新操作。
- 审批单跳转地址，最大长度200个字符。 第三方企业应用在考勤统计页面点击会根据该地址进行跳转，可传对应的审批单详情地址。

source_url: https://open.dingtalk.com/document/development/api-processapprovefinish
updated_at: 2026-06-02 09:24:51
