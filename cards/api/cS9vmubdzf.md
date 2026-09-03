# 创建知识库文档

doc_id: cS9vmubdzf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workspaces/{workspaceId}/docs
api_version: v2-new
app_types: 第三方企业应用
permissions: Document.WorkspaceDocument.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- workspaceId (String, required): 知识库ID，调用新建知识库接口或者获取知识库列表接口获取的workspaceId字段值。

## Query params
- none

## Body
- name (String, required): 文档名称。
- docType (String, required): 文档类型，取值： - **DOC**：文字 - **WORKBOOK**：表格 - **MIND**：脑图 - **FOLDER**：文件夹
- operatorId (String, required): 用户的unionId，可调用查询用户详情接口获取。
- optional: parentNodeId(String), templateId(String), templateType(String)

## Returns
- optional: workspaceId(String), nodeId(String), docKey(String), url(String), dentryUuid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-team-space-document
updated_at: 2026-06-03 10:13:09
