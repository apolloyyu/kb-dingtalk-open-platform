---
title: "数据说明"
source_url: "https://open.dingtalk.com/document/development/data-structure"
namespace: "development"
slug: "data-structure"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "AI 表格 > 数据说明"
doc_id: "TENNGcaoA4"
updated_at: "2026-05-15 09:05:06"
---

> Source: https://open.dingtalk.com/document/development/data-structure
> Path: 应用开发 / 服务端 API / AI 表格 > 数据说明
> Updated: 2026-05-15 09:05:06

# 数据说明

## **数据结构**

AI表格中包含如下基本结构：

- Base，即一篇AI表格文档

  - `baseId`唯一标识了一篇AI表格文档。`baseId`可以通过以下方法获取。

    | **通过URL获取**  image.png | **通过文档信息面板获取**  imageimage | **通过其它API获取**  - 可通过[获取节点列表](0571-get-node-list.md)接口获取。 **[!NOTE]**  创建AI表格时，`docType`值为`BASE`。 |
    | --- | --- | --- |
- Sheet（即数据表），一篇AI表格文档中通常有多个数据表，且至少有一个数据表。

  - 所有需要访问sheet的接口都可以使用`sheetId`或`sheetName`作为入参。
  - sheetId可以通过[获取所有数据表](0461-api-notable-getallsheets.md)接口获取。

    > **[!NOTE]**
    >
    > sheetId仅保证在文档中唯一，不保证全局唯一。
  - sheetName为前端可见的sheet名称，如下图中的`任务管理`。
- Field（即字段），数据表中的每一列即是一个字段，一个数据表中通常有多个字段。

  - 所有需要访问field的接口都可以使用`fieldId`或`fieldName`作为入参。
  - fieldId可以通过[获取所有字段](0466-api-noatable-getallfields.md)接口获取。

    > **[!NOTE]**
    >
    > fieldId仅保证在文档中唯一，不保证全局唯一。
  - fieldName为前端可见的field名称，如下图中的`重要程度`。
  - 每个sheet的第一列为「主字段」，其仅支持特定几种字段类型，且该列不可删除。具体支持的字段类型使用如下方法查看

    - 打开任意AI表格
    - 编辑主字段
    - 查看可设置的字段类型
- Record（即记录），数据表中的每一行即是一个记录，一个数据表中通常有多个记录。

  - 所有需要访问record接口需要使用`recordId`。
  - recordId可以通过[新增记录](0468-api-notable-insertrecords.md)或[列出多行记录](0470-api-notable-listrecords.md)等接口获取。

    > **[!NOTE]**
    >
    > recordId仅保证在文档中唯一，不保证全局唯一。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2556362571/p979051.png)

## **字段属性**

字段属性区域，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9856362571/p979045.png)

不同字段类型所支持的属性请参考下表：

| **字段名** | **类型 (type)** | **属性 (property)** |
| --- | --- | --- |
| 文本 | text | 无 |
| 数字 | number | ``` {     formatter: "INT"        // 整数         | "FLOAT_1"         // 保留1位小数         | "FLOAT_2"         // 保留2位小数         | "FLOAT_3"         // 保留3位小数         | "FLOAT_4"         // 保留4位小数         | "THOUSAND"        // 千分位         | "THOUSAND_FLOAT"  // 千分位（小数点）         | "PERCENT"         // 百分比         | "PERCENT_FLOAT"   // 百分比（小数点） } ``` |
| 货币 | currency | ``` {   currencyType: 'CNY' | 'HKD' | 'USD' | 'EUR' | 'GBP' | 'MOP' | 'VND' | 'JPY' | 'KRW' | 'AED' | 'AUD' | 'BRL' | 'CAD' | 'CHF' | 'INR' | 'IDR' | 'MXN' | 'MYR' | 'PHP' | 'PLN' | 'RUB' | 'SGD' | 'THB' | 'TRY' | 'TWD';   formatter: "INT"        // 整数     | "FLOAT_1"         // 保留1位小数     | "FLOAT_2"         // 保留2位小数     | "FLOAT_3"         // 保留3位小数     | "FLOAT_4"         // 保留4位小数 } ``` |
| 单选 | singleSelect | ``` {     choices: [{         name: "optionName1" // 配置选项名     }, {         name: "optionName2"     }]; } ``` |
| 多选 | multipleSelect | 同「单选」 |
| 日期 | date | ``` {     formatter: "YYYY-MM-DD"    // 显示格式: 2023-12-31         | "YYYY-MM-DD HH:mm"   // 显示格式: 2023-12-31 09:00         | "YYYY/MM/DD"         // 显示格式: 2023/12/31         | "YYYY/MM/DD HH:mm";  // 显示格式: 2023/12/31 09:00 } ``` |
| 人员 | user | ``` {   multiple: boolean; // 支持多选，默认为true } ``` |
| 部门 | department | ``` {   multiple: boolean; // 支持多选，默认为true } ``` |
| 附件 | attachment | 无 |
| 单向关联 | unidirectionalLink | ``` {   multiple: boolean; // 支持多选，默认为true   linkedSheetId: "xxx" // 关联的数据表ID } ``` |
| 双向关联 | bidirectionalLink | ``` {   multiple: boolean; // 支持多选，默认为true   linkedSheetId: "xxx", // 关联的数据表ID   linkedFieldId: "yyy" // 关联的数据表上的字段ID，创建字段时不传 } ``` |
| 链接 | url | 无 |

