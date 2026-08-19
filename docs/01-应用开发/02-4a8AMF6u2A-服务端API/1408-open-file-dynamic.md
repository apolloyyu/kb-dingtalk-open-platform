---
title: "打开文件动态"
source_url: "https://open.dingtalk.com/document/development/open-file-dynamic"
namespace: "development"
slug: "open-file-dynamic"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开文件动态"
doc_id: "QoVhcFyojF"
updated_at: "2025-12-26 19:28:54"
---

> Source: https://open.dingtalk.com/document/development/open-file-dynamic
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开文件动态
> Updated: 2025-12-26 19:28:54

# 打开文件动态

AppLink协议是一种用于在移动端实现应用间跳转的轻量级通信机制。通过该协议，开发者可以快速唤起钉钉客户端中的特定功能页面，例如文件动态页面（fileLog）。

## **使用场景**

此功能适用于需要追踪用户文件操作行为的业务场景，如协同办公、文档审计等。扫码体验版本支持跳转至钉钉内的`fileLog`页面，便于开发者验证调用逻辑和展示效果。支持多种类型文件的访问日志追踪，包括文档、表格、PPT、PDF及音视频文件。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

![qrcode (8)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2519375761/p556488.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/yunpan
```

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/yunpan | route | 是 | 固定值为fileLog。 |

## **使用示例**

请确保设备已安装最新版钉钉客户端，并处于登录状态，否则可能导致跳转失败。若未自动唤起钉钉，请手动选择使用钉钉打开链接。

```
https://applink.dingtalk.com/page/yunpan?yunpan=fileLog
```
