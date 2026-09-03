# 创建会议室

doc_id: K7HCgNrGh3
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/rooms/meetingrooms
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
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取
- roomName (String, required): 会议室名称。
- roomStatus (Integer, required): 会议室状态。 - **0**：全员可用 - **1**：仅管理员可用 - **2**：部分有权限
- isvRoomId (String, required): 调用方外部会议室ID，调用方可传入自有系统内的会议室ID。 若调用方不与外部会议室关联，可传入本企业的实体会议室编号。
- optional: roomCapacity(Integer), roomPicture(String), roomLocation(Object), title(String), desc(String), roomLabelIds(Array of Long), groupId(Long), reservationAuthority(Object), authorizedMembers(Array), memberId(String), memberType(String), memberName(String), enableCycleReservation(Boolean), openReservation(Boolean), roomDescription(String)

## Returns
- optional: result(String)

## Limits
- 会议室可容纳人数，目前无最大值限制。

source_url: https://open.dingtalk.com/document/development/create-a-meeting-room
updated_at: 2026-06-03 10:12:05
