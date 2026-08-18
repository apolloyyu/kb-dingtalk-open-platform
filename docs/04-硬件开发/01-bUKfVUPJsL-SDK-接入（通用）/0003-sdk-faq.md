---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/sdk-faq"
namespace: "development"
slug: "sdk-faq"
group: "硬件开发"
tab: "SDK 接入（通用）"
breadcrumb: "常见问题"
doc_id: "Kx1DP0pcDN"
updated_at: "2026-08-18 09:07:53"
---

> Source: https://open.dingtalk.com/document/development/sdk-faq
> Path: 硬件开发 / SDK 接入（通用） / 常见问题
> Updated: 2026-08-18 09:07:53

# 常见问题

SDK接入接口遇见的常见问题。

- **本SDK是否提供网络接入能力？**

  目前发布的SDK为1.1版本，只提供了协助厂商进行WIFI配网的接口，暂未提供网络通讯能力，如果需要网络通讯能力，请直接参考阿里云IOT的LINK-SDK接入。
- **为什么蓝牙通讯使用物模型？**

  大部分具有网络通讯能力的接入设备，其网络部分采用的阿里云物联网接入开源方案，其使用的也是物模型协议，为了保持协议的一致性，本SDK蓝牙端也使用物模型作为蓝牙通讯上层协议。
- **51架构的单片机是否能够接入SDK？**

  目前版本的SDK需要动态内存分配能力，很多传统51单片机无法支持内存分配能力，不过这种类型的单片机目前已经不多了，如果有接入需要，可联系勤龙来评估具体接入开发。
- **具体我接入的设备的业务相关的物模型文档从哪里获取？**

  后续对应接入设备的物模型文档会和本SDK交付物一同提供。
- **SDK对系统资源的要求？**

  - SDK内部自己实现AES+MD5时， FLASH需要30K，RAM需要8K。
  - SDK内部不自己实现AES+MD5时，FLASHA需要20K，RAM需要4K。
- **每次蓝牙通讯数据的最大长度是多少？**

  最大长度1K。
