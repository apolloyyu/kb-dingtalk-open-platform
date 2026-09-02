---
title: "将对话框信息转发至其父页"
source_url: "https://open.dingtalk.com/document/development/dialog-parent-page"
namespace: "development"
slug: "dialog-parent-page"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 表格能力 > 将对话框信息转发至其父页"
doc_id: "KhTxaOzlHG"
updated_at: "2025-08-27 18:09:23"
---

> Source: https://open.dingtalk.com/document/development/dialog-parent-page
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 表格能力 > 将对话框信息转发至其父页
> Updated: 2025-08-27 18:09:23

# 将对话框信息转发至其父页

本文通过调用**Dingdocs.workbook.host.messageParent**将对话框信息转发至其父页。

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

调用**Dingdocs.workbook.host.messageParent**将对话框信息转发至其父页。

```
await Dingdocs.workbook.host.messageParent(data);
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| data | any | 是 | 转发内容。 |
