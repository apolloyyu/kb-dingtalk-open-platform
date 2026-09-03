# 获取组织服务窗账号列表

doc_id: hMq9NyMlk0
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/link/isv/accounts
api_version: v2-new
app_types: 第三方企业应用
permissions: OfficialAccount.Meta.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用本接口的访问凭证，通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: result(Array), accountId(String), accountName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/the-third-party-enterprise-application-obtains-the-account-list-of-the
updated_at: 2026-06-04 11:30:46
