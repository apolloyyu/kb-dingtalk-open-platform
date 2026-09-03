# 批量获取节点

doc_id: dZQb9gesUb
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/wiki/nodes/batchQuery
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Node.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- operatorId (String, required): 操作人unionId。

## Body
- nodeIds (Array of String, required): 节点id。 最大size20。
- optional: option(Object), withStatisticalInfo(Boolean), withPermissionRole(Boolean)

## Returns
- optional: nodes(Array), nodeId(String), workspaceId(String), name(String), size(Long), type(String), category(String), extension(String), url(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), hasChildren(Boolean), statisticalInfo(Object), wordCount(Long), permissionRole(String), createTimestamp(Long), modifiedTimestamp(Long)

## Limits
- 节点id。 最大size20。

source_url: https://open.dingtalk.com/document/development/obtain-nodes-in-batch
updated_at: 2026-07-15 09:30:13
