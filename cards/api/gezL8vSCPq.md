# 获取 dentryUuid 信息

doc_id: gezL8vSCPq
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/doc/dentries/{dentryId}/queryDentryUuid
api_version: v2-new
app_types: 第三方企业应用
permissions: Document.WorkspaceDocument.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用可调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用可调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- dentryId (String, required): 当前文件的 ID。

## Query params
- spaceId (String, required): 空间 ID。
- operatorId (String, required): 操作人 unionId，调用查询用户详情接口获取 unionid 参数值。

## Body
- none

## Returns
- optional: dentryUuid(String), dentryId(String), spaceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getuuidbydentryid
updated_at: 2026-06-02 18:49:02
