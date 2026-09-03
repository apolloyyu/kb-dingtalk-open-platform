# 企业账号转交主管理员（创建者）

doc_id: 7lOl6H6zqn
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccounts/mainAdministrators/change
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
- sourceUserId (String, required): 原企业账号userid，可通过以下四种方式获得： - 根据手机号查询企业账号用户 - 创建SSO企业账号 - 创建钉钉自建企业账号 - 邀请其他组织企业账号加入
- targetUserId (String, required): 接收专属账号userid，可通过以下四种方式获得： - 根据手机号查询企业账号用户 - 创建SSO企业账号 - 创建钉钉自建企业账号 - 邀请其他组织企业账号加入
- effectCorpId (String, required): 被转交的组织corpId。详情参见基础概念-CorpId。

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/transfer-exclusive-account-to-main-administrator-creator
updated_at: 2026-06-01 16:05:16
