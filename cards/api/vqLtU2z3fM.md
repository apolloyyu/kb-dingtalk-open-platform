# 查询会议录制的详情信息

doc_id: vqLtU2z3fM
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/cloudRecords/getVideos
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议ID，可调用创建视频会议接口获取conferenceId参数值。

## Query params
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取unionid参数值。

## Body
- none

## Returns
- optional: videoList(Array), recordId(String), unionId(String), startTime(Long), recordType(Long), duration(Long), fileSize(Long), endTime(Long), mediaId(String), regionId(String)

## Limits
- 录制持续时长的1000倍。 例如，该字段值为20000，表示本次会议录制的时长为20秒。

source_url: https://open.dingtalk.com/document/development/query-recording-information
updated_at: 2026-06-02 09:10:47
