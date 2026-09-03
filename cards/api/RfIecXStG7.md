# 停止视频会议直播推流

doc_id: RfIecXStG7
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/streamOuts/stop
api_version: v2-new
app_types: 第三方个人应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证： - 企业内部应用可调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用可调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用可调用获取第三方个人应用的access_token接口获取。

## Path params
- conferenceId (String, required): 会议id，可调用创建视频会议接口获取返回参数`conferenceId`字段。

## Query params
- none

## Body
- streamId (String, required): 推流id，可调用开启视频会议直播推流接口获取返回参数`successStreamMap`字段。
- stopAllStream (Boolean, required): 是否停止所有流。 **[!NOTE]** 为true时**streamId**参数无效。
- unionId (String, required): 用户unionId。

## Returns
- optional: code(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/videoconferencing-stops-live-stream-ingest
updated_at: 2026-06-02 12:08:26
