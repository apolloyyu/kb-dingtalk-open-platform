# 批量设置行高

doc_id: kVI0JeDiOI
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/setRowsHeight
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或标题，可调用获取所有工作表接口获取id和工作表的标题。

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 **[!NOTE]** 若操作人无权限，接口会报错 `The operator has no permission`。

## Body
- row (Long, required): 要修改行高的第一行的游标，从0开始。
- rowCount (Long, required): 要修改行高的连续行数。
- height (Long, required): 高度，单位：像素。

## Returns
- optional: sheetId(String), sheetName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-setrowsheight
updated_at: 2026-06-02 18:40:02
