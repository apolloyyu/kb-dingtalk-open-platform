---
title: "弹出对话框"
source_url: "https://open.dingtalk.com/document/development/pop-up-dialog"
namespace: "development"
slug: "pop-up-dialog"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 表格能力 > 弹出对话框"
doc_id: "fkNs9hZ8y5"
updated_at: "2025-08-27 18:09:23"
---

> Source: https://open.dingtalk.com/document/development/pop-up-dialog
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 表格能力 > 弹出对话框
> Updated: 2025-08-27 18:09:23

# 弹出对话框

本文通过调用**Dingdocs.workbook.host.showDialog**弹出对话框容器。

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

调用**Dingdocs.workbook.host.showDialog**弹出对话框容器。

```
Dingdocs.workbook.host.showDialog(
  `https://www.example.com/dialog.html`,
  { width: 600, height: 300 },
).then((view) => {
  view.onMessageReceived((data) => {
    console.log(data);
  });
}).catch((e) => console.error(e));
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| url | String | 是 | 对话框容器内展示的ui界面地址。 |
| dialogOptions | IWorkbookDialogOptions | 否 | 对话框容器的可选配置：   - **width**：容器宽度 - **height**：容器高度 - **title**：容器标题 |
