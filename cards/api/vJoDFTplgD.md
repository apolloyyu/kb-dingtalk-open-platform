# 获取知识库

doc_id: vJoDFTplgD
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/wiki/workspaces/{workspaceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Workspace.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用可调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用可调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- workspaceId (String, required): 知识库id： - 企业内部应用，可通过调用获取知识库列表接口，获取返回参数`workspaceId`字段。 - 第三方企业应用，可通过调用获取知识库列表接口，获取返回参数`workspaceId`字段。

## Query params
- operatorId (String, required): 操作人unionId。
- optional: withPermissionRole(Boolean)

## Body
- none

## Returns
- optional: workspace(Object), workspaceId(String), corpId(String), teamId(String), rootNodeId(String), name(String), type(String), description(String), url(String), icon(Object), value(String), cover(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), permissionRole(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-knowledge-base
updated_at: 2026-06-02 17:37:09
