# 更新浮动图片

doc_id: IIigj1plTo
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/floatImages/{id}
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或标题，可调用获取所有工作表接口获取id和工作表的标题。
- id (String, required): 指定浮动图片 id，可通过「查询浮动图片」接口进行获取。

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 **[!NOTE]** 若操作人无权限，接口会报错 `The operator has no permission`。

## Body
- optional: src(String), anchor(Object), row(Integer), col(Integer), coordinate(Object), width(double), height(double), offsetX(double), offsetY(double)

## Returns
- optional: result(Object), id(String), src(String), anchor(Object), row(Integer), col(Integer), coordinate(Object), width(double), height(double), offsetX(double), offsetY(double), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-updatefloatimage
updated_at: 2026-06-02 18:43:37
