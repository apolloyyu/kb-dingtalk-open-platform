# 获取知识库列表

doc_id: BiEQAAaK3j
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/wiki/workspaces
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Workspace.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- operatorId (String, required): 操作人unionId，可通过调用查询用户详情接口获取。
- optional: nextToken(String), maxResults(Integer), orderBy(String), withPermissionRole(Boolean)

## Body
- none

## Returns
- optional: workspaces(Array), workspaceId(String), corpId(String), teamId(String), rootNodeId(String), name(String), type(String), description(String), url(String), icon(Object), value(String), cover(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), permissionRole(String), nextToken(String)

## Limits
- 分页大小，默认值30。 最大值30。
- 知识库列表，最大size30。

source_url: https://open.dingtalk.com/document/development/get-knowledge-base-list
updated_at: 2026-06-10 18:26:28
