# 获取第三方企业应用的suiteAccessToken

doc_id: 5dOoWwTh3G
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/oauth2/suiteAccessToken
api_version: v2-new
app_types: 第三方企业应用
permissions: isvapi_base

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- suiteKey (String, required): 已创建的第三方企业应用的 Cilent ID（原第三方企业应用SuiteKey）。
- suiteSecret (String, required): 已创建的第三方企业应用的 Cilent Secret（原第三方企业应用SuiteSecret）。
- suiteTicket (String, required): 钉钉开放平台会向应用的回调URL推送的suite_ticket（约5个小时推送一次），详细内容请参考套件票据。

## Returns
- optional: accessToken(String), expireIn(Long)

## Limits
- 钉钉开放平台会向应用的回调URL推送的suite_ticket（约5个小时推送一次），详细内容请参考套件票据。
- 第三方企业应用的凭证过期时间，单位秒。 suiteAccessToken有效期为7200秒，过期之前建议服务端做定时器主动更新，而不是依赖钉钉的定时推送。

source_url: https://open.dingtalk.com/document/development/obtains-the-suite-acess-token-of-third-party-enterprise-applications
updated_at: 2026-06-08 12:02:04
