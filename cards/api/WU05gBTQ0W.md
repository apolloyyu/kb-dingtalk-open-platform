# 获取筛选视图列表

doc_id: WU05gBTQ0W
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/filterViews
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或名称，可调用获取所有工作表接口获取id或name参数值。 **[!NOTE]** 若工作表上没有筛选视图，接口将返回空数组。

## Query params
- operatorId (String, required): 操作人的unionId。 - 可通过通过免登码获取用户信息接口获取unionid参数值。 - 可调用查询用户详情接口获取unionid参数值。 若操作人无权限，接口会报错`The operator has no permission`。

## Body
- none

## Returns
- optional: filterViews(Array), id(String), name(String), range(String), criteria(Map<String, Object>), filterType(String), visibleValues(Array of String), conditions(Array), operator(String), value(String), conditionOperator(String), backgroundColor(String), fontColor(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getfilterviews
updated_at: 2026-06-04 19:09:23
