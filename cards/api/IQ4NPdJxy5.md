# 获取授权的页面地址

doc_id: IQ4NPdJxy5
completeness: full
archived: true
method: POST
endpoint: https://api.dingtalk.com/v1.0/esign/auths/url
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
- optional: redirectUrl(String)

## Returns
- optional: data(Object), taskId(String), mobileUrl(String), pcUrl(String), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/authurl
updated_at: 2026-08-25 09:37:25
