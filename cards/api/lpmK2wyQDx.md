# 查询预约会议历史会议信息

doc_id: lpmK2wyQDx
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/scheduleConferences/{scheduleConferenceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证： - 企业内部应用可调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用可调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- scheduleConferenceId (String, required): 预约会议id，可通过创建预约会议接口获取返回参数`scheduleConferenceId`字段。

## Query params
- optional: nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: totalCount(Integer), nextToken(String), conferenceList(Array), conferenceId(String), title(String), roomCode(String), status(Integer), startTime(Long), endTime(Long)

## Limits
- 本次读取的最大数据记录数量。

source_url: https://open.dingtalk.com/document/development/query-appointment-meeting-history-meeting-information
updated_at: 2026-06-02 12:08:32
