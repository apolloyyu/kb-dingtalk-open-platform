# 通过免登码获取用户信息

doc_id: H2mylS6eke
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/getuserinfo
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- code (String, required): 免登授权码，获取方式请参考： - 小程序：getAuthCode - 微应用：requestAuthCode **[!NOTE]** 此授权码五分钟内有效，且只能使用一次。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(UserGetByCodeResponse), userid(String), device_id(String), sys(Boolean), sys_level(Number), associated_unionid(String), unionid(String), name(String)

## Limits
- 免登授权码，获取方式请参考： - 小程序：getAuthCode - 微应用：requestAuthCode **[!NOTE]** 此授权码五分钟内有效，且只能使用一次。

source_url: https://open.dingtalk.com/document/development/obtain-the-userid-of-a-user-by-using-the-log-free
updated_at: 2026-07-02 10:35:34
