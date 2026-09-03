# 创建会议室预定黑名单

doc_id: O23nOyz3GL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/rooms/bookings/blacklist
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
- unionId (String, required): 操作人unionId。
- blacklistUnionId (String, required): 黑名单用户的unionId。
- startTime (Long, required): 封禁开始时间，毫秒级UTC时间戳。
- optional: endTime(Long), memo(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createbookingblacklist
updated_at: 2026-06-02 13:04:56
