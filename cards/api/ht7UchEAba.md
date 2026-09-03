# 查询动作记录

doc_id: ht7UchEAba
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/customerService/tickets/{ticketId}/actions
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_customer_service_ticket_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- ticketId (String, required): 工单ID。

## Query params
- nextToken (String, required): 查询数据的起始位置，0表示从头开始。
- maxResults (Long, required): 查询单页查询的最大条目数，最大值为100。
- optional: openInstanceId(String), productionType(Long)

## Body
- none

## Returns
- optional: nextCursor(Long), total(Long), list(Array), operatorId(String), operator(String), operatorRole(String), actionCode(String), actionContent(Array), displayValue(String), displayName(String), name(String), value(String), valueType(String)

## Limits
- 查询单页查询的最大条目数，最大值为100。

source_url: https://open.dingtalk.com/document/development/intelligent-customer-service-query-action-records
updated_at: 2026-06-04 19:10:46
