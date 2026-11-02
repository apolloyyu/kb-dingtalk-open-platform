---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-of-document-tables"
namespace: "development"
slug: "overview-of-document-tables"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 概述"
doc_id: "Wf2fe3H07n"
updated_at: "2026-05-15 18:19:01"
---

> Source: https://open.dingtalk.com/document/development/overview-of-document-tables
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 概述
> Updated: 2026-05-15 18:19:01

# 概述

钉钉表格 OpenAPI 提供了一套 RESTful 风格的接口，允许开发者通过程序化方式操作钉钉表格文档。你可以使用这些接口实现数据的自动化读写、工作表管理、单元格查找、区域锁定等功能，适用于数据同步、报表生成、自动化办公等场景。

## **开放概览**

钉钉表格 提供了丰富的开放API，开发者可自行根据业务进行选择。

### **工作表**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建工作表](0591-create-a-worksheet.md) | 在表格文档中创建一个新的工作表。 | 新版 |
| [删除工作表](0593-delete-classic-workbooks.md) | 删除表格内的某个工作表。 | 新版 |
| [获取工作表](0594-obtain-worksheet-properties.md) | 获取某个工作表属性。 | 新版 |
| [更新工作表](0592-update-worksheet.md) | 修改钉钉表格中指定工作表的元属性。 | 新版 |
| [获取所有工作表](0595-obtain-all-worksheets.md) | 获取指定表格中所有的工作表信息。 | 新版 |

### **行列**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [删除行](0596-delete-row.md) | 删除指定的行。 | 新版 |
| [删除列](0597-delete-column.md) | 删除指定的列。 | 新版 |
| [设置自动行高](0598-set-row-height-automatically.md) | 可根据指定的字体大小自动调整钉钉表格中指定行的行高，使内容完整显示。 | 新版 |
| [批量设置列宽](0599-api-setcolumnswidth.md) | 一次性设置钉钉表格中从指定列开始的连续多列的宽度。 | 新版 |
| [批量设置行高](0600-api-setrowsheight.md) | 一次性设置钉钉表格中从指定行开始的连续多行的高度。 | 新版 |
| [工作表中追加行](0601-append-line.md) | 在工作表的已有数据末尾追加若干行数据。 | 新版 |
| [设置行隐藏或显示](0602-set-row-visibility.md) | 设置行隐藏或者正常显示。 | 新版 |
| [设置列隐藏或显示](0603-set-column-visibility.md) | 设置列隐藏或者正常显示。 | 新版 |
| [指定行上方插入若干行](0604-insert-rows-before-rows.md) | 在指定的行上方插入若干行。 | 新版 |
| [指定列左侧插入若干列](0605-insert-column-before-column.md) | 在指定列左侧插入若干列。 | 新版 |

### **单元格区域**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [合并单元格](0606-merge-cells.md) | 将钉钉表格中指定区域内的多个单元格合并为一个整体。 | 新版 |
| [插入下拉列表](0607-insert-drop-down-list.md) | 为钉钉表格中指定单元格区域设置下拉列表选项。 | 新版 |
| [删除下拉列表](0608-delete-drop-down-list.md) | 移除钉钉表格中指定单元格区域上已设置的下拉列表配置。 | 新版 |
| [获取单元格区域](0609-get-cell-properties.md) | 获取单元格属性。 | 新版 |
| [更新单元格区域](0610-update-cell-properties.md) | 更新单元格信息。 | 新版 |
| [查找工作表中的单元格](0611-find-the-next-eligible-cell.md) | 根据指定的条件查找匹配给定字符串的下一个单元格。 | 新版 |
| [查找所有符合条件的单元格](0612-find-all-matching-cells.md) | 在指定工作表中搜索包含目标文本的单元格，并返回匹配单元格的位置列表。 | 新版 |
| [清除单元格区域内数据](0613-clear-cell-data.md) | 清除单元格区域内数据，不包括格式。 | 新版 |
| [清除单元格区域内所有内容](0614-clear-all.md) | 清除单元格区域内所有内容，包括格式。 | 新版 |

### **条件格式**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建条件格式规则](0615-create-conditional-formatting-rules.md) | 在钉钉表格的指定工作表中创建条件格式规则。 | 新版 |

### **筛选**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建筛选](0616-api-createfilter.md) | 在钉钉表格的指定工作表上创建全局筛选，并指定筛选范围。 | 新版 |
| [更新筛选](0617-api-updatefilter.md) | 一次性批量更新全局筛选中多列的筛选条件。 | 新版 |
| [删除筛选](0618-api-deletefilter.md) | 删除指定工作表上的全局筛选，使所有因筛选条件被隐藏的行恢复显示。 | 新版 |
| [获取筛选](0619-api-getfilter.md) | 查询指定工作表上当前生效的全局筛选信息。 | 新版 |
| [筛选排序](0620-api-sortfilter.md) | 对全局筛选范围内的数据按指定列进行升序或降序排序。 | 新版 |
| [设置筛选条件](0621-api-setfiltercriteria.md) | 为全局筛选中的指定列设置或更新筛选条件。 | 新版 |
| [删除筛选条件](0622-api-clearfiltercriteria.md) | 清除全局筛选中指定列的筛选条件，使该列不再参与筛选计算。 | 新版 |

### **筛选试图**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建筛选视图](0623-api-createfilterview.md) | 在钉钉表格的指定工作表上创建筛选视图，并指定视图名称和筛选范围。 | 新版 |
| [更新筛选视图](0624-api-updatefilterview.md) | 更新指定筛选视图的名称、范围或筛选条件。 | 新版 |
| [删除筛选视图](0625-api-deletefilterview.md) | 删除指定工作表上的某个筛选视图及其所有筛选条件。 | 新版 |
| [获取筛选视图列表](0626-api-getfilterviews.md) | 获取指定工作表上所有筛选视图的列表。 | 新版 |
| [设置筛选视图条件](0627-api-setfilterviewcriteria.md) | 为指定筛选视图中的某一列设置或更新筛选条件。 | 新版 |
| [删除筛选视图条件](0628-api-clearfilterviewcriteria.md) | 清除指定筛选视图中某一列的筛选条件，使该列不再参与筛选计算。 | 新版 |

### **浮动图片**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建浮动图片](0629-api-createfloatimage.md) | 获取钉钉表格指定工作表中所有浮动图片的列表信息。 | 新版 |
| [更新浮动图片](0630-api-updatefloatimage.md) | 更新钉钉表格中已有浮动图片的属性。 | 新版 |
| [删除浮动图片](0631-api-deletefloatimage.md) | 删除钉钉表格指定工作表中的一张浮动图片。 | 新版 |

## 名词解释

### **workbookId**

表格文件的唯一标识。即知识库 API 返回的`nodeId`（`dentryUuid`），也可以从表格 URL 中获取。获取方式如下：

- **方式一**：从表格 URL 中获取。

  ![从URL获取workbookId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2944684771/p1063487.png)
- **方式二**：从文档信息中获取。

  ![从文档信息获取workbookId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2944684771/p1063490.png)
- **方式三**：通过知识库 API 获取。

  调用[获取节点](0570-get-knowledge-base-acquisition-node.md)或[创建知识库文档](0567-create-team-space-document.md)接口，返回的`nodeId`（`dentryUuid`）即为`workbookId`。

### **sheetId**

工作表的 ID 或名称。可通过[获取所有工作表](0595-obtain-all-worksheets.md)接口获取，也可以直接传工作表标题。

### **rangeAddress**

单元格范围地址，使用 A1 表示法。

### **operatorId**

操作人的`unionId`，用于标识执行操作的用户身份和权限校验。
