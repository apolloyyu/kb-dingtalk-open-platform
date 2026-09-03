# 创建视频会议

doc_id: LwIgI3MLdf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences
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
- userId (String, required): 会议发起人的unionId，可调用查询用户详情接口获取。
- confTitle (String, required): 预约会议标题。标题最大长度限制不允许超过50。超过50字符时会被截断。超过256字符时调用接口会失败。
- optional: inviteUserIds(Array of String), inviteCaller(Boolean)

## Returns
- optional: conferenceId(String), conferencePassword(String), hostPassword(String), externalLinkUrl(String), phoneNumbers(Array of String), roomCode(String)

## Limits
- 预约会议标题。标题最大长度限制不允许超过50。超过50字符时会被截断。超过256字符时调用接口会失败。

source_url: https://open.dingtalk.com/document/development/create-a-video-conference
updated_at: 2026-06-02 09:18:05
