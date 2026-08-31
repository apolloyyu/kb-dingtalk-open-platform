---
title: "关闭当前视图容器"
source_url: "https://open.dingtalk.com/document/development/closes-container"
namespace: "development"
slug: "closes-container"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 表格能力 > 关闭当前视图容器"
doc_id: "f36Pgk6DAR"
updated_at: "2025-08-27 18:09:24"
---

> Source: https://open.dingtalk.com/document/development/closes-container
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 表格能力 > 关闭当前视图容器
> Updated: 2025-08-27 18:09:24

# 关闭当前视图容器

本文通过调用调用**Dingdocs.workbook.host.close**关闭当前视图容器。

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

调用**Dingdocs.workbook.host.close**关闭当前视图容器。

```
await Dingdocs.workbook.host.close();
```
