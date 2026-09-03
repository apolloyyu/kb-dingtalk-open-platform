# 通知退款结果

doc_id: ZVlykdzN9D
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/badge/codes/refundResults
api_version: v2-new
app_types: 第三方企业应用
permissions: Badge.Common.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- corpId (String, required): 企业corpId。可在钉钉开发者后台首页查看。
- userId (String, required): 用户userId，需要与生成码时使用的**userId**保持一致。
- tradeNo (String, required): 交易订单号，自定义，接入方针对交易生成的唯一订单号。
- refundOrderNo (String, required): 本次退款订单号，自定义，接入方针对交易生成的唯一退款订单号。
- remark (String, required): 备注。
- refundAmount (String, required): 退款金额。
- refundPromotionAmount (String, required): 退款的优惠金额。
- gmtRefund (String, required): 退款时间。 格式：yyyy-MM-dd HH:mm:ss。
- payChannelDetailList (Array, required): 支付渠道明细信息。
- payChannelName (String, required): 支付渠道名称。
- payChannelType (String, required): 支付渠道类型，取值： - **ALIPAY**：支付宝 - **BALANCE**：余额
- amount (String, required): 金额。
- payChannelOrderNo (String, required): 支付渠道号，调用方接入的支付渠道的单号。
- payChannelRefundOrderNo (String, required): 支付渠道退款号，调用方接入的支付渠道的退款单号。
- promotionAmount (String, required): 优惠金额。
- fundToolDetailList (Array, required): 支付资金列表。
- fundToolName (String, required): 资金工具名称。
- gmtCreate (String, required): 创建时间。 格式：yyyy-MM-dd HH:mm:ss。
- gmtFinish (String, required): 完成时间。 格式：yyyy-MM-dd HH:mm:ss。
- promotionFundTool (Boolean, required): 是否是优惠工具。 - **true**：是 - **false**：不是
- payCode (String, required): 支付时使用的付款码。
- optional: extInfo(String)

## Returns
- optional: result(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/notification-dingtalk-badge-code-refund-result
updated_at: 2026-06-04 19:11:54
