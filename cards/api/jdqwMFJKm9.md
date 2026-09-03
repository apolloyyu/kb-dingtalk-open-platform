# 获取审批里创建的与CRM客户关联的TAB表单数据实例列表

doc_id: jdqwMFJKm9
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/formRelatedTabs/datas/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_customdata_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: viewUserId(String), nextToken(Long), formCode(String), maxResults(Integer), relatedField(String), relatedInstId(String)

## Returns
- optional: result(Object), page(Object), hasMore(Boolean), nextToken(Long), totalCount(Long), list(Array), abstractMessage(String), createTime(Long), title(String)

## Limits
- 每页最大的个数

source_url: https://open.dingtalk.com/document/development/api-getrelatedviewtabdata
updated_at: 2026-06-03 09:36:59
