# 升级普通群为服务群

doc_id: KrDMBfRdXr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/normalGroups/upgrade
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
- optional: openGroupSetId(String), templateId(String), openTeamId(String)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/a-dingtalk-group-is-upgraded-to-one-of-the-intelligent
updated_at: 2026-06-04 19:11:24
