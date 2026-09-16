---
title: "互动卡片消息发送流程"
source_url: "https://open.dingtalk.com/document/dingstart/interactive-card-message-sending-process"
namespace: "dingstart"
slug: "interactive-card-message-sending-process"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 互动卡片消息发送流程"
doc_id: "MGdy3Jan48"
updated_at: "2026-07-22 16:55:31"
---

> Source: https://open.dingtalk.com/document/dingstart/interactive-card-message-sending-process
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 互动卡片消息发送流程
> Updated: 2026-07-22 16:55:31

# 互动卡片消息发送流程

本文介绍了通过场景群的群助手发送互动卡片消息的流程。

## 步骤一：创建消息模板

在发送互动卡片消息前，需要先创建消息模板。消息模板通过组件的方式帮助你快速定义互动卡片消息的样式。详情请参考[创建消息模板](0095-create-a-message-template.md)。

## 步骤二：注册卡片回调地址

用户的交互行为，会通过HTTP post method 请求的形式回调给开发者注册的HTTP地址，所以需要配置好HTTP回调地址，详情请参考[响应互动卡片消息](0098-responding-to-interactive-messages.md)。

## 步骤三：发送互动卡片消息

1. 引入Maven包（Java工程）

   ```
   <dependency>
     <groupId>com.aliyun</groupId>
     <artifactId>dingtalk</artifactId>
     <version>1.0.23</version>
   </dependency>

   最新maven版本号，请查询阿里云maven仓库
    
   https://oss.sonatype.org/?spm=openapi-amp.sdkpublish.0.0.6ce52AE02AE0YH#nexus-search;gav~~dingtalk~~~
   ```
2. 调用[创建并投放卡片](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)接口发送动态卡片消息。

   > **[!IMPORTANT]**
   >
   > 该接口是新一代钉钉开放接口，请按照上一步的方式导入依赖。

   ![消息互动](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8779374161/p245171.png)

## 相关文档

其他接口：

- [响应互动卡片消息](0098-responding-to-interactive-messages.md)
- [创建并投放卡片](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)
