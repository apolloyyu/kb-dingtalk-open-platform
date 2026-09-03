# 创建工作表

doc_id: 97be9xkSfY
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets
api_version: v2-new
app_types: 第三方企业应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 若操作人无权限，接口会报错`The operator has no permission`。

## Body
- name (String, required): 工作表的名称。 当指定的工作表名称和已有的工作表名称重复时，将自动重命名为合法值。

## Returns
- optional: visibility(String), name(String), id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-worksheet
updated_at: 2026-06-04 19:09:05
