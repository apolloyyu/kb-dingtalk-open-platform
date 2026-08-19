---
title: "创建钉钉组织"
source_url: "https://open.dingtalk.com/document/development/create-dingtalk-organization"
namespace: "development"
slug: "create-dingtalk-organization"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 创建钉钉组织"
doc_id: "H8O6XaoTrX"
updated_at: "2026-01-22 20:17:48"
---

> Source: https://open.dingtalk.com/document/development/create-dingtalk-organization
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 创建钉钉组织
> Updated: 2026-01-22 20:17:48

# 创建钉钉组织

本文档介绍如何通过 AppLink 协议在移动端快速发起创建钉钉组织的请求，适用于希望集成该功能的企业内部应用或第三方企业应用开发者。使用此协议可提升组织开通效率，用户无需手动进入设置页面，通过扫码即可直接跳转至“创建组织”流程。

## **使用场景**

本协议用于在移动端快速发起创建钉钉组织的请求。用户无需手动填写企业信息，可通过扫码直接跳转至组织创建页面，提升开通效率。

例如，当企业客户首次开通钉钉服务时，ISV 或系统集成商可通过生成专用跳转链接，引导主账号持有者快速进入组织创建页面。结合前端引导页面，可实现“扫码—填写信息—完成创建”的一站式体验，避免用户在多个界面间切换。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验协议跳转效果：

![qrcode (15)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8929375761/p556484.png)

如上图所示，扫描后系统将自动打开钉钉并跳转至“创建组织”页面。整个过程无需手动输入参数，所有初始化操作由客户端自动完成。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/createorg
```

## **字段说明**

- 确保目标设备已安装钉钉客户端并使用主账号登录。
- 页面跳转后，根据提示完成组织名称、行业类型、规模等基本信息填写。
- 提交申请后，系统将校验企业资质并发送审核结果通知。
- 若点击链接无响应，请检查是否安装钉钉、网络连接是否正常、客户端版本是否≥6.5.45。
