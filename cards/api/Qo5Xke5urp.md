# 获取企业实名地址

doc_id: Qo5Xke5urp
completeness: full
archived: true
method: POST
endpoint: https://api.dingtalk.com/v1.0/esign/corps/realname
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 当前用户的userId。 必须是管理员。

## Returns
- optional: code(Integer), message(String), data(Object), taskId(String), pcUrl(String), mobileUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-enterprise-real-name-address
updated_at: 2026-08-25 09:37:32
