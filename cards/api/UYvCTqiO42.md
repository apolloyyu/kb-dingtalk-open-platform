# 获取节点列表

doc_id: UYvCTqiO42
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/wiki/nodes
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Node.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- parentNodeId (String, required): 父节点id(父节点dentryUuid)，可通过调用获取知识库列表接口，获取返回参数`rootNodeId`字段。
- operatorId (String, required): 操作人unionId。
- optional: nextToken(String), maxResults(Integer), withPermissionRole(Boolean)

## Body
- none

## Returns
- optional: nodes(Array), nodeId(String), workspaceId(String), name(String), size(Long), type(String), category(String), extension(String), url(String), creatorId(String), modifierId(String), createTime(String), modifiedTime(String), hasChildren(Boolean), statisticalInfo(Object), wordCount(Long), permissionRole(String), createTimestamp(Long), modifiedTimestamp(Long), nextToken(String)

## Limits
- 分页大小，默认值50。 最大值50。
- 节点列表，最大size50。

source_url: https://open.dingtalk.com/document/development/get-node-list
updated_at: 2026-07-15 09:29:06
