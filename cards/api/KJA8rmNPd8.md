# 根据迁移后的dingId查询原dingId

doc_id: KJA8rmNPd8
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccount/getDingIdByMigrationDingIds
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.OrgAccountMigration.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- migrationDingId (String, required): 迁移后企业账号的dingId。

## Body
- none

## Returns
- optional: dingId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-original-dingid-based-on-the-dingid-after-migration
updated_at: 2026-06-01 15:42:26
