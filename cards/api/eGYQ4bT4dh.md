# 获取全量个人或企业客户数据

doc_id: eGYQ4bT4dh
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/customerInstances
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
- optional: operatorUserId(String), maxResults(Long), nextToken(String), objectType(String)

## Returns
- optional: result(Object), nextToken(String), values(Array), creatorNick(String), modifyTime(String), creatorUserId(String), instanceId(String), data(Map), extendData(Map), createTime(String), objectType(String), permission(Object), participantStaffIds(Array of String), ownerStaffIds(Array of String), processOutResult(String), processInstanceStatus(String), maxResults(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/crm-obtains-all-private-sea-customer-data
updated_at: 2026-06-04 19:12:09
