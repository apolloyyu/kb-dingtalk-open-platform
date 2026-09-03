# 获取企业内部应用的accessToken

doc_id: yCG0X9Q1im
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/oauth2/accessToken
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- appKey (String, required): 已创建的企业内部应用的 Client ID，获取方式可参考Client ID/Client Secret文档说明。
- appSecret (String, required): 已创建的企业内部应用的 Client Secre ，获取方式可参考Client ID/Client Secret文档说明。 请妥善保管Client Secret，避免泄露。

## Returns
- optional: accessToken(String), expireIn(Long)

## Limits
- accessToken的过期时间，单位秒。 accessToken的有效期为7200秒（2小时），有效期内重复获取会返回相同结果并自动续期，过期后获取会返回新的accessToken。

source_url: https://open.dingtalk.com/document/development/obtain-the-access-token-of-an-internal-app
updated_at: 2026-08-25 09:36:27
