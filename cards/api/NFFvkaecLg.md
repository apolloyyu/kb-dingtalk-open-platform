# 套餐转售—分润模式

doc_id: NFFvkaecLg
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/orders/channel
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- none

## Query params
- none

## Body
- orderId (String, required): 第三方的订单ID，需保证唯一性。
- itemCode (String, required): 商品ID。
- itemName (String, required): 商品名称。
- quantity (Float, required): 购买数量。
- orderCreateTime (Float, required): 下单时间。
- optional: payFee(Float)

## Returns
- optional: esignOrderId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/package-resale-1-distribution-mode
updated_at: 2026-06-23 18:15:57
