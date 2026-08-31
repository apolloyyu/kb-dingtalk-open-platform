---
title: "初始化UI界面"
source_url: "https://open.dingtalk.com/document/development/initialize-ui-interface"
namespace: "development"
slug: "initialize-ui-interface"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 初始化酷应用 > 初始化UI界面"
doc_id: "CRIGBJ6Npi"
updated_at: "2025-08-27 18:09:19"
---

> Source: https://open.dingtalk.com/document/development/initialize-ui-interface
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 初始化酷应用 > 初始化UI界面
> Updated: 2025-08-27 18:09:19

# 初始化UI界面

本文通过调用initView初始化UI页面。

## **准备工作**

初始化UI页面需依赖[dingtalk-docs-cool-app](https://www.npmjs.com/package/dingtalk-docs-cool-app)，请先升级到最新版本。

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

在UI页面，开发者可调用**initView**初始化UI页面，允许UI页面访问全局变量「Dingdocs」。

```
/*global Dingdocs*/
import { initView } from 'dingtalk-docs-cool-app';
initView({
 	onReady: () => {
  },
})
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| onReady | Function | 否 | 初始化结束后的回调。 |
