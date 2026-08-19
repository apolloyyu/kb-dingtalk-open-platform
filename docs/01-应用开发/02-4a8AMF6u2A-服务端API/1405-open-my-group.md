---
title: "打开我的群组"
source_url: "https://open.dingtalk.com/document/development/open-my-group"
namespace: "development"
slug: "open-my-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 会话相关 > 打开我的群组"
doc_id: "oHeRKBARrg"
updated_at: "2026-01-22 20:17:46"
---

> Source: https://open.dingtalk.com/document/development/open-my-group
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 会话相关 > 打开我的群组
> Updated: 2026-01-22 20:17:46

# 打开我的群组

本文档介绍如何通过 AppLink 协议在钉钉客户端中打开“我的群组”页面，适用于企业内部应用或第三方应用中需要快速跳转至群聊列表的场景。

## **使用场景**

当用户在应用内点击“我的群聊”或“查看全部群组”等按钮时，可通过此 AppLink 协议直接跳转至钉钉客户端的群组列表页面，提升用户体验与操作效率。该功能适用于以下典型业务场景：

- 企业自建应用中集成群聊入口，方便员工快速访问所属群组。
- 第三方协作工具中提供一键跳转至钉钉群的功能，增强沟通便捷性。
- 应用仪表盘或个人中心增加“群组管理”快捷入口。

## **扫码体验**

扫描下方二维码，可立即在移动端体验该协议的实际效果：

![qrcode (7)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4588375761/p556508.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/groupchat
```

该 URL 为固定协议地址，无需附加任何参数即可生效。调用后将自动打开当前用户默认的“我的群组”页面。

## **字段说明**

本协议无字段。该链接为固定入口，打开的是当前用户默认的群聊列表页面，无需额外参数配置。

## 注意事项

- 该协议不支持传递参数来自定义跳转目标群组。
- 若用户未加入任何群组，仍将进入“我的群组”页面，显示为空列表。
