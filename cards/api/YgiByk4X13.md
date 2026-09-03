# 批量查询视频会议信息

doc_id: YgiByk4X13
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/query
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- conferenceIdList (Array of String, required): 会议ID列表。

## Returns
- optional: infos(Array), conferenceId(String), title(String), startTime(Long), status(Long), mediaStatus(Long), userList(Array), userId(String), nick(String), attendStatus(Long), cameraStatus(Long), micStatus(Long), rejectDescription(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/batch-query-of-video-conference-information
updated_at: 2026-06-02 09:18:02
