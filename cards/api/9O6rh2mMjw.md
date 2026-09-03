# 获取用户token

doc_id: 9O6rh2mMjw
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/oauth2/userAccessToken
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用, 第三方个人应用
permissions: open_app_api_base

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- clientId (String, required): 应用id。可使用扫码登录应用或者第三方个人小程序的appId。 - 企业内部应用传应用的**AppKey** - 第三方企业应用传应用的**SuiteKey** - 第三方个人应用传应用的**AppId**
- clientSecret (String, required): 应用密钥。 - 企业内部应用传应用的**AppSecret** - 第三方企业应用传应用的**SuiteSecret** - 第三方个人应用传应用的**AppSecret**
- grantType (String, required): - 如果使用授权码换token：传`authorization_code`，此时必须填写`code`参数。 - 使用刷新 token 换新 token：传`refresh_token`，此时必须填写`refreshToken`参数。
- optional: code(String), refreshToken(String)

## Returns
- optional: accessToken(String), refreshToken(String), expireIn(Long), corpId(String)

## Limits
- OAuth 2.0 刷新令牌，从上一次接口返回结果中获取。有效期为 30 天。
- > - `accessToken`的有效期为7200秒（2小时），有效期内重复获取将返回相同结果并自动续期；过期后获取会返回新的`accessToken`。

source_url: https://open.dingtalk.com/document/development/obtain-user-token
updated_at: 2026-06-30 16:50:33
