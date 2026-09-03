# 全员静音或全员取消静音

doc_id: 566cBBu1OD
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/allMembers/mute
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议id，可调用创建视频会议接口获取返回参数`conferenceId`字段。

## Query params
- none

## Body
- action (String, required): 操作类型： - **mute**：静音 - **un_mute**：取消静音
- optional: forceMute(Boolean)

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/mute-all-staff-or-unmute-all-staff
updated_at: 2026-06-02 12:08:27
