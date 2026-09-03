# 更新筛选视图

doc_id: o0dzjvj9CI
completeness: full
archived: false
method: PATCH
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/filterViews/{filterViewId}
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或名称，可调用获取所有工作表接口获取id或name参数值。
- filterViewId (String, required): 筛选视图的 ID。

## Query params
- operatorId (String, required): 操作人的unionId。 - 可通过通过免登码获取用户信息接口获取unionid参数值。 - 可调用查询用户详情接口获取unionid参数值。 若操作人无权限，接口会报错`The operator has no permission`。

## Body
- optional: name(String), range(String), criteria(Map<String, Object>), filterType(String), visibleValues(Array of String), conditions(Array), operator(String), value(String), conditionOperator(String), backgroundColor(String), fontColor(String)

## Returns
- optional: id(String), name(String), range(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-updatefilterview
updated_at: 2026-06-04 19:09:22
