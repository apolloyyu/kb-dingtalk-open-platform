---
title: "打开特别关注"
source_url: "https://open.dingtalk.com/document/development/open-special-attention"
namespace: "development"
slug: "open-special-attention"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开特别关注"
doc_id: "xwciBQ89oi"
updated_at: "2026-01-22 20:17:48"
---

> Source: https://open.dingtalk.com/document/development/open-special-attention
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开特别关注
> Updated: 2026-01-22 20:17:48

# 打开特别关注

本文档介绍如何使用 AppLink 协议打开钉钉中的“特别关注”页面。该功能适用于需要引导用户快速进入特别关注列表的场景，例如消息提醒聚合、重要联系人管理等。通过标准 AppLink 跳转机制，开发者可在企业内部应用中实现一键直达“特别关注”页面，提升用户操作效率和消息触达率。

## **使用场景**

在企业IM协作环境中，用户常需快速查看重点关注的成员或群组动态。通过集成 AppLink 协议，以下业务场景可获得显著优化：

- **消息聚合提醒**：当系统检测到关键人员发送新消息时，自动提示并提供跳转入口，引导用户进入“特别关注”列表进行集中查阅。
- **组织架构管理工具**：HR 或管理员在员工自助平台中嵌入“特别关注”快捷入口，帮助新员工快速访问直属上级、部门负责人等重点联系人。
- **协同办公看板**：在项目管理应用中，将项目核心成员设为推荐关注对象，并通过按钮触发跳转，便于团队成员一键关注关键角色。

此类设计减少了用户的多层导航操作，提升了高频功能的可达性。

## **扫码体验**

在手机上使用钉钉客户端扫描该二维码，系统将自动识别协议并跳转至“特别关注”页面。

![qrcode (14)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5143375761/p556455.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/attention_list
```

该协议基于钉钉标准 AppLink 跳转机制，允许外部 H5 页面或应用内组件唤起钉钉原生“特别关注”页面。AppLink 是钉钉提供的一套通用页面跳转协议体系，支持通过 URL 直接打开特定功能模块。

## **字段说明**

- 本协议无自定义字段，仅依赖标准 AppLink 跳转机制完成页面唤起。
- 构造完整的 AppLink URL：`https://applink.dingtalk.com/page/attention_list`

  确保链接完整且未被编码错误。

## 常见问题

**Q：为什么点击后没有反应？**

A：请检查是否在钉钉内置浏览器中打开页面，且客户端版本符合最低要求（≥6.5.45）。同时确认链接未被 URL 编码处理。

**Q：能否携带参数指定默认选中的关注对象？**

A：当前协议不支持传参，仅能打开“特别关注”主列表页面。

**Q：Windows 或 macOS 上是否可用？**

A：目前仅移动端支持，桌面端暂不支持该协议跳转。
