# 查询会议录制中的视频信息

doc_id: GncjrOmAat
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/cloudRecords/videos/getPlayInfos
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议ID，可调用创建视频会议接口获取conferenceId参数值。

## Query params
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取unionid参数值。
- mediaId (String, required): 媒体文件ID，可调用查询会议录制的详情信息接口获取mediaId参数值。
- regionId (String, required): 地域ID，可调用查询会议录制的详情信息接口获取regionId参数值。

## Body
- none

## Returns
- optional: playUrl(String), mp4FileUrl(String), fileSize(Long), duration(Long), status(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-playback-information-about-a-recorded-cloud-video
updated_at: 2026-06-02 09:10:46
