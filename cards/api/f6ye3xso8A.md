# 删除知识库文档

doc_id: f6ye3xso8A
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/doc/workspaces/{workspaceId}/docs/{nodeId}
api_version: v2-new
app_types: 企业内部应用
permissions: Document.WorkspaceDocument.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证， 可调用获取企业内部应用的accessToken接口获取。

## Path params
- workspaceId (String, required): 团队空间ID，可调用新建知识库接口或者获取知识库列表接口获取的workspaceId字段值。
- nodeId (String, required): 团队空间节点ID，可以传文档ID或者文件夹ID，可通过创建知识库文档接口获取nodeId参数值。

## Query params
- operatorId (String, required): 发起删除请求的用户用户的unionId，可通过查询用户详情接口获取unionid参数值。

## Body
- none

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-team-space-documents
updated_at: 2026-06-03 10:13:09
