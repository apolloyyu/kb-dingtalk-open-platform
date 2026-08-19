---
title: "打开外链管理"
source_url: "https://open.dingtalk.com/document/development/open-the-chain-management"
namespace: "development"
slug: "open-the-chain-management"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开外链管理"
doc_id: "cq708IbsFT"
updated_at: "2026-01-08 20:07:18"
---

> Source: https://open.dingtalk.com/document/development/open-the-chain-management
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开外链管理
> Updated: 2026-01-08 20:07:18

# 打开外链管理

AppLink协议是钉钉提供的统一链接唤起方案，用于从外部应用或网页快速跳转至钉钉客户端内的特定功能页面。通过该机制，开发者可实现无缝集成，直接唤起钉钉云盘的外链管理界面，便于对文件共享权限进行集中配置与管理。

## **使用场景**

本功能主要面向企业管理员和第三方应用开发者，适用于需要批量管理文件外链权限、自动化协同办公流程等业务场景。以下是两个典型的应用案例：

**场景一：企业管理员批量设置外链有效期**

在大型组织中，安全合规要求对敏感文件的外链访问进行严格控制。企业管理员可通过内部管理系统集成AppLink协议，在审批流程完成后自动跳转至钉钉外链管理页面，为多个文件统一设置外链有效期限和访问权限。

流程如下：

1. 管理员登录企业内部文档管理系统；
2. 选择需对外分享的文件组；
3. 系统生成对应AppLink链接（携带预设参数）；
4. 点击“管理外链”按钮，唤起钉钉客户端；
5. 在钉钉中完成外链类型（公开/密码/组织内）、有效期、下载权限等配置。

该流程显著提升操作效率，避免逐一手动配置。

**场景二：第三方协同办公应用自动唤起权限调整界面**

某项目协作SaaS平台允许团队成员上传阶段性成果并对外分享。当客户请求查看最新版本时，项目经理可在平台内点击“更新外链权限”，系统调用AppLink协议直接打开钉钉外链管理页，快速切换为“无需密码、限时可下载”模式。

## **扫码体验**

使用移动端钉钉扫描下方二维码，快速体验：

![qrcode (9)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0533375761/p556448.png)

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | 不支持 | 不支持 |

## **协议**

```
https://applink.dingtalk.com/page/yunpan
```

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/yunpan | route | 是 | 该字段值固定传**externalLink**。 |

## **使用示例**

以下为通过 AppLink 协议唤起钉钉外链管理页面的完整示例：

> **[!NOTE]**
>
> 确保参数正确，特别是 `route=externalLink` 中的键值对需严格匹配，区分大小写。

```
https://applink.dingtalk.com/page/yunpan?route=externalLink
```
