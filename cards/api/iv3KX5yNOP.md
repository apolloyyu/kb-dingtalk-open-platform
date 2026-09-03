# 查询客户数据

doc_id: iv3KX5yNOP
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/relations/datas/targets/{targetId}
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- targetId (String, required): 客户的unionId，只能通过以下方式获取： - 企业内部应用，调用查询用户详情接口获取。 - 第三方企业应用，通过钉钉统一授权套件获取。

## Query params
- relationType (String, required): 关系类型。 - **crm_customer**：企业客户 - **crm_customer_personal**：个人客户

## Body
- none

## Returns
- optional: relations(Array), relationId(String), relationType(String), bizDataList(Array), key(String), value(String), extendValue(String), openConversationIds(Array of String)

## Limits
- 客户的unionId，只能通过以下方式获取： - 企业内部应用，调用查询用户详情接口获取。 - 第三方企业应用，通过钉钉统一授权套件获取。

source_url: https://open.dingtalk.com/document/development/querying-customer-data
updated_at: 2026-06-03 09:36:57
