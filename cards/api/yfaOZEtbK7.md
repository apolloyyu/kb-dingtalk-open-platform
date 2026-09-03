# 授权企业账号可加入多组织

doc_id: yfaOZEtbK7
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccounts/multiOrgPermissions/auth
api_version: v2-new
app_types: 企业内部应用
permissions: Contact.OrgAccountSecurity.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- joinCorpId (String, required): 被授权的组织CorpId。
- optional: grantDeptIdList(Array of Long)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/authorize-a-dedicated-account-to-join-multiple-organizations
updated_at: 2026-06-08 11:20:17
