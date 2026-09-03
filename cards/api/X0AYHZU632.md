# 查询客户群组列表

doc_id: X0AYHZU632
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/groupSets/lists
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- relationType (String, required): 关系类型。 - **crm_customer**：企业客户 - **crm_customer_personal**：个人客户
- optional: nextToken(String), maxResults(Integer), queryDsl(String)

## Body
- none

## Returns
- optional: hasMore(Boolean), nextToken(String), resultList(Array), name(String), openGroupSetId(String), relationType(String), memberQuota(Integer), memberCount(Integer), templateId(String), ownerUserId(String), managerUserIds(String), notice(String), noticeToped(Integer), owner(Object), userId(String), manager(Array), lastOpenConversationId(String), gmtCreate(String), gmtModified(String), groupChatCount(Integer), totalCount(Integer)

## Limits
- 每页条目数，最大值10。
- 群组内单个群的人数上限。
- 有2个客户群，为“核心客户1群”、“供应商客户1群”，对应的群组分别为“核心客户”、“供应商客户”，如下图所示。调用本接口，获取所有名称包含“客户”的客户群组列表，按创建时间降序结果为：

source_url: https://open.dingtalk.com/document/development/query-groups
updated_at: 2026-06-03 15:47:52
