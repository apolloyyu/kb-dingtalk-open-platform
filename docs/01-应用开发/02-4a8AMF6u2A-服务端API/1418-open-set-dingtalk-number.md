---
title: "打开设置钉钉号"
source_url: "https://open.dingtalk.com/document/development/open-set-dingtalk-number"
namespace: "development"
slug: "open-set-dingtalk-number"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开设置钉钉号"
doc_id: "fmm7NzCsei"
updated_at: "2025-12-26 15:07:53"
---

> Source: https://open.dingtalk.com/document/development/open-set-dingtalk-number
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开设置钉钉号
> Updated: 2025-12-26 15:07:53

# 打开设置钉钉号

本文档介绍使用AppLink协议打开设置钉钉号页面的相关说明。

## **使用场景**

在企业管理或成员管理过程中，若需引导用户快速进入“设置钉钉号”页面进行配置，可通过 AppLink 协议实现一键跳转，提升操作效率。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

![qrcode (19)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9843375761/p556467.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/dingtalk_id_settings
```

## **字段说明**

- 本协议无额外参数字段，直接使用固定链接即可完成跳转。
- 使用已登录钉钉账号的移动设备（Android 或 iOS）扫描该二维码。
- 确保设备上已安装并登录最新版钉钉客户端（≥6.5.45）。
