# 根据指定条件查询个人或企业客户数据

doc_id: jrpbAhrWLe
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/personalCustomers
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- maxResults (Integer, required): 每页条数，最大值100。
- optional: currentOperatorUserId(String), relationType(String), nextToken(String), queryDsl(String)

## Body
- none

## Returns
- optional: values(Array), instanceId(String), objectType(String), creatorUserId(String), creatorNick(String), data(Map), extendData(Map), permission(Object), ownerStaffIds(Array of String), participantStaffIds(Array of String), procOutResult(String), procInstStatus(String), gmtCreate(String), gmtModified(String), hasMore(Boolean), nextToken(String), maxResults(Integer), totalCount(Integer)

## Limits
- 每页条数，最大值100。

source_url: https://open.dingtalk.com/document/development/obtains-crm-individual-customers-in-batches-based-on-specified-query
updated_at: 2026-06-04 19:12:10
