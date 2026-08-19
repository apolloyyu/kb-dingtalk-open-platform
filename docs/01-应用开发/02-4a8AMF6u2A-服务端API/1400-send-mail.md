---
title: "发送邮件"
source_url: "https://open.dingtalk.com/document/development/send-mail"
namespace: "development"
slug: "send-mail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 发送邮件"
doc_id: "TrehoZ0XcM"
updated_at: "2026-01-22 20:17:45"
---

> Source: https://open.dingtalk.com/document/development/send-mail
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 发送邮件
> Updated: 2026-01-22 20:17:45

# 发送邮件

通过 AppLink 协议可以快速唤起钉钉客户端并打开邮件撰写页面，适用于 H5 应用或外部系统中需要快捷发送邮件的集成场景。该协议不携带参数，直接触发默认行为，便于在审批通过后快速发起邮件通知、任务完成提醒等轻量级消息触达。

## **使用场景**

- 在 H5 页面中嵌入“发送邮件”按钮，用户点击后自动拉起钉钉客户端并进入邮件撰写界面。
- 外部业务系统（如 OA、CRM）中，在流程节点完成后提供一键发邮件功能，提升操作效率。
- 审批通过后自动跳转至邮件撰写页，便于用户向相关方发送结果通知。
- 第三方应用中集成邮件入口，作为辅助沟通方式补充协作能力。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验协议效果：

![qrcode (5)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9409375761/p556510.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/mailcompose
```

## **字段说明**本协议无字段。

**说明**：由于此协议仅用于打开邮件撰写页，默认使用当前用户身份，不支持携带收件人、主题等参数，因此无需定义字段。

**验证方式**：

- **客户端行为验证**：点击链接后，若成功唤起钉钉客户端并跳转至邮件撰写页面，则表示协议调用成功。
- **失败排查方向**：

  - 检查是否在非钉钉环境中调用（如微信、普通浏览器）。
  - 确认客户端版本是否满足最低要求（≥6.5.45）。
  - 确保网络可访问 `https://applink.dingtalk.com`。
