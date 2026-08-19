---
title: "打开选择联系人发起电话"
source_url: "https://open.dingtalk.com/document/development/open-select-contact-initiating-phone"
namespace: "development"
slug: "open-select-contact-initiating-phone"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开选择联系人发起电话"
doc_id: "AtXbRmQAQo"
updated_at: "2026-01-22 20:17:50"
---

> Source: https://open.dingtalk.com/document/development/open-select-contact-initiating-phone
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开选择联系人发起电话
> Updated: 2026-01-22 20:17:50

# 打开选择联系人发起电话

通过 AppLink 协议，可实现从链接或二维码快速拉起钉钉客户端的“选择联系人发起电话”页面。用户无需手动进入通讯录，即可高效选择联系人并发起语音通话。该功能适用于客服系统、企业内部通讯等需要快速拨打电话的业务场景，提升沟通效率和用户体验。

## **使用场景**

用户扫描特定二维码或点击预设链接后，钉钉移动端将自动唤起“选择联系人”界面，支持用户从企业通讯录中选择成员，并立即发起语音通话。

此流程减少了操作路径，特别适合在工单系统、服务台、审批通知等场景中集成，帮助用户一键直连相关人员。

### 适用说明

- 仅限已加入企业的认证用户使用，访客账号无法正常使用该功能。
- 目前仅支持移动端（Android 和 iOS），macOS 与 Windows 客户端暂不支持。

## **扫码体验**

使用移动端钉钉扫描下方二维码，立即体验跳转效果：

> **提示**：请确保当前登录账号为企业成员，且所在组织已启用通讯录权限。

![qrcode (20)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1053375761/p556469.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/directCreateCall
```

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/directCreateCall | title | 否 | 打开选择联系人发起电话页面的标题。 |

## **使用示例**

**参数说明**：

- `title`参数非必填，可根据实际业务需求动态传入，增强上下文识别。
- 示例中 `来自客服系统的紧急呼叫`将显示为页面标题，提升用户认知。

**构造链接**：构造如下完整链接，用于触发拨号流程。

```
https://applink.dingtalk.com/page/directCreateCall?title=来自客服系统的紧急呼叫
```

## **常见问题**

- **无法拉起页面？**

  - 检查客户端版本是否满足最低要求（≥6.5.45）。
  - 确认当前账号属于企业成员且已登录。
  - 检查应用是否已上线或处于调试模式。
- **提示无权限？**

  - 检查当前用户是否有权访问目标联系人。
- **链接无效？**

  - 确保 URL 使用 HTTPS 协议，且拼写正确。
  - 避免使用短链或重定向中间层，建议直接调用原始 AppLink。
