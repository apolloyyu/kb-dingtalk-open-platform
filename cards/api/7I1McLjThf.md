# 关闭视频会议

doc_id: 7I1McLjThf
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- conferenceId (String, required): 会议ID，可调用创建视频会议接口获取conferenceId参数值。

## Query params
- unionId (String, required): 员工在当前开发者企业账号范围内的唯一标识，可调用查询用户详情接口获取unionid参数值。

## Body
- none

## Returns
- optional: code(Long), cause(String)

## Limits
- 调用本接口，关闭视频会议，仅限该会议的主持人有关闭视频会议的权限。

source_url: https://open.dingtalk.com/document/development/close-audio-video-conference
updated_at: 2026-06-02 09:18:04
