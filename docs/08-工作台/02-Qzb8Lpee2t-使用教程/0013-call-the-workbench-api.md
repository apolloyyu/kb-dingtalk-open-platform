---
title: "调用工作台 API"
source_url: "https://open.dingtalk.com/document/dingstart/call-the-workbench-api"
namespace: "dingstart"
slug: "call-the-workbench-api"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 其他参考"
doc_id: "SO2afwaWFW"
updated_at: "2025-12-08 09:29:42"
---

> Source: https://open.dingtalk.com/document/dingstart/call-the-workbench-api
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 其他参考
> Updated: 2025-12-08 09:29:42

# 调用工作台 API

调用工作台API前，需要先获取API调用凭证并申请接口权限。

## **开放能力**

在调用DingTalk OpenAPI中的工作台相关接口前，必须从开放平台获取访问凭证API Token，这个访问凭证包含你的企业信息以及可调用的接口权限，目前可调用工作台相关的接口如下：

- [获取工作台插件检验的规则信息](../../01-应用开发/02-4a8AMF6u2A-服务端API/1000-you-can-call-this-operation-to-obtain-the-information-about.md)
- [获取工作台插件权限点](../../01-应用开发/02-4a8AMF6u2A-服务端API/0999-obtain-the-permissions-of-the-workbench-plug-in.md)

## 获取访问凭证API Token

API Token是由钉钉开放平台颁发，用来调用钉钉开放平台提供的应用管理能力。在调用钉钉开放平台提供的应用管理能力前，需要通过以下步骤，获取API Token：

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

## **权限申请**

通过以下步骤添加工作台相关接口权限：

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/index)，然后单击目标应用，进入**应用详情**页。
2. 在**应用详情**页，单击**权限管理**，然后选择**工作台**。
3. 选择工作台相关接口权限，最后单击**申请权限**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8137405171/p786690.png)

## **接口调用流程**

如下图所示，在调用工作台API前，您需要完成以下准备工作：

1. 添加接口调用权限。应用创建后默认只开放登录和消息通知接口的调用权限，您需要根据开发需要，添加对应的接口使用权限。
2. 获取应用的access\_token。access\_token相当于是身份凭证。调用接口时，通过access\_token来鉴权调用者身份。

   - 企业内部应用请参考[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端API/0033-obtain-the-access-token-of-an-internal-app.md)。
   - 第三方企业应用请参考[获取第三方应用授权企业的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)。

     ![调用流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5025515361/p132205.png)

## 调用方式

钉钉开放平台提供了API Explorer和SDK方便开发者调用服务端API。

- API Explorer：

  API Explorer是可视化在线API调用工具，可实时查看API请求和返回结果。访问地址：<https://open-dev.dingtalk.com/apiExplorer>
- SDK:

  钉钉开放平台提供了Java、PHP、Python、.NET SDK供开发者使用。单击[服务端SDK下载](../../01-应用开发/02-4a8AMF6u2A-服务端API/0002-download-the-server-side-sdk.md)。