## **记录值格式**

记录值（又称字段值）展示，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8956362571/p979046.png)

不同字段类型所使用的格式请参考下表：

| **字段名** | **类型 (type)** | **设置值（新增/更新记录时使用的格式）** | **返回值（返回记录值时返回的格式）** |
| --- | --- | --- | --- |
| 文本 | text | ``` "TextString" // 字符串 ``` | ``` "TextString" // 字符串 ``` |
| 数字 | number | ``` 123 // 支持整数/浮点数/字符串 ``` | ``` "123" // 数字值，以字符串形式返回 ``` |
| 货币 | currency | ``` 123 // 支持整数/浮点数/字符串 ``` | ``` "123" // 数字值，以字符串形式返回 ``` |
| 单选 | singleSelect | ``` "optionName1" // 单选选项名 ``` | ``` {   "id": "id", // 选项ID   "name": "optionName1" // 选项名 } ``` |
| 多选 | multipleSelect | ``` ["optionName1", "optionName2"] // 多选选项名 ``` | ``` [   {     "id": "id1", // 选项ID     "name": "optionName1" // 选项名   },   {     "id": "id2", // 选项ID     "name": "optionName2" // 选项名   } ] ``` |
| 日期 | date | ``` 1688601600000 // 时间戳 "2023-12-20 03:00" // 或者 ISO 8601字符串 ``` | ``` 1688601600000 // 时间戳 ``` |
| 人员 | user | ``` [   {     unionId: "xxx"   } ] ``` | ``` [   {     unionId: "xxx"   } ] ``` |
| 部门 | department | ``` [   {     deptId: "xxx"   } ] ``` | ``` [   {     deptId: "xxx"   } ] ``` |
| 附件 | attachment | 具体请参考[上传附件](0458-upload-attachment.md)。 | ``` [   {     "filename": "image.xlsx",     "size": 92250,     "type": "xls",     "url": "xxx"   } ] ```   **[!NOTE]**  url是附件访问链接。   - 当附件是在线文档时，其是在线文档链接，该链接没有访问时效。 - 当附件是其它文件时，是一个有**访问时效**的下载链接，一段时间后该链接将无法访问。 |
| 单向关联 | unidirectionalLink | ``` {     "linkedRecordIds": [         "xxx",         "yyy"     ] } ``` | ``` {     "linkedRecordIds": [         "xxx",         "yyy"     ] } ```   **[!NOTE]**  field property中包含关联的sheetId，配合这里返回的recordId，可以通过调用[获取记录](0469-api-getrecord.md)接口去获取关联记录的值。 |
| 双向关联 | bidirectionalLink | ``` {     "linkedRecordIds": [         "xxx",         "yyy"     ] } ``` | ``` {     "linkedRecordIds": [         "xxx",         "yyy"     ] } ``` |
| 链接 | url | ``` {   "text": "Dingtalk",   "link": "https://dingtalk.com" } ``` | ``` {   "text": "Dingtalk",   "link": "https://dingtalk.com" } ``` |
