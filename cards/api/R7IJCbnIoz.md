# 新建知识库

doc_id: R7IJCbnIoz
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/wiki/workspaces
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Workspace.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- operatorId (String, required): 操作人unionId。

## Body
- name (String, required): 知识库名称。
- optional: option(Object), description(String), teamId(String)

## Returns
- optional: workspace(Object), workspaceId(String), corpId(String), teamId(String), rootNodeId(String), name(String), type(String), description(String), url(String), icon(Object), value(String), cover(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), permissionRole(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/new-knowledge-base
updated_at: 2026-06-02 17:37:08
