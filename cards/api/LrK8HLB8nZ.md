# 获取节点

doc_id: LrK8HLB8nZ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/wiki/nodes/{nodeId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Node.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- nodeId (String, required): 节点id(节点dentryUuid)，可通过调用获取节点列表接口，获取返回参数`nodeId`字段。

## Query params
- operatorId (String, required): 操作人unionId。
- optional: withStatisticalInfo(Boolean), withPermissionRole(Boolean)

## Body
- none

## Returns
- optional: node(Object), nodeId(String), workspaceId(String), name(String), size(Long), type(String), category(String), extension(String), url(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), hasChildren(Boolean), statisticalInfo(Object), wordCount(Long), permissionRole(String), createTimestamp(Long), modifiedTimestamp(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-knowledge-base-acquisition-node
updated_at: 2026-07-15 09:31:02
