# 查询应用市场订单详情

doc_id: WTmKSr868s
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/appMarket/orders/{orderId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Market.Order.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- optional: orderId(Long)

## Query params
- none

## Body
- none

## Returns
- optional: bizOrderId(Long), corpId(String), itemCode(String), itemName(String), goodsCode(String), goodsName(String), totalActualPayFee(Long), status(Long), quantity(Long), paidTimestamp(Long), createTimestamp(Long), startTimestamp(Long), endTimestamp(Long), inAppOrder(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/check-the-order-details-app-store
updated_at: 2026-07-08 14:13:51
