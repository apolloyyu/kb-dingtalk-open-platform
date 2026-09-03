# 查询视频会议成员

doc_id: Gu3lyRg4cG
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/members
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议conferenceId，可通过创建视频会议接口获取conferenceId。

## Query params
- optional: nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: memberModels(Array), unionId(String), conferenceId(String), userNick(String), joinTime(Long), leaveTime(Long), duration(Long), host(Boolean), attendStatus(Integer), outerOrgMember(Boolean), pstnJoin(Boolean), coHost(Boolean), nextToken(String), totalCount(Integer)

## Limits
- 每页最大条目数，默认值128，无最大值限制。

source_url: https://open.dingtalk.com/document/development/querying-video-conference-members
updated_at: 2026-06-02 09:18:03
