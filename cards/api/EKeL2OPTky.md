# 套餐转售（底价结算模式）

doc_id: EKeL2OPTky
completeness: full
archived: true
method: POST
endpoint: https://api.dingtalk.com/v1.0/esign/orders/resale
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- serviceStartTime (Long, required): 合同生效起始时间，Unix时间戳。
- serviceStopTime (Long, required): 合同失效截止日期，Unix时间戳，默认有效时间一年。
- orderCreateTime (Long, required): 下单时间，Unix时间戳。
- orderId (String, required): ISV方的订单Id，用于幂等，请保证唯一性。
- quantity (Long, required): 购买数量（电子合同份数）。

## Returns
- optional: code(Integer), message(String), data(Object), esignOrderId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/package-resale-base-price-settlement-mode-1
updated_at: 2026-08-25 09:37:28
