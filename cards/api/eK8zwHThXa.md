# 查询预约会议

doc_id: eK8zwHThXa
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/scheduleConferences/{scheduleConferenceId}/infos
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- scheduleConferenceId (String, required): 预约会议id，可通过创建预约会议接口获取返回参数`scheduleConferenceId`字段。

## Query params
- requestUnionId (String, required): 请求者unionId。

## Body
- none

## Returns
- optional: requestId(String), scheduleConferenceId(String), title(String), startTime(Long), endTime(Long), roomCode(String), url(String), phones(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-meeting-reservation
updated_at: 2026-06-02 12:08:30
