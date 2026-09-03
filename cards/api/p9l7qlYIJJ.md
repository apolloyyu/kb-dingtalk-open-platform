# 查询企业进行中会议列表

doc_id: p9l7qlYIJJ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/orgConferences
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: nextToken(String), totalCount(Integer), hasMore(Boolean), onGoingConfList(Array), conferenceId(String), title(String), roomCode(String), status(Integer), startTime(Long), endTime(Long), creatorId(String), creatorNick(String), bizType(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-queryorgconferencelist
updated_at: 2026-06-02 12:04:35
