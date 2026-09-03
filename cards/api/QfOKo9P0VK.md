# 判断用户是否是认证组织的语文老师接口

doc_id: QfOKo9P0VK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/edu/paas/certifiedTeachers/chineseTeachers/check
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_get_member

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该API的应用凭证，通过服务商获取第三方应用授权企业的access_token接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 可通过根据手机号获取userid接口获取userid；长度限制1～50个字符。
- bizCode (String, required): 三方ISV接入的业务编码，长度限制1～50个字符。

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- 可通过根据手机号获取userid接口获取userid；长度限制1～50个字符。
- 三方ISV接入的业务编码，长度限制1～50个字符。

source_url: https://open.dingtalk.com/document/development/api-isyuwencertifiedteacher
updated_at: 2026-06-08 09:48:21
