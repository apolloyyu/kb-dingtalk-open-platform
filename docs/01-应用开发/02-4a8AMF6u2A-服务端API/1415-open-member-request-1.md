---
title: "打开成员申请"
source_url: "https://open.dingtalk.com/document/development/open-member-request-1"
namespace: "development"
slug: "open-member-request-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开成员申请"
doc_id: "RI35Kn6tW4"
updated_at: "2025-12-26 15:07:52"
---

> Source: https://open.dingtalk.com/document/development/open-member-request-1
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开成员申请
> Updated: 2025-12-26 15:07:52

# 打开成员申请

本文档介绍如何使用AppLink协议打开新成员申请页面。该功能允许开发者通过标准协议唤起钉钉客户端中的成员申请页面，便于企业组织进行新成员的加入管理。

## **使用场景**

当企业应用需要引导用户进入钉钉组织的新成员申请页面时，可使用 `https://applink.dingtalk.com/page/orgapplylist` 协议直接跳转。适用于第三方管理后台、门户系统集成等场景，提升操作便捷性。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

![qrcode (16)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2339375761/p556483.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/orgapplylist
```

## **字段说明**

- 本协议无字段参数，无需拼接额外查询参数。直接使用上述链接即可触发页面跳转。
- 用户需已登录钉钉客户端，且客户端版本满足最低要求。
