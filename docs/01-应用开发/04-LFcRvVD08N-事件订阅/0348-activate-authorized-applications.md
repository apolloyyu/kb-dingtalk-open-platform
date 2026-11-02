---
title: "授权应用开通"
source_url: "https://open.dingtalk.com/document/development/activate-authorized-applications"
namespace: "development"
slug: "activate-authorized-applications"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 授权应用开通"
doc_id: "JlxllTtvMH"
updated_at: "2025-10-16 15:06:31"
---

> Source: https://open.dingtalk.com/document/development/activate-authorized-applications
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 授权应用开通
> Updated: 2025-10-16 15:06:31

# 授权应用开通

钉钉应用广场中的第三方企业应用，企业管理员可以授权开通。开通后，钉钉后台会推送授权信息到第三方应用后台。第三方企业应用需要完成企业信息初始化和授权。

钉钉支持通过RDS推送（聚石塔/钉钉云）、HTTP推送和SyncHTTP推送方式向应用推送回调事件。第三方应用后台收到**企业授权变更应用**事件后，需要初始化企业信息。不同的推送方式，初始化企业信息完成授权的方式也不同。

![p205947](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7639207161/p256072.png)

## RDS推送（聚石塔/钉钉云）和SyncHTTP推送

推荐第三方企业应用使用RDS推送来接收数据，安全稳定性能高。

钉钉云RDS推送和SyncHTTP推送方式下，管理员授权开通应用的流程如下图所示。

> **[!NOTE]**
>
> 小程序使用dd.corpId获取企业corpId，微应用由前端从URL中获取。微应用的首页URL，可以使用$CORPID$做为参数占位符，钉钉容器会将$CORPID$替换为当前访问的企业的corpId。
>
> 例如:https://www.dingtalk.com?corpId=$CORPID$

![钉钉云推送流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5175299951/p165940.png)
