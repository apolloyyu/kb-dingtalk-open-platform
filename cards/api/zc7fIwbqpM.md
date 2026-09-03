# 查询会议室详情

doc_id: zc7fIwbqpM
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/rooms/meetingRooms/{roomId}
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： 企业内部应用，调用获取企业内部应用的accessToken接口获取。 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- roomId (String, required): 会议室ID，可调用查询会议室列表接口获取。

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取获取。

## Body
- none

## Returns
- optional: result(Object), roomId(String), roomStaffId(String), corpId(String), roomName(String), roomStatus(Integer), roomLabels(Array), labelId(Long), labelName(String), roomCapacity(Integer), roomLocation(Object), title(String), desc(String), roomPicture(String), isvRoomId(String), roomGroup(Object), groupId(Long), groupName(String), parentId(Long), deviceUnionIds(Array of String), reservationAuthority(Object), authorizedMembers(Array), memberId(String), memberType(String), memberName(String), enableCycleReservation(Boolean), roomUnionId(String), extensionConfig(Object), openReservation(Boolean), maxReservationTimeInterval(Integer), minReservationTimeInterval(Integer), advanceReservation(Object), advanceReservationTime(Integer), advanceReservationTimeUnit(String), advanceBookTimeFormat(String), reservationCloseDetail(Object), taskStartTime(Long), taskEndTime(Long), closeReason(String), contactUnionId(String), contactNick(String), sendNotify(Boolean), approvalSwitch(Boolean), approvalType(Integer), roomDescription(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/check-meeting-room-details
updated_at: 2026-06-03 10:12:08
