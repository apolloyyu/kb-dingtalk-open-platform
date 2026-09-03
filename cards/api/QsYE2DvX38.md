# 合并单元格

doc_id: QsYE2DvX38
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress}/merge
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的nodeId(dentryUuid)即是表格workbookId，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或标题，可调用获取所有工作表接口获取id和工作表的标题。
- rangeAddress (String, required): 需要合并的单元格范围，格式为`区域内左上角单元格:区域内右下角单元格`。 例如：B2:C3

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 若操作人无权限，接口会报错 `The operator has no permission`。

## Body
- optional: mergeType(String)

## Returns
- optional: a1Notation(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/merge-cells
updated_at: 2026-06-04 19:09:12
