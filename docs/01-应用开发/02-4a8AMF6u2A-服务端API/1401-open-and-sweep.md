---
title: "打开扫一扫"
source_url: "https://open.dingtalk.com/document/development/open-and-sweep"
namespace: "development"
slug: "open-and-sweep"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开扫一扫"
doc_id: "pQgdOzST4n"
updated_at: "2025-12-26 15:07:47"
---

> Source: https://open.dingtalk.com/document/development/open-and-sweep
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开扫一扫
> Updated: 2025-12-26 15:07:47

# 打开扫一扫

本说明文档介绍如何使用AppLink协议打开钉钉扫一扫功能。通过该协议，开发者可在H5页面中快速唤起钉钉客户端的“扫一扫”功能，实现扫码交互操作。

## **使用场景**

在企业应用或第三方服务中，当需要用户扫描二维码以完成身份验证、设备绑定或跳转特定页面时，可通过AppLink协议直接调用钉钉内置的扫一扫功能，提升操作效率与用户体验。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

![qrcode (6)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3223375761/p556442.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/scan
```

## **字段说明**

本协议无字段。

> **[!NOTE]**
>
> - 用户点击链接后，系统将自动唤起钉钉客户端并进入“扫一扫”界面。
> - 若无法唤起钉钉，请检查是否已正确拼接协议地址，并确认钉钉为最新版本。
