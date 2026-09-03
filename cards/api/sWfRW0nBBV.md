# 获取会议室忙闲信息

doc_id: sWfRW0nBBV
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/meetingRooms/schedules/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Calendar.Event.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- userId (String, required): 本次请求的资源所归属的用户unionId，可调用查询用户详情接口获取。

## Query params
- none

## Body
- roomIds (Array of String, required): 待查询的会议室roomId列表，可调用查询会议室列表接口获取，建议不超过5个。
- startTime (String, required): 查询开始时间，iso8601格式，例如：2022-07-29T14:55Z。
- endTime (String, required): 查询结束时间，iso8601格式，例如：2022-07-29T14:55Z。

## Returns
- optional: scheduleInformation(Array), roomId(String), error(String), scheduleItems(Array), status(String), eventId(String), organizer(Object), id(String), start(Object), dateTime(String), timeZone(String), end(Object)

## Limits
- 待查询的会议室roomId列表，可调用查询会议室列表接口获取，建议不超过5个。

source_url: https://open.dingtalk.com/document/development/queries-free-and-busy-meeting-room-information
updated_at: 2026-06-01 18:18:26
