---
title: "初始化脚本服务"
source_url: "https://open.dingtalk.com/document/development/initialize-script-service"
namespace: "development"
slug: "initialize-script-service"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 初始化酷应用 > 初始化脚本服务"
doc_id: "qB2YI61brW"
updated_at: "2025-08-27 18:09:19"
---

> Source: https://open.dingtalk.com/document/development/initialize-script-service
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 初始化酷应用 > 初始化脚本服务
> Updated: 2025-08-27 18:09:19

# 初始化脚本服务

本文介绍通过调用initScript进行文档酷应用初始化脚本服务。

## **准备工作**

初始化脚本服务需依赖[dingtalk-docs-cool-app](https://www.npmjs.com/package/dingtalk-docs-cool-app)，请先升级到最新版本。

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

在脚本服务页面，开发者可调用**initScript**初始化脚本服务，导入脚本函数**。**

```
import { initScript } from 'dingtalk-docs-cool-app';
initScript({
  scriptUrl: '脚本函数js文件',
})
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| scriptUrl | String | 是 | 脚本函数js文件地址。 |
