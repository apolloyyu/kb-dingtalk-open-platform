# 筛选排序

doc_id: lmwIbIHrNM
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/filter/sort
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或名称，可调用获取所有工作表接口获取id或name参数值。

## Query params
- operatorId (String, required): 操作人的unionId。 - 可通过通过免登码获取用户信息接口获取unionid参数值。 - 可调用查询用户详情接口获取unionid参数值。 若操作人无权限，接口会报错`The operator has no permission`。

## Body
- field (Object, required): 排序规则对象。
- column (Long, required): 列偏移量，相对于筛选范围首列，从 0 开始。
- optional: ascending(Boolean)

## Returns
- optional: id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-sortfilter
updated_at: 2026-06-04 19:09:19
