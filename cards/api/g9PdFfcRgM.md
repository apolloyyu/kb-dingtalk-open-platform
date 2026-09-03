# 删除会议室

doc_id: g9PdFfcRgM
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/rooms/meetingRooms/{roomId}
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- roomId (String, required): 会议室ID，可调用查询会议室列表接口获取。

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取获取。

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-a-meeting-room
updated_at: 2026-06-03 10:12:06
