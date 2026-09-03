# 查询用户进行中会议列表

doc_id: VZDoUqoA3d
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/conference/users/lists
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 要查询的用户unionId，可调用查询用户详情接口获取。

## Body
- none

## Returns
- optional: onGoingConfIdList(Array of String), memberModelMap(Map<String, Object>), unionId(String), conferenceId(String), userNick(String), joinTime(Long), leaveTime(Long), duration(Long), attendStatus(Integer), host(Boolean), coHost(Boolean), outerOrgMember(Boolean), pstnJoin(Boolean), deviceType(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-queryuserongoingconference
updated_at: 2026-06-02 12:02:37
