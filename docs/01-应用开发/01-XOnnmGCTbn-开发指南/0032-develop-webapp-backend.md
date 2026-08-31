---
title: "开发网页应用服务端"
source_url: "https://open.dingtalk.com/document/dingstart/develop-webapp-backend"
namespace: "dingstart"
slug: "develop-webapp-backend"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 开发网页应用服务端"
doc_id: "8yNN6uNxHl"
updated_at: "2026-06-30 09:00:36"
---

> Source: https://open.dingtalk.com/document/dingstart/develop-webapp-backend
> Path: 应用开发 / 开发指南 / 开发网页应用 > 开发网页应用服务端
> Updated: 2026-06-30 09:00:36

# 开发网页应用服务端

如果你需要实现免登、接入事件订阅和使用钉钉服务端 API，参考本文档流程概览开发网页应用服务端。

## 流程概览

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**开发配置** > **安全设置**，填写服务端出口 IP。

   > **[!NOTE]**
   >
   > 服务端出口 IP：指调用钉钉服务端 API 时，必须在开发者后台配置的合法服务器 IP 地址列表，用于建立安全白名单机制。若未配置或请求 IP 不在列表中，接口调用将报错“访问 ip 不在白名单之中”。需填入企业服务器的公网 IP（支持 IPv4，多个 IP 用逗号分隔，部分场景支持通配符）。
3. 实现免登，企业内部应用请参考[网页应用（H5微应用）免登](../02-4a8AMF6u2A-服务端-API/0018-enterprise-internal-application-logon-free.md)，第三方企业应用请参考[开发并测试第三方企业网页应用（H5）免登](../02-4a8AMF6u2A-服务端-API/0020-web-applications-h5.md)。
4. 申请接口调用权限。详情参考[添加接口调用权限](../02-4a8AMF6u2A-服务端-API/0003-add-api-permission.md)。
5. 选择合适的事件推送方式并完成接入。

   开发者对特定的事件进行订阅并接收相关的推送消息。通过事件订阅功能，开发者可以及时获取钉钉中发生的各种事件的通知。企业内部应用支持两种种方式接收钉钉推送的回调事件：[开发 HTTP 推送服务端](../04-LFcRvVD08N-事件订阅/0004-develop-stream-mode-push-server.md#6d7a5d60ddwgj)和[开发 Stream 模式推送服务端（推荐）](../04-LFcRvVD08N-事件订阅/0004-develop-stream-mode-push-server.md#7c157d52c89et)。
6. 调用服务端 API，进行业务集成。例如调用机器人接口。详情参考[服务端SDK下载](../02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)。
