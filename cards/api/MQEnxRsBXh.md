# 根据迁移后的unionId查询原unionId

doc_id: MQEnxRsBXh
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccount/getUnionIdByMigrationUnionIds
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.OrgAccountMigration.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- migrationUnionId (String, required): 迁移后企业账号的unionId，可调用查询企业账号用户详情接口获得unionid参数值。

## Body
- none

## Returns
- optional: unionId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-the-original-union-id-based-on-the-union-id
updated_at: 2026-06-01 15:43:34
