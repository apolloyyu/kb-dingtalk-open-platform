# 根据会议号查询会议信息

doc_id: CqizOT6d6d
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/roomCodes/{roomCode}/infos
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- roomCode (String, required): 会议码。

## Query params
- optional: nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: nextToken(String), hasMore(Boolean), totalCount(Integer), conferenceList(Array), conferenceId(String), title(String), roomCode(String), externalLinkUrl(String), status(Integer), startTime(Long), endTime(Long), confDuration(Long), creatorId(String), creatorNick(String), scheduleConferenceId(String), bizType(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-queryconferenceinfobyroomcode
updated_at: 2026-06-02 12:05:02
