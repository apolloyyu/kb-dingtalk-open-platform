---
title: "打开云盘首页"
source_url: "https://open.dingtalk.com/document/development/open-the-cloud-disk-home-page"
namespace: "development"
slug: "open-the-cloud-disk-home-page"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开云盘首页"
doc_id: "DRp5USAO44"
updated_at: "2026-01-21 15:04:17"
---

> Source: https://open.dingtalk.com/document/development/open-the-cloud-disk-home-page
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开云盘首页
> Updated: 2026-01-21 15:04:17

# 打开云盘首页

本文档介绍如何通过 AppLink 协议打开钉钉云盘首页。该功能适用于在 H5 页面或第三方应用中快速唤起钉钉客户端并跳转至用户个人云盘首页的场景，如文件管理、协同办公、内容分享等业务流程，帮助提升用户操作效率和体验。

## **使用场景**

当用户在移动端网页、小程序或外部应用中点击特定链接时，可通过 AppLink 协议自动唤起已安装的钉钉客户端，并直接跳转至其个人云盘首页。该方式避免了多次手动导航，适用于需要快速访问云盘内容的协作场景。

例如：

- 在企业内部 H5 管理系统中提供“前往云盘”入口；
- 第三方文档平台集成“在钉钉云盘查看”按钮；
- 营销活动页引导用户查看存储在云盘中的资料。

## **快速体验**

快速体验，请点击<https://applink.dingtalk.com/page/yunpan>。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | ≥6.5.50 | ≥6.5.50 |

## **协议**

```
https://applink.dingtalk.com/page/yunpan
```

## **字段说明**

- 本协议采用标准的 AppLink 协议格式，无需携带任何参数即可触发钉钉客户端的添加好友界面。
- 该链接为固定路径调用，不支持附加查询参数，所有跳转行为由钉钉客户端内部逻辑处理。
- 调用成功时，系统将自动拉起已安装的钉钉应用，并进入“添加好友”页面。
- 若未安装钉钉，则部分浏览器会提示前往应用商店下载。
