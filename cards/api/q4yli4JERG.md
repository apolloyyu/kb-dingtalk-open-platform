# 查询企业内部群信息

doc_id: q4yli4JERG
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/securities/orgGroupInfos
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Group.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- pageSize (Integer, required): 分页大小。
- uuid (String, required): 每次查询唯一标识，保证每次分页查询时该值不变。
- operatorUserId (String, required): 当前查询人的userId。
- pageStart (Integer, required): 分页号，从1开始。
- optional: groupMembersCountEnd(Integer), syncToDingpan(Integer), groupOwner(String), createTimeEnd(Long), createTimeStart(Long), groupMembersCountStart(Integer), lastActiveTimeEnd(Long), groupName(String), lastActiveTimeStart(Long)

## Body
- none

## Returns
- optional: totalCount(Long), itemCount(Integer), items(Array), openConversationId(String), groupOwner(String), groupName(String), groupAdminsCount(Integer), groupMembersCount(Integer), groupCreateTime(Long), groupLastActiveTime(Long), groupLastActiveTimeShow(String), syncToDingpan(Integer), usedQuota(Long), groupOwnerUserId(String), status(Integer), templateId(String), templateName(String), extensions(Map<String, String>)

## Limits
- 群人数范围最大值，例如100。
- 创建时间查询最大时间戳。
- 每次查询唯一标识，保证每次分页查询时该值不变。
- 最后一次活跃时间戳最大值。

source_url: https://open.dingtalk.com/document/development/obtain-group-info
updated_at: 2026-06-04 19:09:59
