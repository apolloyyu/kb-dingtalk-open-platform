---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/authorization-overview"
namespace: "development"
slug: "authorization-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 访问凭证 > 概述"
doc_id: "8b48PPPMaj"
updated_at: "2026-01-22 21:24:00"
---

> Source: https://open.dingtalk.com/document/development/authorization-overview
> Path: 应用开发 / 服务端 API / 认证与授权 > 访问凭证 > 概述
> Updated: 2026-01-22 21:24:00

# 概述

在调用 DingTalk OpenAPI 之前，应用必须从钉钉开放平台获取访问凭证（accessToken）。该凭证包含应用的身份信息及其对钉钉资源的访问权限，是调用 API 的必要认证凭据。

## **背景说明**

为了帮助开发者清晰理解不同场景下的身份认证机制，本文档将系统介绍钉钉开放平台支持的四种 accessToken 类型、其适用对象、权限范围及使用方式。同时提供完整的操作流程指引和关键注意事项，确保开发者能够正确、高效地完成接口调用准备。

## 权限说明

钉钉开放平台通过两种权限模型来管理应用对资源的访问控制，确保安全与灵活性兼顾：

> **[!NOTE]**
>
> 无论使用哪种权限类型调用DingTalk OpenAPI，都需要先获取对应权限类型的访问凭证accessToken。

### **类型一：****用户**身份访问凭证

- **定义**：用户身份访问凭证（委托权限），即需要用户授权后，应用代表登录用户调用DingTalk OpenAPI对资源进行操作。
- **特点**：

  - 用户需主动授权，同意应用访问其个人数据或代表其执行操作。
  - 调用 API 时使用用户的`accessToken`，操作结果受用户权限限制。
  - 适用于涉及用户私有数据的场景，如读取个人日程、个人手机号等。

### **类型二：**应用身份访问凭证

- **定义**：应用身份访问凭证（应用权限），应用身份访问凭证适用于不需要用户登录的应用程序。安装应用时，管理员可以预先授予权限。
- **特点**：

  - 应用可独立于用户身份调用 API，直接访问组织级资源。
  - 使用企业内部应用或第三方应用的`accessToken`。
  - 适用于后台任务、批量处理、自动化运维等场景。

## 访问凭证accessToken

访问凭证（accessToken）是由钉钉开放平台颁发的，用来校验调用者的身份信息，确保调用者具有要执行的操作的权限。

钉钉开放平台目前提供以下四类 accessToken，分别对应不同的应用场景和权限层级：

> **[!IMPORTANT]**
>
> 使用不同的accessToken调用同一个API，可能获取的数据有所不同，详情参考具体的API文档说明。

| 授权凭证 | 应用场景 | 获取方式 |
| --- | --- | --- |
| 用户accessToken | 需要登录用户授权的应用。 | [获取用户token](0032-obtain-user-token.md) |
| 企业内部应用accessToken | 企业内部应用调用服务端API获取应用资源。 | [获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md) |
| 第三方企业应用accessToken | 第三方企业应用或定制应用调用服务端API获取应用资源。 | [获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md) |
| 第三方企业应用suiteAccessToken | 获取第三方企业应用的信息。 | [获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md) |

## 如何使用访问凭证accessToken

要调用DingTalk OpenAPI，请将访问令牌作为Bearer令牌附加到HTTP请求中的Authorization标头中。例如：

```
GET https://api.dingtalk.com/v1.0/me/ HTTP/1.1
Host: api.dingtalk.com
Authorization: Bearer EwAoA8lxxxx=
```

完整操作请参考：

- 获取登录用户的访问凭证：参考[获取登录用户的访问凭证](0029-obtain-identity-credentials.md)文档教程。
- 获取无登录用户的访问凭证：参考[获取应用的API访问凭证](0030-used-application-authorization.md)文档教程。

## **注意事项**

| 注意事项 | 说明 |
| --- | --- |
| 🔐 Client Secret 泄露风险 | 严禁在前端代码、客户端或日志中打印 Secret |
| 🕒 accessToken 有效期 | 默认 7200 秒，需实现自动刷新机制 |
| 🧩 接口支持的 accessToken 类型 | 必须查阅具体接口文档确认，不可混用 |
