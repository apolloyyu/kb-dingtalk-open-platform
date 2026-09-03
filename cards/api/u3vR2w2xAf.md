# 获取企业认证信息

doc_id: u3vR2w2xAf
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/organizations/authInfos
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.Org.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: targetCorpId(String)

## Body
- none

## Returns
- optional: orgName(String), licenseOrgName(String), registrationNum(String), unifiedSocialCredit(String), organizationCode(String), legalPerson(String), licenseUrl(String), authLevel(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-enterprise-authentication-information
updated_at: 2026-06-01 16:09:42
