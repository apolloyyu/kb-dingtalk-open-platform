# 批量查询客户群

doc_id: Dn0xSVDrEn
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/crmGroupChats/batchQuery
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: openConversationIds(Array of String)

## Returns
- optional: result(Array), openConversationId(String), openGroupSetId(String), ownerUserId(String), ownerUserName(String), name(String), memberCount(Integer), gmtCreate(Long), iconUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-customer-groups-in-batches
updated_at: 2026-06-04 19:12:18
