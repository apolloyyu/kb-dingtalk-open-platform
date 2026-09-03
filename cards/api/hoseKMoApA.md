# 通知退款结果

doc_id: hoseKMoApA
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/finance/payCodes/refundResults/notify
api_version: v2-new
app_types: 第三方企业应用
permissions: Finance.PayCode.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- corpId (String, required): 企业corpId。可在钉钉开发者后台首页查看。
- userId (String, required): 用户userId，需要和创建码时传入的userId保持一致。
- tradeNo (String, required): 交易订单号，调用方生成。
- refundOrderNo (String, required): 本次退款订单号，由调用方生成。
- remark (String, required): 备注。
- refundAmount (String, required): 退款金额。
- refundPromotionAmount (String, required): 退款的优惠金额。
- gmtRefund (String, required): 退款时间。 格式：yyyy-MM-dd HH:mm:ss。
- payChannelDetailList (Array, required): 支付渠道明细信息。
- payChannelName (String, required): 支付渠道名称，最终展示在钉钉用户账单明细中。例如：支付宝、食堂点券等。
- payChannelType (String, required): 支付渠道类型，取值： - **ALIPAY**：支付宝 - **BALANCE**：余额
- amount (String, required): 支付渠道金额。
- payChannelOrderNo (String, required): 支付渠道订单号。
- payChannelRefundOrderNo (String, required): 支付渠道退款订单号。
- promotionAmount (String, required): 优惠金额。
- fundToolDetailList (Array, required): 资金工具明细。
- fundToolName (String, required): 资金工具名称。例如：余额。
- gmtCreate (String, required): 开始时间。 格式：yyyy-MM-dd HH:mm:ss。
- gmtFinish (String, required): 结束时间。 格式：yyyy-MM-dd HH:mm:ss。
- promotionFundTool (Boolean, required): 是否优惠资金工具。 - **true**：是 - **false**：不是
- payCode (String, required): 付款码。
- optional: extInfo(String)

## Returns
- optional: result(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-payment-code-refund-information-synchronization-operation
updated_at: 2026-06-04 19:11:58
