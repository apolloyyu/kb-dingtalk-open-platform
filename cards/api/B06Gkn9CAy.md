# 创建自助单

doc_id: B06Gkn9CAy
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/customerService/tickets
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_customer_service_ticket_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- sourceId (String, required): 会员来源，取diamond配置的值。
- foreignId (String, required): 第三方会员ID。
- foreignName (String, required): 第三方会员名称。
- templateId (String, required): 自助单ID，钉钉智能客服自助单配置里的值。
- title (String, required): 工单标题。
- optional: openInstanceId(String), productionType(Integer), properties(Array), name(String), value(String)

## Returns
- optional: ticketId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-self-service-ticket
updated_at: 2026-06-04 19:10:45
