# 指定列左侧插入若干列

doc_id: udX907NsFi
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/insertColumnsBefore
api_version: v2-new
app_types: 第三方企业应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表的ID或标题。 - 企业内部应用，可调用获取所有工作表接口获取id或者传工作表的标题。 - 第三方企业应用，建议传递工作表的标题。 工作表的标题查看步骤如下图。

## Query params
- operatorId (String, required): 操作人unionId，可调用查询用户详情接口获取。

## Body
- column (Long, required): 指定列的游标，从0开始。
- columnCount (Long, required): 插入列的数量。

## Returns
- optional: id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/insert-column-before-column
updated_at: 2026-06-04 19:09:11
