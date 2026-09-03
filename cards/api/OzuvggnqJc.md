# 查询会议室分组信息

doc_id: OzuvggnqJc
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/rooms/groups/{groupId}
api_version: v2-new
app_types: 第三方企业应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- groupId (Long, required): 分组ID，可调用查询会议室分组列表接口获取。

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取获取。

## Body
- none

## Returns
- optional: groupId(Long), groupName(String), parentId(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-meeting-room-groups
updated_at: 2026-06-03 10:12:12
