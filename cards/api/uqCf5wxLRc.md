# 查找所有符合条件的单元格

doc_id: uqCf5wxLRc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/findAll
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或标题，可调用获取所有工作表接口获取id和工作表的标题。

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 若操作人无权限，接口会报错 `The operator has no permission`。
- optional: select(String)

## Body
- text (String, required): 要查找的文本。 如果开启了 **useRegExp**，则为正则模式，示例："\\d+"
- findOptions (Object, required): 查找选项。
- unionCells (Boolean, required): 是否对找到的单元格地址做聚合。建议进行聚合，否则可能返回大量地址。可选值： - **true**：是 - **false**：否（默认值）
- optional: matchEntireCell(Boolean), matchCase(Boolean), useRegExp(Boolean), matchFormulaText(Boolean), scope(String), includeHidden(Boolean)

## Returns
- optional: value(Array), a1Notation(String), values(Array)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/find-all-matching-cells
updated_at: 2026-06-04 19:09:15
