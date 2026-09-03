# 根据指定条件查询联系人数据

doc_id: hVuAIe3Pdt
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/customObjects/contacts/datas/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- maxResults (Long, required): 分页大小。 **[!NOTE]** 最多可一次获取200条数据。
- optional: currentOperatorUserId(String), objectType(String), nextToken(String), providerCorpId(String), queryDsl(String)

## Returns
- optional: result(Object), nextToken(String), hasMore(Boolean), maxResults(Long), values(Array), gmtModified(String), creatorUserId(String), instanceId(String), data(Map<String, String>), extendData(Map<String, String>), gmtCreate(String), objectType(String), permission(Object), participantUserIds(Array of String), ownerUserIds(Array of String)

## Limits
- 分页大小。 **[!NOTE]** 最多可一次获取200条数据。

source_url: https://open.dingtalk.com/document/development/api-getcontacts
updated_at: 2026-06-04 19:12:12
