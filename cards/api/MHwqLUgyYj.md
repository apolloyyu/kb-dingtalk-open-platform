# 创建筛选

doc_id: MHwqLUgyYj
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/createFilter
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
- range (String, required): 筛选范围，使用 A1 表示法。例如 `A1:D10` 表示从 A1 到 D10 的区域。筛选范围的第一行将作为标题行，不参与筛选计算。
- optional: criteria(Map<String, Object>), filterType(String), visibleValues(Array of String), conditions(Array), operator(String), value(String), conditionOperator(String), backgroundColor(String), fontColor(String)

## Returns
- optional: id(String)

## Limits
- 筛选条件数组，最多 2 个。仅当 `filterType` 为 `condition` 时需要传。
- - 每个工作表最多只能有一个全局筛选，若已存在筛选则会报错。

source_url: https://open.dingtalk.com/document/development/api-createfilter
updated_at: 2026-06-04 19:09:17
