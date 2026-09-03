# 查找工作表中的单元格

doc_id: fgJfZ6cq0d
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress}/findNext
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID，传递`nodeId`（dentryUuid）即表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表的ID或标题，可调用获取所有工作表接口获取id或者传工作表的标题。 image
- rangeAddress (String, required): 开始查找的起始位置，从该区域左上角的单元格开始（但并不包括该单元格）。

## Query params
- operatorId (String, required): 操作人unionId。

## Body
- text (String, required): 要查找的文本。
- optional: findOptions(Object), matchEntireCell(Boolean), matchCase(Boolean), useRegExp(Boolean), matchFormulaText(Boolean), scope(String), includeHidden(Boolean)

## Returns
- optional: a1Notation(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/find-the-next-eligible-cell
updated_at: 2026-06-03 16:43:35
