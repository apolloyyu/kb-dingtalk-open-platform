# 通知支付结果

doc_id: X2vIAkYJI1
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/badge/codes/payResults
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
- payCode (String, required): 码值，接入方硬件设备扫描钉工牌二维码获取的码值。
- corpId (String, required): 企业corpId。可在钉钉开发者后台首页查看。
- userId (String, required): 用户userId，需要与生成码时传入的**userId**保持一致。
- gmtTradeCreate (String, required): 交易开始时间。 格式：yyyy-MM-dd HH:mm:ss。
- gmtTradeFinish (String, required): 交易结束时间。 格式：yyyy-MM-dd HH:mm:ss。
- tradeNo (String, required): 交易号，接入方自身系统针对交易生成的唯一订单号。
- tradeStatus (String, required): 交易状态，取值： - **SUCCESS**：成功 - **FALL**：失败
- title (String, required): 订单标题。
- remark (String, required): 备注。
- amount (String, required): 订单金额。
- promotionAmount (String, required): 订单优惠金额。
- chargeAmount (String, required): 收费金额。 - 该笔交易针对收款方的收费金额, 如果没有传0.00。 - 收单情况下，支付宝向调用方收取的手续费。
- payChannelDetailList (Array, required): 支付渠道明细信息。 - 如果**tradeStatus**为**SUCCESS**（支付成功），支付渠道信息则必传。 - 如果**tradeStatus**为**FAIL**（支付失败），同时建议传递**tradeErrorCode**, **tradeErrorMsg**，用于告知用户扣款失败原因。
- payChannelName (String, required): 支付渠道名称。
- payChannelType (String, required): 支付渠道类型，取值： - **ALIPAY**：支付宝 - **BALANCE**：余额
- payChannelOrderNo (String, required): 支付渠道单号。
- fundToolDetailList (Array, required): 资金工具明细。
- fundToolName (String, required): 资金渠道名称。
- promotionFundTool (Boolean, required): 是否是优惠工具。 - **true**：是 - **false**：不是
- merchantName (String, required): 商户名称。
- optional: gmtCreate(String), gmtFinish(String), extInfo(String), tradeErrorCode(String), tradeErrorMsg(String)

## Returns
- optional: result(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/sync-dingtalk-badge-code-payment-result
updated_at: 2026-06-04 19:11:53
