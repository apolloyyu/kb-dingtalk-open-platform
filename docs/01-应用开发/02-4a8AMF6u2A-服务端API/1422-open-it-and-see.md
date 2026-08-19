---
title: "打开看看"
source_url: "https://open.dingtalk.com/document/development/open-it-and-see"
namespace: "development"
slug: "open-it-and-see"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开看看"
doc_id: "sINb7NeMOM"
updated_at: "2026-01-22 20:17:52"
---

> Source: https://open.dingtalk.com/document/development/open-it-and-see
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开看看
> Updated: 2026-01-22 20:17:52

# 打开看看

本文档介绍如何通过 AppLink 协议在钉钉客户端中唤起“看看”内容聚合页，帮助开发者实现从企业内部应用快速跳转至钉钉原生内容模块的功能。该能力适用于需要集成资讯、动态或轻量内容展示的企业微应用，提升用户在工作场景下的信息获取效率。

## **使用场景**

企业开发者可在微应用的 WebView 或钉钉内置浏览器中发起此协议跳转，用于快速进入钉钉“看看”模块的内容首页。典型使用场景包括：

- 在企业门户中嵌入“查看公司动态”入口，点击后直达“看看”页面。
- 从自定义工作台卡片跳转至组织内的内容聚合页，增强员工参与感与信息触达效率。

调用行为基于当前登录用户的上下文自动识别，无需额外传参。

## **扫码体验**

可通过扫描下方二维码，在移动设备上使用钉钉扫码访问示例页面，体验协议唤起效果。

![qrcode (23)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3744375761/p556478.png)

## 版本支持

在满足以下客户端版本的前提下，通过URL Scheme 唤起功能：

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/connectionCircleHome
```

## **字段说明**

- 此为固定协议链接，无需附加参数；
- 所有打开行为均基于当前登录用户上下文自动识别，不支持自定义字段传递；
- 钉钉客户端将自动解析用户身份及组织关系，并展示对应的“看看”内容页。
