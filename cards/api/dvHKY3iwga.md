# 邀请用户入会

doc_id: dvHKY3iwga
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/users/invite
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- optional: conferenceId(String)

## Query params
- none

## Body
- nick (String, required): 被邀请人姓名。
- optional: unionId(String), inviteeList(Array), phoneInviteeList(Array), phoneNumber(String)

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/invite-users-to-join
updated_at: 2026-06-02 12:05:48
