# 查询单个日程详情

doc_id: OV2eKcPPgz
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 日程所属用户的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历Id，统一为primary，表示用户的主日历。
- eventId (String, required): 日程ID，可调用查询日程列表接口获取id参数值。

## Query params
- optional: maxAttendees(Long)

## Body
- none

## Returns
- optional: id(String), summary(String), description(String), status(String), start(Object), date(String), dateTime(String), timeZone(String), originStart(Object), end(Object), isAllDay(Boolean), recurrence(Object), pattern(Object), type(String), dayOfMonth(Integer), daysOfWeek(String), index(String), interval(Integer), firstDayOfWeek(String), range(Object), endDate(String), numberOfOccurrences(Integer), attendees(Array), displayName(String), responseStatus(String), self(Boolean), isOptional(Boolean), organizer(Object), location(Object), seriesMasterId(String), createTime(String), updateTime(String), reminders(Array), method(String), minutes(String), onlineMeetingInfo(Object), conferenceId(String), url(String), extraInfo(Map), extendedProperties(Object), sharedProperties(Object), sourceOpenCid(String), belongCorpId(String), meetingRooms(Array), roomId(String), categories(Array), richTextDescription(Object), text(String)

## Limits
- 最大参与人数，默认值100，最大值500。

source_url: https://open.dingtalk.com/document/development/query-details-about-an-event
updated_at: 2026-06-02 09:25:00
