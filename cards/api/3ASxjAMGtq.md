# 套餐转售—底价结算模式

doc_id: 3ASxjAMGtq
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/orders/resale
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
- orderId (String, required): isv方的订单ID，用于幂等，请保证唯一性。
- quantity (Float, required): 购买数量，电子合同份数。
- orderCreateTime (Float, required): 下单时间。
- serviceStopTime (Float, required): 合同失效截止日期。默认有效时间一年。
- optional: serviceStartTime(Float)

## Returns
- optional: esignOrderId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/package-resale-2-reserve-price-settlement-mode
updated_at: 2026-06-04 19:11:05
