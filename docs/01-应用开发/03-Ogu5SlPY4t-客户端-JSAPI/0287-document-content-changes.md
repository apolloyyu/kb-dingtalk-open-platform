---
title: "监听文档内容变更"
source_url: "https://open.dingtalk.com/document/development/document-content-changes"
namespace: "development"
slug: "document-content-changes"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 监听文档状态 > 监听文档内容变更"
doc_id: "9kMIJPWBL7"
updated_at: "2025-08-27 18:09:26"
---

> Source: https://open.dingtalk.com/document/development/document-content-changes
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 监听文档状态 > 监听文档内容变更
> Updated: 2025-08-27 18:09:26

# 监听文档内容变更

本文通过调用**Dingdocs.workbook.event.onContentChanged**监听文档内容变更。

## **准备工作**

初始化脚本服务JSAPI需依赖[dingtalk-docs-cool-app](https://www.npmjs.com/package/dingtalk-docs-cool-app)，请先升级到最新版本。

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

调用**Dingdocs.workbook.event.onContentChanged**监听文档内容变更。

```
offContentChanged = Dingdocs.workbook.event.onContentChanged(({ sheetId, a1Notation }) => {
  console.log('ContentChanged', sheetId, a1Notation);
})
// 注销监听
offContentChanged()
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| handler | Function | 是 | 监听文档内容变更后的回调：   - **sheetId**：发生变更的表格id - **a1Notation**：发生变更的单元格位置 |
