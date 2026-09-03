# 更换服务群所在的群分组

doc_id: UnMHc8jGkU
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/groups/configurations
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
- optional: openTeamId(String), openConversationId(String), openGroupSetId(String)

## Returns
- optional: success(Boolean)

## Limits
- 内部群只能更换到内部服务群组，外部群只能更换到外部服务群组。例如，服务群A当前所在分组为**内部服务群组**，更换服务群A所在的分组时，只能更换到另一个**内部服务群组**内。

source_url: https://open.dingtalk.com/document/development/modify-a-service-group
updated_at: 2026-06-04 19:11:24
