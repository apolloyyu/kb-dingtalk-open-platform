# 查询日程列表

doc_id: 6CtAUmz22W
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 查询目标用户的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历id，统一为primary，表示用户的主日历。

## Query params
- optional: timeMin(String), timeMax(String), showDeleted(Boolean), maxResults(Integer), maxAttendees(Integer), nextToken(String), syncToken(String), seriesMasterId(String)

## Body
- none

## Returns
- optional: nextToken(String), events(Array), id(String), summary(String), description(String), start(Object), date(String), dateTime(String), timeZone(String), originStart(Object), end(Object), isAllDay(Boolean), recurrence(Object), pattern(Object), type(String), dayOfMonth(Integer), daysOfWeek(String), index(String), interval(Integer), firstDayOfWeek(String), range(Object), endDate(String), numberOfOccurrences(Integer), attendees(Array), displayName(String), responseStatus(String), self(Boolean), isOptional(Boolean), organizer(Object), location(Object), meetingRooms(Array of String), seriesMasterId(String), createTime(String), updateTime(String), status(String), onlineMeetingInfo(Object), conferenceId(String), url(String), extraInfo(Map), reminders(Array), method(String), minutes(String), extendedProperties(Object), sharedProperties(Object), sourceOpenCid(String), belongCorpId(String), roomId(String), categories(Array), richTextDescription(Object), text(String), syncToken(String)

## Limits
- 日程开始时间的最小值，格式为ISO-8601的date-time格式，可不填。 `timeMin`和 `timeMax`最大差值为一年。
- 日程开始时间的最大值，格式为ISO-8601的date-time格式，可不填。 `timeMin`和 `timeMax`最大差值为一年。
- 最大返回记录数，最大值100，默认值100。
- 每个日程的参与者查询个数，默认100，最大100。 如果参会人数超过100人，需要拉取全部参会人请使用获取日程参与者接口获取。

source_url: https://open.dingtalk.com/document/development/query-an-event-list
updated_at: 2026-06-02 09:25:01
