# 授权其他组织查看本组织的企业账号信息

doc_id: Yj2lhCCjlN
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccounts/mobiles/visibleInOtherOrg
api_version: v2-new
app_types: 企业内部应用
permissions: Contact.OrgAccount.VisiblityInOtherOrg

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- toCorpIds (Array of String, required): 被授权组织对应corpId列表。 **[!NOTE]** 被授权组织的corpId列表和调用接口的调用者对应 userId，都不能为空且参数出错会导致调用报错。
- optUserId (String, required): 当前调用接口的调用者对应userId。 **[!NOTE]** 用于数据审计，需填写当前组织下真实的员工userId，否则接口调用会失败。
- optional: fields(Array of String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-orgaccountmobilevisibleinotherorg
updated_at: 2026-06-01 16:06:13
