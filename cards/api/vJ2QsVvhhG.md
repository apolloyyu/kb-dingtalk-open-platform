# 根据手机号获取候选人信息

doc_id: vJ2QsVvhhG
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/ats/candidates
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- phoneNumber (String, required): 候选人手机号。 可以在智能招聘应用的候选人信息中获取。
- optional: bizCode(String)

## Body
- none

## Returns
- optional: candidateId(String), name(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-candidate-information-based-on-mobile-phone-number
updated_at: 2026-06-04 19:10:33
