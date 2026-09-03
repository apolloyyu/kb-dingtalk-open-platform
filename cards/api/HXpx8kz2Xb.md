# 执行工单活动

doc_id: HXpx8kz2Xb
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/customerService/tickets/{ticketId}
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_customer_service_ticket_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- ticketId (String, required): 工单ID。

## Query params
- none

## Body
- sourceId (String, required): 会员来源，取diamond配置的值。
- foreignId (String, required): 会员ID。
- foreignName (String, required): 会员名称。
- activityCode (String, required): 动作编码。
- optional: openInstanceId(String), productionType(Integer), properties(Array), name(String), value(String)

## Returns
- optional: taskId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/intelligent-customer-service-execute-work-order-activities
updated_at: 2026-06-02 19:50:17
