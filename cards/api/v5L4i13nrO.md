# 获取日程参与者

doc_id: v5L4i13nrO
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/attendees
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 本次请求的资源所归属的用户unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历id，统一为**primary**，表示用户的主日历。
- eventId (String, required): 日程ID，可调用查询日程列表接口获取id参数值。

## Query params
- optional: maxResults(Integer), nextToken(String)

## Body
- none

## Returns
- optional: nextToken(String), attendees(Array), id(String), displayName(String), responseStatus(String), self(Boolean), isOptional(Boolean)

## Limits
- 最大返回记录数，默认值100，最大值500。

source_url: https://open.dingtalk.com/document/development/get-the-participants-of-a-schedule
updated_at: 2026-06-02 09:25:05
