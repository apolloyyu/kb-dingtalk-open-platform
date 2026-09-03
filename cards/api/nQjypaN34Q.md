# 查询视频会议信息

doc_id: nQjypaN34Q
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议conferenceId，可调用创建视频会议接口获取conferenceId。

## Query params
- none

## Body
- none

## Returns
- optional: confInfo(Object), activeNum(Integer), attendNum(Integer), confDuration(Long), conferenceId(String), creatorId(String), creatorNick(String), externalLinkUrl(String), invitedNum(Integer), startTime(Long), status(Integer), title(String), roomCode(String), endTime(Long), scheduleConferenceId(String), bizType(String), cloudRecordStatus(Integer), cloudRecordOwnerUnionId(String), minutesStatus(Integer), minutesOwnerUnionId(String), extensionAppSettings(Array), appId(String), appCode(String), autoOpenMode(Integer), extensionAppBizData(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/querying-video-conference-information
updated_at: 2026-06-03 10:12:04
