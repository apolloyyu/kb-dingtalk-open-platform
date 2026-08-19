---
title: "打开普通页面"
source_url: "https://open.dingtalk.com/document/development/open-normal-page"
namespace: "development"
slug: "open-normal-page"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开普通页面"
doc_id: "lQybe0dniF"
updated_at: "2026-07-21 09:26:23"
---

> Source: https://open.dingtalk.com/document/development/open-normal-page
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开普通页面
> Updated: 2026-07-21 09:26:23

# 打开普通页面

本文档介绍如何使用 AppLink 协议在钉钉客户端中打开普通网页页面，涵盖移动端与桌面端的容器类型控制、参数配置说明及使用示例。通过该协议，开发者可灵活指定目标页面的打开方式（如全屏、侧边栏、工作台等），提升用户体验和应用集成能力。

## **使用场景**

适用于企业内部自建应用或第三方 ISV 应用，在钉钉内通过链接跳转方式打开指定网页。例如：

- 在群聊机器人消息中点击链接，以侧边栏形式打开审批详情页；
- 从菜单入口进入时，使用沉浸式容器展示轻量级表单页面；
- 桌面端用户点击功能按钮后，在独立窗口或工作台区域打开管理后台。

此协议支持多端适配，可根据设备类型自动选择最优容器模式，实现一致的交互体验。

## **扫码体验**

![qrcode (3)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9713375761/p556414.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | ≥7.0.40 | ≥7.0.40 |

## **协议**

```
https://applink.dingtalk.com/page/link
```

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/link | url | 是 | 目标页面的url，需要urlEncode处理。 |
| target | 否 | 打开的容器类型：   - 移动端：    - **fullScreen**（默认）：全屏容器打开   - **panel**：沉浸式容器打开，请参考[沉浸式容器](1427-immersive-container-1.md) - 桌面端：    - **browser（默认）**：外部浏览器打开   - **popupWindow**：独立窗口打开   - **panel**：第四栏打开   - **slide**：侧边栏打开   - **workbench**：工作台打开 |
| targetDesktop | 否 | 打开的容器类型（桌面端）：   - **browser（默认）**：外部浏览器打开 - **popupWindow**：独立窗口打开 - **panel**：第四栏打开 - **slide**：侧边栏打开 - **workbench**：工作台打开   **[!NOTE]**   - targetDestop参数仅针对桌面端有效。 - 在链接中同时指定 targetDesktop 和 target 参数，桌面端会优先使用 targetDesktop 参数。 |
| mobileHeight | 否 | 移动端沉浸式容器高度。   - **semi**：百分之50屏幕高度，该字段不传则默认为 83%屏幕高度。 |

## 使用示例

- 使用**全屏容器**打开普通页面

  此链接将在移动端以全屏模式打开钉钉官网，兼容所有支持版本的客户端。

  ```
  https://applink.dingtalk.com/page/link?url=http%3A%2F%2Fwww.dingtalk.com
  ```
- 使用**沉浸式容器**打开普通页面

  在移动端，该链接将以沉浸式容器（默认高度为屏幕的 83%）打开目标页面；在桌面端，则按`target`定义的行为处理（如侧边栏或工作台）。

  ```
  https://applink.dingtalk.com/page/link?url=http%3A%2F%2Fwww.dingtalk.com&target=panel
  ```

**验证方法**：

为确认目标页面是否正确打开，请参考以下验证方式：

1. **界面反馈观察**：

   - 移动端检查是否以全屏或半屏面板展示目标页面；
   - 桌面端确认是否在预期区域（如侧边栏、工作台）打开。
2. **日志调试**：

   - 在 H5 页面中添加 `console.log` 输出加载状态；
   - 使用钉钉开发者工具（DevTools）查看网络请求与跳转过程。
3. **错误排查**：

   - 若页面未正常打开，请检查 URL 是否已正确编码。
