# 确认完成权益的更新

doc_id: 1hlR7qkqSL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/ats/rights/{rightsCode}/confirm
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- rightsCode (String, required): 权益码，常见权益码如下： - RIGHTS_ATS_ADVANCED：智能招聘高级版 其他权益场景需线下提供，请通过技术支持-在线答疑自助工具咨询。

## Query params
- optional: bizCode(String)

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/confirm-benefits
updated_at: 2026-06-04 19:10:35
