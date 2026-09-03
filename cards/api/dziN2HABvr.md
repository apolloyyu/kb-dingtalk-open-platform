# 升级云客服服务群为钉钉智能服务群

doc_id: dziN2HABvr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/cloudGroups/upgrade
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
- openConversationId (String, required): 群ID。
- ccsInstanceId (String, required): 智能云客服租户ID。
- optional: templateId(String), openGroupSetId(String), openTeamId(String)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/upgraded-the-cloud-customer-service-group-to-the-dingtalk-intelligent
updated_at: 2026-06-03 09:11:05
