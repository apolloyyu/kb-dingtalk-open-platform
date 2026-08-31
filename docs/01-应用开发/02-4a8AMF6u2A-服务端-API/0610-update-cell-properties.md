---
title: "更新单元格区域"
source_url: "https://open.dingtalk.com/document/development/update-cell-properties"
namespace: "development"
slug: "update-cell-properties"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 单元格区域 > 更新单元格区域"
doc_id: "3nr9isYFnd"
updated_at: "2026-06-04 19:09:15"
---

> Source: https://open.dingtalk.com/document/development/update-cell-properties
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 单元格区域 > 更新单元格区域
> Updated: 2026-06-04 19:09:15

# 更新单元格区域

调用本接口，更新单元格信息，包括单元格中的值、背景色、超链接、字体大小、水平对齐方式、垂直对齐方式等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress} |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Document.Workbook.Write-钉钉表格写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过以下方式获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](0553-knowledge-base-overview.md) 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用[获取节点](https://open.dingtalk.com/document/development/get-node)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |
| sheetId | String | 是 | 工作表ID或名称。   - 企业内部应用，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id或name参数值。 - 第三方企业应用，可调用[创建工作表](0591-create-a-worksheet.md)接口获取id和name。 |
| rangeAddress | String | 是 | Range地址。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。      若操作人无权限，接口会报错 `The operator has no permission`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| horizontalAlignments | Array of Array | 否 | 水平对齐方式，可选值：为'left'-左对齐、'center'-居中对齐、'right'-右对齐、'general'-默认对齐方式。  根据Range地址范围传参，格式为二维数组。详情请参考如下示例：      Range地址范围有几行，该参数二维数组内就有几个元素；Range地址范围内有几列，该参数二维数组每个元素内就有几个值。    **示例1**：Range地址为A1:B3，范围内是一个三行两列的表格，该参数值格式如下：   ``` {     "horizontalAlignments": [         ["left", "general"],         ["center", "general"],         ["right", "general"]     ] } ```   **示例2**：Range地址为A1:C3，范围内是一个三行三列的表格，该参数值格式如下：   ``` {     "horizontalAlignments": [         ["left", “left”, "general"],         ["center", "center", "general"],         ["right", "right", "general"]     ] } ``` |
| numberFormat | String | 否 | 数字格式。   | 名称 | 数字格式 | 示例 | | --- | --- | --- | | 常规 | "General" |  | | 文本 | "@" |  | | 数字 | "#,##0" | 1,234 | | 数字（小数点） | "#,##0.00" | 1,234.56 | | 百分数 | "0%" | 12% | | 百分数（小数点） | "0.00%" | 12.34% | | 科学计数 | "0.00E+00" | 1.01E+03 | | 人民币 | "¥#,##0" | ¥1,234 | | 人民币（小数点） | ¥#,##0.00" | ¥1,234.56 | | 美元 | "$#,##0" | $1,234 | | 美元（小数点） | "$#,##0.00" | $1,234.56 | | 日期 | "yyyy/m/d" | 2022/1/1 | | 日期（中文） | "yyyy年m月d日" | 2022年1月1日 | | 日期（中文年月） | "yyyy年m月" | 2022年1月 | | 时间 | "hh:mm:ss" | 00:00:00 | | 日期时间 | "yyyy/m/d hh:mm:ss" | 2022/1/1 00:00:00 | |
| wordWrap | String | 否 | 换行方式，可选值：   - **overflow**：溢出 - **clip**：截断 - **autoWrap**：自动换行 |
| values | Array of Array | 否 | 单元格的值，根据Range地址范围传参，格式为二维数组。详情请参考如下示例：      Range地址范围有几行，该参数二维数组内就有几个元素；Range地址范围内有几列，该参数二维数组每个元素内就有几个值。    **示例1**：Range地址为A1:B3，范围内是一个三行两列的表格，该参数值格式如下：   ``` {     "values": [         ["1", "2"],         ["3", "4"],         ["5", "6"]     ] } ```   **示例2**：Range地址为A1:C3，范围内是一个三行三列的表格，该参数值格式如下：   ``` {     "values": [         ["1","2","3"],         ["4","5","6"],         ["7","8","9"]     ] } ``` |
| complexValues | Array of Array | 否 | 单元格的值，根据Range地址范围传参，格式为二维数组。  可通过该字段，给对应单元格填入「富文本格式」的内容，详见后续附录。 |
| backgroundColors | Array of Array | 否 | 背景色，颜色的16进制值，根据Range地址范围传参，格式为二维数组。详情请参考如下示例：      Range地址范围有几行，该参数二维数组内就有几个元素；Range地址范围内有几列，该参数二维数组每个元素内就有几个值。    **示例1**：Range地址为A1:B3，范围内是一个三行两列的表格，该参数值格式如下：   ``` {     "backgroundColors": [         ["#ff0000", "#00ff00"],         ["#f0f0f0", "#0000ff"],         ["#f0f0f0", "#0000ff"]     ] } ```   **示例2**：Range地址为A1:C3，范围内是一个三行三列的表格，该参数值格式如下：   ``` {     "backgroundColors": [         ["#ff0000","#ff0000","#ff0000"],         ["#ff0000","#ff0000","#ff0000"],         ["#ff0000","#ff0000","#ff0000"]     ] } ``` |
| fontColors | Array of Array | 否 | 字体颜色，颜色的16进制值，根据Range地址范围传参，格式为二维数组。 |
| fontSizes | Array of Array | 否 | 字体大小，根据Range地址范围传参，格式为二维数组。详情请参考如下示例：      Range地址范围有几行，该参数二维数组内就有几个元素；Range地址范围内有几列，该参数二维数组每个元素内就有几个值。    **示例1**：Range地址为A1:B3，范围内是一个三行两列的表格，该参数值格式如下：   ``` {     "fontSizes": [         [14, 14],         [15, 15],         [10, 10]     ] } ```   **示例2**：Range地址为A1:C3，范围内是一个三行三列的表格，该参数值格式如下：   ``` {     "fontSizes": [         [14, 14, 14],          [15, 15, 15],          [10, 10, 10]     ] } ``` |
| fontWeights | Array of Array | 否 | 字体粗细，可选值：   - **bold**：加粗 - **normal**：正常 |
| hyperlinks | Array of Array | 否 | 超链接，根据Range地址范围传参，格式为二维数组。详情请参考如下示例：      Range地址范围有几行，该参数二维数组内就有几个元素；Range地址范围内有几列，该参数二维数组每个元素内就有几个值。    **示例1**：Range地址为A1:B3，范围内是一个三行两列的表格，该参数值格式如下：   ``` {     "hyperlinks": [         [             {                 "type": "path",                 "link": "https://www.dingtalk.com",                 "text": "test"             },             {                 "type": "sheet",                 "link": "Sheet2",                 "text": "测试"             }        ],         [             {                 "type": "range",                 "link": "Sheet2!A4",                 "text": "test"             },             {                 "type": "path",                 "link": "https://www.dingtalk.com",                 "text": "测试"             }        ],         [             {                 "type": "range",                 "link": "Sheet2!A4",                 "text": "2"             },             {                 "type": "sheet",                 "link": "Sheet2",                 "text": "测试"             }         ]     ] } ```   **示例2**：Range地址为A1:C3，范围内是一个三行三列的表格，该参数值格式如下：   ``` {   "hyperlinks": [         [             {                 "type": "path",                 "link": "https://www.dingtalk.com",                 "text": "test"             },             {                 "type": "sheet",                 "link": "Sheet2",                 "text": "测试"             },{                 "type": "path",                 "link": "https://www.dingtalk.com",                 "text": "test"             }         ],         [             {                 "type": "range",                 "link": "Sheet2!A4",                 "text": "test"             },             {                 "type": "path",                 "link": "https://www.dingtalk.com",                 "text": "测试"             },{                 "type": "path",                 "link": "https://www.dingtalk.com",                 "text": "test"             }         ],         [             {                 "type": "range",                 "link": "Sheet2!A4",                 "text": "2"             },             {                 "type": "sheet",                 "link": "Sheet2",                 "text": "测试"             },{                 "type": "path",                 "link": "https://www.dingtalk.com",                 "text": "test"             }         ]     ] } ``` |
| verticalAlignments | Array of Array | 否 | 垂直对齐方式，可选值：为'top'-顶部对齐、'middle'-垂直居中、'bottom'-底部对齐。  根据Range地址范围传参，格式为二维数组。详情请参考如下示例：      Range地址范围有几行，该参数二维数组内就有几个元素；Range地址范围内有几列，该参数二维数组每个元素内就有几个值。    **示例1**：Range地址为A1:B3，范围内是一个三行两列的表格，该参数值格式如下：   ``` {     "verticalAlignments": [         ["top", "top"],         ["middle", "middle"],         ["bottom", "bottom"]     ] } ```   **示例2**：Range地址为A1:C3，范围内是一个三行三列的表格，该参数值格式如下：   ``` {     "verticalAlignments": [         ["top", "top", "top"],         ["middle", "middle", "middle"],         ["bottom", "bottom", "bottom"]     ] } ``` |

### 请求示例

HTTP

```
PUT /v1.0/doc/workbooks/e54Lqxxxxx/sheets/Sheet1/ranges/A1:B1?operatorId=ppgAQuxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f86e0bxxx
Content-Type:application/json

{
  "horizontalAlignments" : [ [ "general" ] ],
  "numberFormat" : "@",
  "wordWrap" : "autoWrap",
  "values" : [ [ "text" ] ],
  "complexValues" : [ [ "text" ] ],
  "backgroundColors" : [ [ "#ff0000" ] ],
  "fontColors" : [ [ "#000000" ] ],
  "fontSizes" : [ [ 14 ] ],
  "fontWeights" : [ [ "bold" ] ],
  "hyperlinks" : [ [ {
    "type" : "path",
    "link" : "https://www.dingtalk.com",
    "text" : "DingTalk"
  } ] ],
  "verticalAlignments" : [ [ "middle" ] ]
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| a1Notation | String | 被更新的range地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "a1Notation" : "A1"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.resource.notWorkbook | %s | 不支持的文档类型，请检查workbookId。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
