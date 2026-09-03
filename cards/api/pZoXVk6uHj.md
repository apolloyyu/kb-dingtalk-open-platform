# 批量获取加班规则设置

doc_id: pZoXVk6uHj
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/overtimeSettings/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: overtimeSettingIds(Array of Long)

## Returns
- optional: result(Array), settingId(Long), name(String), default(Boolean), durationSettings(Map<String, Object>), calcType(Integer), durationType(Integer), overtimeRedress(Boolean), settings(Map), overtimeRedressBy(String), vacationRate(Float), skipTime(String), skipTimeByFrames(Array), startTime(String), endTime(String), valid(Boolean), skipTimeByDurations(Array), duration(Long), minus(Long), holidayPlanOvertimeRedress(Boolean), holidayPlanOvertimeRedressBy(String), holidayPlanVacationRate(Float), warningSettings(Array), time(String), threshold(Long), action(String), stepType(Integer), stepValue(Float), workMinutesPerDay(Integer), overtimeDivisions(Array), previousDayType(String), nextDayType(String), timeSplitPoint(String), id(Long)

## Limits
- 取值为**风险预警**或**最大加班时间**。

source_url: https://open.dingtalk.com/document/development/batch-retrieve-overtime-rules
updated_at: 2026-06-01 16:47:21
