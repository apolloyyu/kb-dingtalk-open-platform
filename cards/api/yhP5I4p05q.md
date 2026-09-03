# 获取我的文档知识库信息

doc_id: yhP5I4p05q
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/wiki/mineWorkspaces
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Workspace.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- operatorId (String, required): 操作人unionId。

## Body
- none

## Returns
- optional: workspace(Object), workspaceId(String), corpId(String), teamId(String), rootNodeId(String), name(String), type(String), description(String), url(String), icon(Object), value(String), cover(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), permissionRole(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-my-documents
updated_at: 2026-06-02 17:37:12
