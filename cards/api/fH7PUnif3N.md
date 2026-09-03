# 获取签到链接

doc_id: fH7PUnif3N
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{unionId}/calendars/{calendarId}/events/{eventId}/signInLinks
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- calendarId (String, required): 日程所属的日历ID，统一为**primary**，表示用户的主日历。
- optional: userId(String), eventId(String)

## Query params
- none

## Body
- none

## Returns
- optional: signInLink(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getsigninlink
updated_at: 2026-06-01 18:18:51
