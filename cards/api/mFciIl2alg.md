# 创建浮动图片

doc_id: mFciIl2alg
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/floatImages
api_version: v2-new
app_types: 企业内部应用
permissions: Document.Workbook.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- workbookId (String, required): 表格文件 ID ，知识库 API 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用获取节点和创建知识库文档接口获取。
- sheetId (String, required): 工作表ID或标题，可调用获取所有工作表接口获取id和工作表的标题。

## Query params
- operatorId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 **[!NOTE]** 若操作人无权限，接口会报错 `The operator has no permission`。

## Body
- src (String, required): 浮动图片资源地址，需要通过调用获取资源上传信息接口获得 `resourceUrl`。
- anchor (Object, required): 浮动图片定位信息。
- row (Integer, required): 相对第几行定位，游标从 0 开始。
- col (Integer, required): 相对第几列定位，游标从 0 开始。
- coordinate (Object, required): 设置几何信息。
- width (double, required): 指定图片宽度，单位：像素。
- height (double, required): 指定图片高度，单位：像素。
- offsetX (double, required): 相对定位坐标的横向偏移量，单位：像素。
- offsetY (double, required): 相对定位坐标的纵向偏移量，单位：像素。

## Returns
- optional: result(Object), id(String), src(String), anchor(Object), row(Integer), col(Integer), coordinate(Object), width(double), height(double), offsetX(double), offsetY(double), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-createfloatimage
updated_at: 2026-06-02 18:43:00
