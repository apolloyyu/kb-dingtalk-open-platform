# 预计算时长

doc_id: aK9WEUzrWH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/approvals/durations/calculate
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: userId(String)

## Body
- optional: bizType(Long), fromTime(String), toTime(String), durationUnit(String), calculateModel(Long), leaveCode(String)

## Returns
- optional: result(Object), duration(double), durationDetail(Array), date(String), success(Boolean)

## Limits
- 开始时间。开始时间不能早于当前时间前31天。支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- 结束时间。 - biz_type为1时，结束时间减去开始时间不能超过1天。 - biz_type为2或3时，结束时间减去开始时间的天数不能超过31天。 支持以下格式： - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43
- > 例如，企业某员工11月2日排班（上班时间09:00，下班时间18:00），11月3日未排班。默认班次为（8:30-17:30）该员工计划需要请假，请假开始时间是11月02日的09:00:00，结束是11月3日的18:00:00，那么调用本接口可获取这个请假时长范围内，该员工预计请假的时长2天。

source_url: https://open.dingtalk.com/document/development/api-calculateduration
updated_at: 2026-06-01 16:53:34
