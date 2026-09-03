# 添加日程参与者

doc_id: 8brpIk1ZkD
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/attendees
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。
- optional: x-client-token(String)

## Path params
- userId (String, required): 日程创建者的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历id，统一为primary，表示用户的主日历。
- eventId (String, required): 日程ID，可调用查询日程列表接口获取id参数值。

## Query params
- none

## Body
- attendeesToAdd (Array, required): 需要添加的参与人列表。
- optional: id(String), isOptional(Boolean), pushNotification(Boolean), chatNotification(Boolean)

## Returns
- none

## Limits
- 幂等校验。 - 相同的`x-client-token`表示同一次请求。 - 过期失效，1天。
- 每次日程参与者操作最大支持500人，最大支持操作5000人的日程。

source_url: https://open.dingtalk.com/document/development/add-schedule-participant
updated_at: 2026-06-02 09:25:03
