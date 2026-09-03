# 创建日程

doc_id: RXmKYv9nS7
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取企业accessToken(应用商店应用)接口获取。 - 第三方个人应用，调用获取用户token接口获取。
- optional: x-client-token(String)

## Path params
- userId (String, required): 日程组织者的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，统一为**primary**，表示用户的主日历。

## Query params
- none

## Body
- summary (String, required): 日程标题，最大不超过2048个字符。
- start (Object, required): 日程开始时间。
- optional: description(String), date(String), dateTime(String), timeZone(String), end(Object), isAllDay(Boolean), recurrence(Object), pattern(Object), type(String), dayOfMonth(Integer), daysOfWeek(String), index(String), interval(Integer), firstDayOfWeek(String), range(Object), endDate(String), numberOfOccurrences(Integer), attendees(Array), id(String), isOptional(Boolean), location(Object), displayName(String), reminders(Array), method(String), minutes(Integer), onlineMeetingInfo(Object), extra(Map<String, String>), uiConfigs(Array), uiName(String), uiStatus(String), richTextDescription(Object), text(String)

## Returns
- optional: id(String), summary(String), description(String), start(Object), date(String), dateTime(String), timeZone(String), end(Object), isAllDay(Boolean), recurrence(Object), pattern(Object), type(String), dayOfMonth(Integer), daysOfWeek(String), index(String), interval(Integer), firstDayOfWeek(String), range(Object), endDate(String), numberOfOccurrences(Integer), attendees(Array), displayName(String), responseStatus(String), self(Boolean), isOptional(Boolean), organizer(Object), location(Object), reminders(Array), method(String), minutes(String), createTime(String), updateTime(String), onlineMeetingInfo(Object), conferenceId(String), url(String), extraInfo(Map), uiConfigs(Array), uiName(String), uiStatus(String), richTextDescription(Object), text(String)

## Limits
- 幂等校验。 - 相同的`x-client-token`表示同一次请求。 - 过期失效，1天。
- 日程标题，最大不超过2048个字符。
- 日程描述，最大不超过5000个字符。
- 日程参与人列表，最多支持500个参与人。
- 日程提醒，可以添加多个。 - 如果不传默认提醒时间为：开始前15分钟提醒。 - 如果传空数据表示不创建任何提醒。
- - 每次日程参与者操作最大支持500人，最大支持操作5000人的日程。

source_url: https://open.dingtalk.com/document/development/create-schedule
updated_at: 2026-06-02 09:24:57
