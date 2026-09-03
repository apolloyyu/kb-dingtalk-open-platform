# 获取第三方企业应用的suite_access_token

doc_id: pEN2VC7PiA
completeness: full
archived: true
method: POST
endpoint: https://oapi.dingtalk.com/service/get_suite_token
api_version: v1-oapi
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- suite_key (String, required): 第三方应用的suiteKey。可在钉钉开发者后台的应用详情页获取。
- suite_secret (String, required): 第三方应用的suiteSecret，可在钉钉开发者后台的应用详情页获取。
- suite_ticket (String, required): 钉钉开放平台会向应用的回调URL推送的suite_ticket（约5个小时推送一次），详细内容请参考数据格式biz_type=2。

## Returns
- optional: errmsg(String), errcode(Number), suite_access_token(String), expires_in(Number)

## Limits
- 钉钉开放平台会向应用的回调URL推送的suite_ticket（约5个小时推送一次），详细内容请参考数据格式biz_type=2。
- 第三方企业应用的凭证过期时间，单位秒。 **[!NOTE]** suite_access_token有效期为7200秒，过期之前建议服务端做定时器主动更新，而不是依赖钉钉的定时推送。

source_url: https://open.dingtalk.com/document/development/obtain-application-suite-ticket
updated_at: 2026-08-25 09:36:31
