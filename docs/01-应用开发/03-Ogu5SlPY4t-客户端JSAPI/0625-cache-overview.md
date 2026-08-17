---
title: "缓存概览"
source_url: "https://open.dingtalk.com/document/development/cache-overview"
namespace: "development"
slug: "cache-overview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 缓存概览"
doc_id: "ru06aa6hy6"
updated_at: "2025-09-17 20:59:58"
---

> Source: https://open.dingtalk.com/document/development/cache-overview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 缓存概览
> Updated: 2025-09-17 20:59:58

# 缓存概览

小程序的缓存数据是以应用为维度。不同ID的小程序间缓存数据是互相隔离、不受影响的。默认情况下，开发者无需关心缓存维度的问题。

当开发者在开发第三方企业应用且希望使用本地缓存临时保存用户企业相关的一些信息时，则需要注意缓存的这个特性。用户可以存在于多个组织，在不同的组织间可以随意切换，多个组织可能会开通同一个第三方企业应用。这种情况下，从应用的维度，同一个用户在不同的时间可能具备不同的企业身份，即dd.corpId不同。

**扫码体验**

![1595555871023-13](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4675013061/p174274.png)
