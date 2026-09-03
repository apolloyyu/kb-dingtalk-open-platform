# 查询客户群列表

doc_id: AbdLvSP5Uu
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/crmGroupChats
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- relationType (String, required): 关系类型。 - **crm_customer**：企业客户。 - **crm_customer_personal**：个人客户。
- maxResults (Integer, required): 每页最大条目数，最大值100。
- optional: nextToken(String), queryDsl(String)

## Body
- none

## Returns
- optional: resultList(Array), openConversationId(String), openGroupSetId(String), ownerUserId(String), ownerUserName(String), name(String), memberCount(Integer), gmtCreate(Long), hasMore(Boolean), nextToken(String), totalCount(Integer)

## Limits
- 每页最大条目数，最大值100。

source_url: https://open.dingtalk.com/document/development/query-the-list-of-customer-groups
updated_at: 2026-06-04 19:12:17
