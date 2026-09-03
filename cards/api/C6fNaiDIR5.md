# 更新会议室信息

doc_id: C6fNaiDIR5
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/rooms/meetingRooms
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取。
- roomId (String, required): 会议室ID，可调用查询会议室列表接口获取。
- optional: roomName(String), roomCapacity(Integer), roomPicture(String), roomStatus(Integer), roomLocation(Object), title(String), desc(String), roomLabelIds(Array of Long), isvRoomId(String), groupId(Long), reservationAuthority(Object), authorizedMembers(Array), memberId(String), memberType(String), memberName(String), enableCycleReservation(Boolean), openReservation(Boolean), roomDescription(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-meeting-room-information
updated_at: 2026-06-03 10:12:07
