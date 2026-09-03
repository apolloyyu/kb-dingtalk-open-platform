# 获取签退链接

doc_id: 15GNjLUa2e
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/signOutLinks
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- calendarId (String, required): 日程所属的日历Id，统一为primary，表示用户的主日历。
- optional: userId(String), eventId(String)

## Query params
- none

## Body
- none

## Returns
- optional: signOutLink(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getsignoutlink
updated_at: 2026-06-01 18:18:51
