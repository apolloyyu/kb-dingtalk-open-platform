# 解码钉工牌电子码

doc_id: mOjXv1UkX8
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/finance/payCodes/decode
api_version: v2-new
app_types: 第三方企业应用
permissions: Finance.PayCode.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: payCode(String), requestId(String)

## Returns
- optional: corpId(String), userId(String), userInCorp(Boolean), codeType(String), alipayCode(String), userCorpRelationType(String), codeIdentity(String), codeId(String), outBizId(String), extInfo(String)

## Limits
- 请求ID，由调用方随机生成幂等字符串。 例如： - UUID随机字符串 - 时间戳+用户ID等 - 两次调用解码同一个码，传的requestId必须要一致，才能解码成功。 - 调用支付宝解码后，10分钟后码就会过期，再次调用，即使使用相同的**requestId**，支付宝也会返回失败。

source_url: https://open.dingtalk.com/document/development/decoding-dingtalk-payment-code
updated_at: 2026-06-04 19:11:57
