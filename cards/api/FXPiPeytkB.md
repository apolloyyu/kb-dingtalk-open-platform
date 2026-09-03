# 获取所有工作表

doc_id: FXPiPeytkB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。

## Query params
- operatorId (String, required): 操作人的unionId。 - 可通过通过免登码获取用户信息接口获取unionid参数值。 - 可调用查询用户详情接口获取unionid参数值。 若操作人无权限，接口会报错`The operator has no permission`。

## Body
- none

## Returns
- optional: value(Array), id(String), name(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-all-worksheets
updated_at: 2026-06-04 19:09:07
