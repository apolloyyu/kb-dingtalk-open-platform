---
title: "读写钉钉文档模型"
source_url: "https://open.dingtalk.com/document/development/dingtalk-document-model"
namespace: "development"
slug: "dingtalk-document-model"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 脚本服务 > 读写钉钉文档模型"
doc_id: "234xBKZzn2"
updated_at: "2026-08-28 10:26:29"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-document-model
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 脚本服务 > 读写钉钉文档模型
> Updated: 2026-08-28 10:26:29

# 读写钉钉文档模型

本文通过调用**DingdocsScript.workbook**访问钉钉表格模型，实现钉钉文档读写。

## **准备工作**

读写钉钉文档模型需依赖[dingtalk-docs-cool-app](https://www.npmjs.com/package/dingtalk-docs-cool-app)，请先升级到最新版本。

```
npm install dingtalk-docs-cool-app --save
```

## **API使用说明**

> **[!NOTE]**
>
> 建议钉钉版本使用最新版本。

| **客户端** | **Android** | **IOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

在在脚本函数js文件中，开发者可调用**DingdocsScript.workbook**访问钉钉表格对象模型。

```
function insertSheet() {
  const sheet = DingdocsScript.workbook.insertSheet();
  sheet.activate();
}
```

## **如何读写钉钉表格对象模型**

当需要对文档执行某个具体的操作时，应当首先获取到表格的对象模型，然后调用对象上的具体方法。

调用DingdocsScript.workbook可访问钉钉表格文档模型的顶级对象Workbook，代表当前打开的表格文档。调用JSAPI读写表格数据时，通常从Workbook开始。

## 常用对象

如下图所示，根据表格的数据对象模型，将API进行了对象划分。常用的对象有：

- **Workbook**：工作簿。包含多个工作表，Workbook为顶级对象，可以直接通过调用DingdocsScript.workbook获取。
- **Sheet**：工作表。包含单元格和单元格区域，要获取Sheet对象，可以使用 Workbook.getSheet('Sheet1') 方法，其中Sheet1为工作表名称。
- **Range**：单个选区。包含单个或者多个单元格，要获取Range对象，可以使用Workbook.getRange('A1:B1')方法， 获取当前工作表上的A1:B1选区；或者也可以使用sheet.getRange('A1:B1') 获取特定工作表上的A1:B1选区。
- **RangeList**：多个选区。包含多个区域，要获取RangeList对象，可以使用Workbook.getRangeList(['A1:B1', 'C2:D2']) 方法来获取当前工作表上的A1:B1和C1:D2选区。同样的，在sheet上也可以调用类似的API来获取特定工作表上的选区。![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/w5VLqXj14kWxlX19/img/2f11b2ed-a0c2-408b-a182-ff6b080ed65d.png)

## 基本使用方式

首先需要确定要操作的对象，再调该对象上的API。

例如，需要设置一个区域内所有单元格的背景色，那么操作对象就是Range，首先获取到Range，再调用Range对象中的setBackgroundColor API。

```
// 获取当前的 sheet
const sheet = Workbook.getActiveSheet();
// 获取选区 A1
const range = sheet.getRange('A1');
// 设置选区 A1 的背景色
range.setBackgroundColor('#ffff00');
```

更多钉钉表格对象模型API，请参见[钉钉表格对象模型API参考文档](0297-workbook.md)。
