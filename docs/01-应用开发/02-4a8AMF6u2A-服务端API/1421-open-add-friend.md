---
title: "打开添加好友"
source_url: "https://open.dingtalk.com/document/development/open-add-friend"
namespace: "development"
slug: "open-add-friend"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开添加好友"
doc_id: "EittWJS1vu"
updated_at: "2026-01-23 10:14:22"
---

> Source: https://open.dingtalk.com/document/development/open-add-friend
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开添加好友
> Updated: 2026-01-23 10:14:22

# 打开添加好友

本文档介绍如何通过 AppLink 协议在外部应用中唤起钉钉客户端并跳转至“添加好友”页面，适用于希望提升用户添加联系人效率的开发者。

## **使用场景**

在第三方应用或网页中，点击链接即可直接唤起钉钉客户端并进入“添加好友”界面，避免用户手动打开钉钉搜索联系人，显著提升操作便捷性。该功能广泛应用于以下场景：

- 企业对外服务页面嵌入添加客服链接
- 合作伙伴间快速建立沟通关系
- 社交引流、客户转化等业务场景

## **快速体验**

请点击 <https://applink.dingtalk.com/page/addContact>。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | ≥6.5.50 | ≥6.5.50 |

## **协议**

```
https://applink.dingtalk.com/page/addContact
```

## **字段说明**

- 本协议采用标准的 AppLink 协议格式，无需携带任何参数即可触发钉钉客户端的添加好友界面。
- 该链接为固定路径调用，不支持附加查询参数，所有跳转行为由钉钉客户端内部逻辑处理。
- 调用成功时，系统将自动拉起已安装的钉钉应用，并进入“添加好友”页面。
- 若未安装钉钉，则部分浏览器会提示前往应用商店下载。
