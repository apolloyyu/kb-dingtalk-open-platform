# 解码钉工牌电子码

doc_id: rGYuVi6A3C
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/badge/codes/decode
api_version: v2-new
app_types: 第三方企业应用
permissions: Badge.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- payCode (String, required): 码值，解码接口仅支持钉钉侧生成的码值。 目前不支持标准码解析，标准码是由支付宝侧生成的。
- requestId (String, required): 请求ID，由调用方随机生成幂等字符串。 例如： - UUID随机字符串 - 时间戳+用户ID等 - 两次调用解码同一个码，传的requestId必须要一致，才能解码成功。 - 调用支付宝解码后，10分钟后码就会过期，再次调用，即使使用相同的**requestId**，支付宝也会返回失败。

## Returns
- optional: corpId(String), userId(String), codeType(String), alipayCode(String), userCorpRelationType(String), codeIdentity(String), codeId(String), outBizId(String), extInfo(String)

## Limits
- 请求ID，由调用方随机生成幂等字符串。 例如： - UUID随机字符串 - 时间戳+用户ID等 - 两次调用解码同一个码，传的requestId必须要一致，才能解码成功。 - 调用支付宝解码后，10分钟后码就会过期，再次调用，即使使用相同的**requestId**，支付宝也会返回失败。

source_url: https://open.dingtalk.com/document/development/stack-dingtalk-badge
updated_at: 2026-07-20 09:21:57
