# 套餐转售（分润模式）

doc_id: IEM394BPCe
completeness: full
archived: true
method: POST
endpoint: https://api.dingtalk.com/v1.0/esign/orders/channel
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
- itemCode (String, required): 商品id。
- itemName (String, required): 商品名称。
- orderId (String, required): ISV方订单Id，用于幂等，请保证唯一性。
- payFee (Long, required): 支付金额，以分为单位。 **[!NOTE]** 仅作记录，不作为凭证。
- quantity (Long, required): 购买数量。
- optional: orderCreateTime(Long)

## Returns
- optional: code(Integer), message(String), data(Object), esignOrderId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/package-resale-profit-distribution-model-1
updated_at: 2026-08-25 09:37:27
