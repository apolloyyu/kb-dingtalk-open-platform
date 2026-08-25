---
title: "获取工作台API访问凭证"
source_url: "https://open.dingtalk.com/document/development/used-to-obtain-the-application-authorization-without-api-token"
namespace: "development"
slug: "used-to-obtain-the-application-authorization-without-api-token"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉工作台 > 获取工作台API访问凭证"
doc_id: "t7dOryppF7"
updated_at: "2026-08-25 09:36:37"
---

> Source: https://open.dingtalk.com/document/development/used-to-obtain-the-application-authorization-without-api-token
> Path: 应用开发 / 服务端API / 钉钉工作台 > 获取工作台API访问凭证
> Updated: 2026-08-25 09:36:37

# 获取工作台API访问凭证

API Token是由钉钉开放平台颁发，用来调用钉钉开放平台提供的应用管理能力。在调用钉钉开放平台提供的应用管理能力前，请参考本文先获取访问凭证API Token。

## 简介

在调用DingTalk OpenAPI中的工作台相关接口前，必须从开放平台获取访问凭证API Token，这个访问凭证包含你的企业信息以及可调用的接口权限，目前可调用工作台相关的接口如下：

- [获取工作台插件权限点](1000-obtain-the-permissions-of-the-workbench-plug-in.md)
- [批量添加最近使用应用](0999-add-recently-used-apps-in-bulk.md)
- [获取工作台插件检验的规则信息](1001-you-can-call-this-operation-to-obtain-the-information-about.md)

## 获取访问凭证API Token

通过以下步骤，获取API Token：

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 在开发者后台首页，单击**生成TOKEN**，用于生成持久的API Token。

   > **[!NOTE]**
   >
   > - 重新生成API Token之后，之前的API Token会失效。
   > - 同一企业同一时间生效的API Token只有一个。

   ![获取API Token](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3700594261/p290038.png)
3. （可选）生成Token后，单击后面的设置图标，设置Token的IP白名单。

   > **[!NOTE]**
   >
   > 出于安全性考虑，钉钉开放平台提供了生成Token和设置Token生效的IP白名单功能，降低了因Token泄漏导致的安全风险。

   ![设置IP白名单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3700594261/p290039.png)
