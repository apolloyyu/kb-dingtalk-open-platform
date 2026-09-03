# 获取分组管理员信息

doc_id: KJJcGIuW0z
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/rooms/groupAdmin/{groupId}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- optional: groupId(Long)

## Query params
- optional: unionId(String)

## Body
- none

## Returns
- optional: result(Object), groupId(Long), groupName(String), groupAdmins(Array), memberId(String), memberName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-querymeetingroomgroupadmin
updated_at: 2026-07-03 09:40:10
