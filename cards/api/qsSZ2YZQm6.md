# 取消预约会议

doc_id: qsSZ2YZQm6
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/scheduleConferences/cancel
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
- scheduleConferenceId (String, required): 预约会议id，可通过创建预约会议接口获取返回参数`scheduleConferenceId`字段。
- creatorUnionId (String, required): 预约会议创建者unionId。

## Returns
- optional: success(Boolean)

## Limits
- - 该接口只能取消通过创建预约会议接口创建的预约会议。

source_url: https://open.dingtalk.com/document/development/cancel-appointment-meeting
updated_at: 2026-07-30 09:57:45
