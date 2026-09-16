---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-of-application-licensing"
namespace: "development"
slug: "overview-of-application-licensing"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "应用授权 > 概述"
doc_id: "LpOCAZjf7x"
updated_at: "2026-07-02 10:35:36"
---

> Source: https://open.dingtalk.com/document/development/overview-of-application-licensing
> Path: 应用开发 / 服务端 API / 应用授权 > 概述
> Updated: 2026-07-02 10:35:36

# 概述

钉钉应用广场中的第三方企业应用，企业管理员可以授权开通。管理员授权开通应用时，钉钉会推送**企业授权变更应用**事件给第三方企业应用，第三方企业应用需要进行企业信息初始化和授权。

钉钉支持通过以下三种方式推送**企业授权变更应用**事件。不同的推送方式，初始化企业信息完成授权的方式也不同。

- RDS推送（聚石塔/钉钉云部署）
- HTTP推送（不推荐）
- SyncHTTP推送

![p205947](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6379592871/p259908.png)

## RDS推送（聚石塔/钉钉云）和SyncHTTP推送的授权流程

推荐第三方企业应用使用RDS推送来接收数据，安全稳定性能高。

钉钉云RDS推送和SyncHTTP推送方式下，管理员授权开通应用的流程如下图所示。

> **[!NOTE]**
>
> 小程序使用dd.corpId获取企业corpId，微应用由前端从URL中获取。微应用的首页URL，可以使用$CORPID$做为参数占位符，钉钉容器会将$CORPID$替换为当前访问的企业的corpId。

![钉钉云推送流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5175299951/p165940.png)
