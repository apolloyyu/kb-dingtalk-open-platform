# 查询服务群活跃用户

doc_id: AjrbM8o2jX
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/groups/queryActiveUsers
api_version: v2-new
app_types: 企业内部应用
permissions: ServiceGroup.Group.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- openConversationId (String, required): 群ID。
- optional: openTeamId(String)

## Body
- none

## Returns
- optional: activeUserInfos(Array), unionId(String), nickName(String), actionIndexL7d(double), actionIndexL14d(double), actionIndexL30d(double), activeScore(double), ranking(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-active-service-users
updated_at: 2026-06-04 19:11:23
