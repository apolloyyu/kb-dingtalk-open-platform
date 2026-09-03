# 批量设置列宽

doc_id: gL9mRE5lOc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/setColumnsWidth
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
- column (Integer, required): 要修改列宽的第一列的游标，从0开始。
- width (Integer, required): 宽度，单位：像素。
- columnCount (Integer, required): 要修改列宽的连续列数。

## Returns
- optional: sheetId(String), sheetName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-setcolumnswidth
updated_at: 2026-06-02 18:39:26
