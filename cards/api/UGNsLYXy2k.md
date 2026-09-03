# 设置筛选条件

doc_id: UGNsLYXy2k
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/filter/setColumnFilterCriteria
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
- column (Long, required): 列偏移量，相对于筛选范围首列，从 0 开始。例如筛选范围为 `B1:E10`，则 `column=0` 代表 B 列，`column=1` 代表 C 列。
- filterCriteria (Object, required): 筛选条件对象。
- filterType (String, required): 筛选类型。可选值： - **values**：按值筛选 - **color**：按颜色筛选 - **condition**：按条件筛选
- optional: visibleValues(Array of String), backgroundColor(String), fontColor(String), conditions(Array), operator(String), value(String), conditionOperator(String)

## Returns
- optional: id(String)

## Limits
- 按条件筛选时的条件列表，最多 2 个条件。当 `filterType` 为 `condition` 时必填。
- 多个条件之间的逻辑关系。取值： **and**：且（默认值） **or**：或。 当 `conditions` 包含 2 个条件时生效。

source_url: https://open.dingtalk.com/document/development/api-setfiltercriteria
updated_at: 2026-06-04 19:09:20
