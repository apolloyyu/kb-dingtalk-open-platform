---
title: "注册脚本服务"
source_url: "https://open.dingtalk.com/document/development/register-script-service"
namespace: "development"
slug: "register-script-service"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 脚本服务 > 注册脚本服务"
doc_id: "E6UQYMX8Xb"
updated_at: "2025-08-27 18:09:20"
---

> Source: https://open.dingtalk.com/document/development/register-script-service
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 脚本服务 > 注册脚本服务
> Updated: 2025-08-27 18:09:20

# 注册脚本服务

本文介绍通过调用**DingdocsScript.registerScript**注册钉钉文档模型脚本服务。

## **准备工作**

注册脚本服务需依赖[dingtalk-docs-cool-app](https://www.npmjs.com/package/dingtalk-docs-cool-app)，请先升级到最新版本。

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

在脚本函数js文件中，开发者可调用**DingdocsScript.registerScript**注册钉钉文档模型脚本服务。

```
function insertSheet() {

}

DingdocsScript.registerScript('insertSheet', insertSheet);
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| funcName | String | 是 | 脚本服务名称。 |
| func | String | 是 | 脚本服务行为。 |
