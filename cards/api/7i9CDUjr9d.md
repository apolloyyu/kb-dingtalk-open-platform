# 分页查询工单

doc_id: 7i9CDUjr9d
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/customerService/tickets
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_customer_service_ticket_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- templateId (String, required): 工单模板ID。
- nextToken (String, required): 查询数据的起始位置，0表示从头开始。
- maxResults (Integer, required): 查询单页查询的最大条目数，最大值为100。
- optional: openInstanceId(String), productionType(Integer), ticketId(String), sourceId(String), foreignId(String), ticketStatus(String), startTime(Long), endTime(Long)

## Body
- none

## Returns
- optional: nextCursor(Long), total(Long), list(Array), foreignId(String), sourceId(String), foreignName(String), templateId(String), title(String), ticketId(String), ticketStatus(String), openInstanceId(String), productionType(Integer), gmtCreate(String), gmtModified(String), bizDataMap(Map)

## Limits
- 查询单页查询的最大条目数，最大值为100。

source_url: https://open.dingtalk.com/document/development/intelligent-customer-service-paging-query-work-order
updated_at: 2026-06-03 12:05:57
