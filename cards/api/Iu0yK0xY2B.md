# 针对单个日程进行签到

doc_id: Iu0yK0xY2B
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/signin
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 本次请求的资源所归属的用户unionId。 - 企业内部应用和第三方企业应用通过查询用户详情接口获取unionid参数值。 - 第三方个人应用通过获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，统一为**primary**，表示用户的主日历。
- eventId (String, required): 日程ID，可通过查询日程列表接口获取id参数值。

## Query params
- none

## Body
- none

## Returns
- optional: checkInTime(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/sign-in-single-schedule-news
updated_at: 2026-06-01 18:18:49
