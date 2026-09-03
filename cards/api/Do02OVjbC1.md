# 开启视频会议云录制

doc_id: Do02OVjbC1
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/cloudRecords/start
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议ID，可调用创建视频会议接口获取conferenceId参数值。

## Query params
- none

## Body
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取unionid参数值。 **[!NOTE]** 只有当用户是会议主持人时，才有权限开启云录制。
- optional: smallWindowPosition(String), mode(String)

## Returns
- optional: code(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/video-conference-open-cloud-recording
updated_at: 2026-06-02 09:10:50
