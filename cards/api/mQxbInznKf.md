# 工作表中追加行

doc_id: mQxbInznKf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/appendRows
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID，传递`nodeId`（dentryUuid）即表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表的ID或标题，可调用获取所有工作表接口获取或填写工作表的标题。

## Query params
- operatorId (String, required): 操作人的unionId，可通过免登码获取用户信息或根据userId获取用户详情接口两种方式获取。

## Body
- values (Array of Array, required): 要追加的数据列表。

## Returns
- optional: a1Notation(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/append-line
updated_at: 2026-06-04 19:09:09
