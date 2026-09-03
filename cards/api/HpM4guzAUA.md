# 置顶知识库

doc_id: HpM4guzAUA
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/doc/spaces/{spaceId}/pin
api_version: v2-new
app_types: 第三方企业应用
permissions: Document.Workspace.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 知识库 。

## Query params
- operatorId (String, required): 操作人 UnionID。

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-pinspace
updated_at: 2026-06-02 17:37:09
