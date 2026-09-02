---
title: "调用脚本服务"
source_url: "https://open.dingtalk.com/document/development/call-the-script-service"
namespace: "development"
slug: "call-the-script-service"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 脚本服务 > 调用脚本服务"
doc_id: "jS5IcrG0lL"
updated_at: "2025-08-27 18:09:22"
---

> Source: https://open.dingtalk.com/document/development/call-the-script-service
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 脚本服务 > 调用脚本服务
> Updated: 2025-08-27 18:09:22

# 调用脚本服务

本文通过调用**Dingdocs.script.run**的JSAPI执行文档酷应用脚本服务。

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

在UI页面，开发者可调用**Dingdocs.script.run**执行文档酷应用脚本服务。

```
Dingdocs.script.run('insertSheet').catch((e) => console.error(e));
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| funcName | String | 是 | 脚本服务名称。 |
| ...args | any[] | 是 | 执行脚本服务时的传参。 |
