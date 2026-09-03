# 获取单个客户群详情

doc_id: KkD2HzjBXY
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/crmGroupChats/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- openConversationId (String, required): 客户群openConversationId，调用查询客户群列表接口获取openConversationId参数值。

## Body
- none

## Returns
- optional: openConversationId(String), openGroupSetId(String), ownerUserId(String), ownerUserName(String), name(String), memberCount(Integer), gmtCreate(Long), iconUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-a-single-customer-group
updated_at: 2026-06-04 19:12:18
