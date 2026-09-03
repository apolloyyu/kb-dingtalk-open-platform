# 获取企业开通应用后的授权信息

doc_id: K9lVtuKSBB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/oauth2/apps/authInfo
api_version: v2-new
app_types: 第三方企业应用
permissions: isvapi_base

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过调用获取第三方企业应用的suiteAccessToken接口获取。

## Path params
- none

## Query params
- authCorpId (String, required): 授权企业的corpId。

## Body
- none

## Returns
- optional: authAppInfo(Object), agentList(Array), agentId(Long), agentName(String), appId(Long), adminList(Array of String), authCorpInfo(Object), inviteCode(String), industry(String), corpName(String), licenseCode(String), authChannel(String), authChannelType(String), authLevel(Long), inviteUrl(String), corpLogoUrl(String), authUserInfo(Object), userId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-authorization-information-after-the-enterprise-activates-the-application-1
updated_at: 2026-08-28 10:26:10
