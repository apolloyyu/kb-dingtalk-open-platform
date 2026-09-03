# 创建客户群

doc_id: PVk5TzO3B9
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/groups
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- groupName (String, required): 群名称。
- ownerUserId (String, required): 群主userId。
- relationType (String, required): 关系类型。 - **crm_customer**：企业客户 - **crm_customer_personal**：个人客户
- optional: memberUserIds(String)

## Returns
- optional: openConversationId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-customer-group
updated_at: 2026-06-04 19:12:16
