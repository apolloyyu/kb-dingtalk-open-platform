---
title: "发DING消息"
source_url: "https://open.dingtalk.com/document/development/send-ding-message"
namespace: "development"
slug: "send-ding-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 发DING消息"
doc_id: "QpyObxc3D4"
updated_at: "2026-01-22 20:17:47"
---

> Source: https://open.dingtalk.com/document/development/send-ding-message
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 发DING消息
> Updated: 2026-01-22 20:17:47

# 发DING消息

通过 AppLink 协议，可在 H5 页面中快速唤起钉钉客户端并跳转至 DING 消息创建页面，实现一键发送 DING 的功能。该协议适用于在钉钉移动端中触发钉钉 DING 功能的业务场景，例如任务提醒、审批催办等。

## **使用场景**

用户在 H5 页面或第三方应用中点击特定链接后，自动拉起钉钉客户端并进入“新建 DING”界面，提升消息触达效率和操作便捷性。

典型使用场景包括：任务截止前提醒、审批流程催办、会议邀约确认、项目进度同步等需要高优先级触达用户的业务环节。用户点击后可直接进入 DING 编辑界面，提升操作效率与用户体验。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

> 提示：请使用 Android 或 iOS 设备扫码，macOS 与 Windows 客户端暂不支持该协议。

![qrcode (10)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3633375761/p556450.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/dingcreate
```

## **字段说明**

- 该协议为无参直接跳转类型，调用后将默认打开钉钉内的 DING 创建页面，无需传递额外参数。
- 本协议不包含任何可配置字段，属于隐式调用行为，所有内容需由用户在客户端内手动填写。

## 常见问题

- **为什么点击后没有反应？**

  可能原因：钉钉未安装、版本过低、浏览器不支持跳转。建议检查设备环境并添加引导文案。
- **能否预填 DING 内容？**

  当前协议不支持预填标题或内容。
- **是否支持静默发送？**

  不支持。该协议仅用于跳转创建页面，最终发送动作由用户手动完成，保障信息安全与合规性。
- **macOS 或 Windows 上能用吗？**

  目前仅支持 Android 和 iOS 移动端，桌面端暂不支持此协议。
