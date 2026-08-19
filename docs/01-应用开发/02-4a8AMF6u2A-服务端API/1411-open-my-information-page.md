---
title: "打开我的信息页面"
source_url: "https://open.dingtalk.com/document/development/open-my-information-page"
namespace: "development"
slug: "open-my-information-page"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开我的信息页面"
doc_id: "ynvOcf3zBK"
updated_at: "2025-12-26 15:07:50"
---

> Source: https://open.dingtalk.com/document/development/open-my-information-page
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开我的信息页面
> Updated: 2025-12-26 15:07:50

# 打开我的信息页面

本文档介绍如何通过 AppLink 协议唤起钉钉客户端并跳转至当前用户个人资料页。该协议适用于需要快速访问用户个人信息的场景，例如身份核验、内部系统集成等。

## **使用场景**

本协议用于在支持 AppLink 的环境中调用钉钉客户端，直接打开当前登录用户的“我的信息”页面。此操作无需额外参数，协议本身不包含可配置字段，但依赖设备端已安装钉钉应用且用户处于登录状态。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

![qrcode (12)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3329375761/p556486.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/myProfile
```

## **字段说明**

本协议无自定义字段，所有行为由客户端默认逻辑控制。
