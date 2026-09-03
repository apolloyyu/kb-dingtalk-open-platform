# 查询企业是否实名认证

doc_id: 6THV76J8WN
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/esign/corps/infos
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: isRealName(String), orgRealName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-enterprise-information
updated_at: 2026-06-04 19:11:07
