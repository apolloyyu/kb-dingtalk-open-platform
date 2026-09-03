# 获取企业专属钉钉权益列表

doc_id: mZp8OLkAR2
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/benefits
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Industry.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: benefitsList(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-queryexclusivebenefits
updated_at: 2026-06-02 19:19:58
