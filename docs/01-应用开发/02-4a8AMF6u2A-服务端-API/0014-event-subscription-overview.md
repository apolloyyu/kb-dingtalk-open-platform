---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/event-subscription-overview"
namespace: "development"
slug: "event-subscription-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "事件订阅 > 概述"
doc_id: "wyndAPHm6X"
updated_at: "2026-07-02 10:35:13"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-overview
> Path: 应用开发 / 服务端 API / 事件订阅 > 概述
> Updated: 2026-07-02 10:35:13

# 概述

## 什么是事件订阅。

钉钉事件订阅功能，是钉钉开放平台推出的一项服务。这项服务允许开发者在自己开发的应用程序中，实时接收到钉钉平台产生的各类重要通知。通过设置事件订阅，你的应用能够监听到钉钉中发生的诸如部门架构调整、员工签到、打卡等事件，并据此在你的应用中进行及时响应和处理。利用这一功能，你的企业应用将能够更深度地与钉钉平台集成，实现信息共享和业务协同。

## **订阅流程**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3179592871/p741471.png)

## **订阅方式**

### **Stream 模式推送**

Stream 模式是钉钉开放平台提供的一种集成方式，它可以监听事件订阅回调使用 Stream 模式接入，钉钉开放平台将通过 Websocket 连接与应用程序通讯，Stream 模式将极大降低接入门槛和资源依赖，不需要公网服务器、IP、域名等资源，只需集成钉钉开放平台 SDK 即可。

- **适用应用：**企业内部应用、第三方企业应用
- **配置方式**：参考[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)
- **安全性**：不需要暴露公网ip，免受攻击，传输层使用TLS加密，每条连接的建立都有完整鉴权。
- **加解密**：无需加解密，接收到的为事件详细数据。

### **HTTP 推送**

HTTP推送方式适用于本地部署的情况，以HTTP POST请求方式以加密的方式推送给业务方。

- **适用应用：**企业内部应用
- **配置方式**：参考[配置 HTTP 推送（不推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#58bfd87c4fupu)
- **安全性**：数据通道是公网通道，需要流量花费，安全等级低，效率低。
- **加解密**：推送的数据是密文数据，需要开发者自行验签、加解密，实现不同开发语言的验签、加解密逻辑。
