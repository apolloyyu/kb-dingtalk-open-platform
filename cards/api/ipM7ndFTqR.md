# 获取定制应用的accessToken

doc_id: ipM7ndFTqR
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/oauth2/corpAccessToken
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: isvapi_base

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- suiteKey (String, required): 定制应用的CustomKey。
- suiteSecret (String, required): 定制应用的CustomSecret。
- authCorpId (String, required): 授权企业的CorpId。iShot2022-10-17 10
- suiteTicket (String, required): 钉钉推送的suiteTicket，定制应用该参数自定义，比如Test。

## Returns
- optional: accessToken(String), expireIn(Long)

## Limits
- 定制应用的accessToken超时时间，单位秒。 **[!NOTE]** accessToken的有效期为7200秒（2小时），有效期内重复获取会返回新的accessToken。

source_url: https://open.dingtalk.com/document/development/obtain-the-access-token-of-the-third-party-application-authorization-enterprise
updated_at: 2026-04-29 22:27:43
