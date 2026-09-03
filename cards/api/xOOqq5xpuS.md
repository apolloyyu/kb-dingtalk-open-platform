# 获取企业最新钉钉指数信息

doc_id: xOOqq5xpuS
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/dingIndexs
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: statDate(String), idxTotal(Float), idxEfficiency(Float), idxCarbon(Float), idxMonthlyAvg(Float)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-latest-dingtalk-index-information
updated_at: 2026-06-01 16:08:52
