# 创建场景服务群

doc_id: UdNVgTsFMk
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/groups
api_version: v2-new
app_types: 企业内部应用
permissions: ServiceGroup.Group.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openTeamId (String, required): 开放团队ID。
- openGroupSetId (String, required): 开放群组ID。
- groupName (String, required): 群名称。
- ownerStaffId (String, required): 群主员工userid。
- optional: groupBizId(String), memberStaffIds(Array of String), groupTagNames(Array of String)

## Returns
- optional: openConversationId(String), groupUrl(String)

## Limits
- 群成员员工ID列表，最大值20。

source_url: https://open.dingtalk.com/document/development/create-a-scenario-service-group
updated_at: 2026-06-04 19:11:22
