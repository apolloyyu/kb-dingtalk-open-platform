---
title: "App Extension接入"
source_url: "https://open.dingtalk.com/document/development/app-extension-access-1"
namespace: "development"
slug: "app-extension-access-1"
group: "专属版客户端插件"
tab: "iOS 插件"
breadcrumb: "iOS 插件 > App Extension接入"
doc_id: "tyvgoBIkAl"
updated_at: "2026-08-12 09:20:48"
---

> Source: https://open.dingtalk.com/document/development/app-extension-access-1
> Path: 专属版客户端插件 / iOS 插件 / iOS 插件 > App Extension接入
> Updated: 2026-08-12 09:20:48

# App Extension接入

钉钉目前仅支持Network Extension类别的appex接入，用于三方开发VPN等服务。本章节介绍如何接入Network Extension。

## **证书与审核**

- 打包appex需要额外的一份mobile provision

  - bundle id: **dd.work.exclusive4xxx.NetworkExtension**
- 如果需要上架ABM，则必须获得政府部门许可的VPN运营资质证明文件

### **集成方式**

由于钉钉侧暂时没有Network Extension，因此目前开发者需要提供打包好的appex文件，钉钉侧在打包过程中会重签名注入到产物中。

- 命名规范：DingtalkExtNetworkExtension.appex

> **[!IMPORTANT]**
>
> 由于不排除钉钉后续也要开发NetworkExtension的可能性，因此接入方需要慎重评估后续升级过程中潜在的冲突，如果后续开发中存在冲突，钉钉侧会联系开发方进行调整适配，存在额外的开发工作。
