# 更新单元格区域

doc_id: 3nr9isYFnd
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress}
api_version: v2-new
app_types: 第三方企业应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过以下方式获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或名称。 - 企业内部应用，可调用获取所有工作表接口获取id或name参数值。 - 第三方企业应用，可调用创建工作表接口获取id和name。
- rangeAddress (String, required): Range地址。

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 若操作人无权限，接口会报错 `The operator has no permission`。

## Body
- optional: horizontalAlignments(Array of Array), numberFormat(String), wordWrap(String), values(Array of Array), complexValues(Array of Array), backgroundColors(Array of Array), fontColors(Array of Array), fontSizes(Array of Array), fontWeights(Array of Array), hyperlinks(Array of Array), verticalAlignments(Array of Array)

## Returns
- optional: a1Notation(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-cell-properties
updated_at: 2026-06-04 19:09:15
