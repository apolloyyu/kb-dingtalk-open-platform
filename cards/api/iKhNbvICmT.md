# 获取视频会议详情

doc_id: iKhNbvICmT
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/data/conferences/{conferenceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议ID。

## Query params
- none

## Body
- none

## Returns
- optional: conferenceId(String), title(String), confStartTime(Float), duration(Float), totalNum(Long), attendeeNum(Long), attendeePercentage(String), callerId(String), callerName(String), memberList(Array), unionId(String), name(String), attendDuration(Float), staffId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-video-meeting-details
updated_at: 2026-06-04 19:10:03
