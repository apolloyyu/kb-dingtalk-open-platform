# 修改日程

doc_id: 68Mxcrdh14
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。
- optional: x-client-token(String)

## Path params
- userId (String, required): 日程组织者的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，统一为primary，表示用户的主日历。
- eventId (String, required): 日程ID，可调用查询日程列表接口获取id参数值。

## Query params
- none

## Body
- id (String, required): 日程ID。
- uiName (String, required): 组件名称，可取值（持续更新）： - **updateEventButton**：编辑日程按钮 - **deleteEventButton**：删除日程按钮 - **transferEventButton**：转让日程按钮 - **attendee**：参与人区域 - **comment**：日程评论区域
- uiStatus (String, required): 组件状态，可取值： - **hide**：隐藏 - **disable**: 禁用（新版详情页支持，低版本暂不支持disable，组件将被隐藏） 按钮类：无法点击。 区域类：无法交互。如将评论区域设置为disable，那么无法写评论，但是评论内容依然可见。 - **enable**：可使用（默认状态）
- optional: summary(String), description(String), start(Object), date(String), dateTime(String), timeZone(String), end(Object), isAllDay(Boolean), recurrence(Object), pattern(Object), type(String), dayOfMonth(Integer), daysOfWeek(String), index(String), interval(Integer), firstDayOfWeek(String), range(Object), endDate(String), numberOfOccurrences(Integer), attendees(Array), email(String), isOptional(Boolean), location(Object), displayName(String), extra(Map<String, String>), reminders(Array), method(String), minutes(Integer), onlineMeetingInfo(Object), richTextDescription(Object), text(String), uiConfigs(Array)

## Returns
- optional: id(String), summary(String), description(String), start(Object), date(String), dateTime(String), timeZone(String), end(Object), isAllDay(Boolean), recurrence(Object), pattern(Object), type(String), dayOfMonth(Integer), daysOfWeek(String), index(String), interval(Integer), firstDayOfWeek(String), range(Object), endDate(String), numberOfOccurrences(Integer), attendees(Array), displayName(String), responseStatus(String), self(Boolean), isOptional(Boolean), organizer(Object), location(Object), meetingRooms(Array of String), reminders(Array), method(String), minutes(String), createTime(String), updateTime(String), onlineMeetingInfo(Object), conferenceId(String), url(String), richTextDescription(Object), text(String), uiConfigs(Array), uiName(String), uiStatus(String)

## Limits
- 幂等校验。 - 相同的`x-client-token`表示同一次请求。 - 过期失效，1天。
- 日程提醒，可以添加多个。 - 如果不传默认提醒时间为： - **非全天日程**：开始前15分钟提醒 - **全天日程**：开始前一天9点提醒 - 如果传空数据表示不创建任何提醒。
- - 每次日程参与者操作最大支持500人，最大支持操作5000人的日程。

source_url: https://open.dingtalk.com/document/development/modify-event
updated_at: 2026-06-02 09:24:59
