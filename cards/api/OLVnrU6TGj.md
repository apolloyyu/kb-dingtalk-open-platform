# 启用企业账号

doc_id: OLVnrU6TGj
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccounts/enable
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
- userId (String, required): 企业账号的userid，可通过以下四种方式获得： - 根据手机号查询企业账号用户 - 创建SSO企业账号 - 创建钉钉自建企业账号 - 邀请其他组织企业账号加入

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/enable-a-dedicated-account
updated_at: 2026-06-02 09:18:14
