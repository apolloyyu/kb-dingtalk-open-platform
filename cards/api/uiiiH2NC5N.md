# 更新预约会议

doc_id: uiiiH2NC5N
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/conference/scheduleConferences
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
- creatorUnionId (String, required): 预约会议创建者unionId。
- scheduleConferenceId (String, required): 预约会议id，可通过创建预约会议接口获取返回参数`scheduleConferenceId`字段。
- title (String, required): 预约会议标题。标题最大长度限制不允许超过50。
- startTime (Long, required): 预约会议开始时间，毫秒级UTC时间戳。
- endTime (Long, required): 预约会议结束时间，毫秒级UTC时间戳。

## Returns
- optional: success(Boolean)

## Limits
- 预约会议标题。标题最大长度限制不允许超过50。

source_url: https://open.dingtalk.com/document/development/update-appointment-meeting
updated_at: 2026-06-02 12:08:29
