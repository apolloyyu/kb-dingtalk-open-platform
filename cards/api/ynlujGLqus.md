# 取消预定会议室

doc_id: ynlujGLqus
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/meetingRooms/batchRemove
api_version: v2-new
app_types: 第三方企业应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 日程组织者的unionId，可调用查询用户详情接口获取。
- calendarId (String, required): 日程所属的日历ID，统一为**primary**，表示用户的主日历。
- eventId (String, required): 日程ID，可调用查询日程列表接口获取id参数值。

## Query params
- none

## Body
- optional: meetingRoomsToRemove(Array), roomId(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/remove-a-meeting-room
updated_at: 2026-06-02 09:18:07
