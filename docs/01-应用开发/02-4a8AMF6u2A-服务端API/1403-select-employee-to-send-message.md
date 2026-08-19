---
title: "选择员工发送消息"
source_url: "https://open.dingtalk.com/document/development/select-employee-to-send-message"
namespace: "development"
slug: "select-employee-to-send-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 会话相关 > 选择员工发送消息"
doc_id: "tC3ovCeaMZ"
updated_at: "2026-01-22 20:17:46"
---

> Source: https://open.dingtalk.com/document/development/select-employee-to-send-message
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 会话相关 > 选择员工发送消息
> Updated: 2026-01-22 20:17:46

# 选择员工发送消息

本文档介绍通过 AppLink 协议打开“选择员工”页面并触发消息发送功能的相关说明。该能力适用于企业内部自建应用，帮助开发者在钉钉客户端中快速唤起选人组件，并预置消息内容进行发送。

## **使用场景**

在企业内部应用中，当需要用户从组织架构中选择一个或多个员工并发送特定消息时，可通过本 AppLink 协议直接跳转至“选择员工”界面，支持预设消息内容和操作场景，提升交互效率。

典型业务场景包括：

- 发送工作通知或提醒
- 快速转发审批、日志等内容
- 自定义消息模板的一键分享

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | 不支持 | 不支持 | ≥6.5.50 | ≥6.5.50 |

## **协议**

```
https://applink.dingtalk.com/page/open_user_select
```

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/open\_user\_select | wnd\_caption | 是 | 选人窗口的标题。 |
| url\_param | 是 | 业务参数，JSON格式，需要encode处理。  **该参数内包含两个key：**   - sengMsgScene：场景参数，必传且固定传true。 - defaultMsg：默认发送的消息内容，非必填。 |

> **[!NOTE]**
>
> `url_param`是必填的业务参数，需传入一个 JSON 字符串，并对其进行标准 URL 编码（推荐使用`encodeURIComponent`方法处理）。

#### 编码规范

- 原始 JSON 字符串应使用 UTF-8 编码
- 整个字符串需经`encodeURIComponent()`处理后再拼接到 URL 中
- 示例工具方法（JavaScript）：

  - url\_param参数原始 JSON：

    ```
    {"sendMsgScene":true,"defaultMsg":"Hello"}
    ```
  - url\_param参数URL 编码后：

    ```
    %7B%22sendMsgScene%22%3Atrue%2C%22defaultMsg%22%3A%22Hello%22%7D
    ```

## **使用示例**

```
https://applink.dingtalk.com/page/open_user_select?wnd_caption=选人组件发送消息&url_param=%7B%22sengMsgScene%22%3Atrue%2C%22defaultMsg%22%3A%22%E4%BD%A0%E5%A5%BD%22%7D
```

- `wnd_caption=选人组件发送消息`：设置弹窗标题为“选人组件发送消息”。
- `sendMsgScene=true` 表示进入消息发送流程。
- `defaultMsg=你好`（UTF-8 编码后为`%E4%BD%A0%E5%A5%BD`）作为默认消息内容。

## 常见问题

**Q1：为什么点击链接没有反应？**

A：请检查客户端版本是否符合要求（macOS/Windows ≥6.5.50），并确认应用已正确配置消息权限。

**Q2：defaultMsg 中中文乱码怎么办？**

A：请确保对整个 JSON 字符串使用 UTF-8 编码后再进行 URL 编码，不可仅编码部分内容。

**Q3：如何调试 AppLink 是否生效？**

A：建议在浏览器地址栏直接粘贴完整 URL 测试跳转效果，或通过 H5 页面 `<a href="...">` 标签模拟点击。
