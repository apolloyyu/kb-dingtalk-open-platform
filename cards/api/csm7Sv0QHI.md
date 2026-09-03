# 删除工作表

doc_id: csm7Sv0QHI
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或名称。 - 企业内部应用，可调用获取所有工作表接口获取id或name参数值。 - 第三方企业应用，可调用创建工作表接口获取id和name。

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 若操作人无权限，接口会报错`The operator has no permission`。

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-classic-workbooks
updated_at: 2026-06-04 19:09:06
