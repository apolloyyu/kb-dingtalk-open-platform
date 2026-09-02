---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/sso-overview"
namespace: "development"
slug: "sso-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 概述"
doc_id: "QKBVgceaQ8"
updated_at: "2026-09-02 18:13:35"
---

> Source: https://open.dingtalk.com/document/development/sso-overview
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 概述
> Updated: 2026-09-02 18:13:35

# 概述

“免登”是指用户进入应用后，无需输入钉钉用户名和密码，应用程序可自动获取当前用户身份，并以此身份登录系统的流程。通过免登机制，开发者可以实现无缝的身份认证体验，提升用户使用便捷性与安全性。

## 适用对象

本文档适用于以下类型的应用开发者：

- **企业内部应用**：由企业自行开发并仅供本企业员工使用的应用。
- **第三方企业应用（ISV 应用）**：由第三方服务商开发并提供给多个企业客户安装使用的 SaaS 类应用。
- **应用管理后台系统**：需要企业管理员在钉钉管理后台直接访问的配置与管理系统。

# 支持的免登场景

- [网页应用（H5微应用）免登](0018-enterprise-internal-application-logon-free.md)
- [应用管理后台免登](0022-log-on-site-application-management-backend.md)
- [实现网页方式登录应用（登录第三方网站）](0019-tutorial-obtaining-user-personal-information.md)

  - 浏览器内实现

    - 扫码登录
    - 使用钉钉账号密码方式登录

## 企业内部应用免登

当企业开发者开发了一个企业内部应用时，企业员工在钉钉内使用该应用，无需输入账户密码即可自动登录所开发的系统。

免登步骤，详情参见[网页应用（H5微应用）免登](0018-enterprise-internal-application-logon-free.md)。

| 步骤 | 说明 |
| --- | --- |
| 步骤一：获取免登授权码。 | PC端暂不支持小程序开发，如果要开发PC端应用，需使用**微应用开发**方式。 |
| 步骤二：获取access\_token。 | 调用接口[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。 |
| 步骤三：获取用户userid。 | 调用接口[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获取用户的userid。 |
| 步骤四：获取用户详情。 | 调用接口[查询用户详情](0056-query-user-details.md)获取用户详情信息。 |

## 第三方企业应用免登

在钉钉上开发的第三方企业应用，作为公开的云端SaaS服务可以让企业客户安装使用。管理员开通第三方企业应用后，企业员工在钉钉内使用该第三方企业应用时，无需输入账号密码便可直接登录该应用。

免登步骤，详情参见[第三方企业应用免登流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-logon-free)。

| 步骤 | 说明 |
| --- | --- |
| 步骤一：获取免登授权码 | PC端暂不支持小程序开发，如果要开发PC端应用，需使用**微应用开发**方式。 |
| 步骤二：获取access\_token | 调用接口[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)。 |
| 步骤三：获取用户userid。 | 调用接口[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获取用户的userid。 |
| 步骤四：获取用户详情。 | 调用接口[查询用户详情](0056-query-user-details.md)获取用户详情信息。 |

## 应用管理后台免登

当开发的应用需要企业管理员在[钉钉管理后台](https://oa.dingtalk.com/)对应用进行一些设置和管理功能时，你需要开发一套应用的后台管理系统，管理员在[钉钉管理后台](https://oa.dingtalk.com/)直接点应用管理后台，便可免输入账户密码实现自动登录你的应用管理后台系统。

免登步骤，详情参见[应用管理后台免登](0022-log-on-site-application-management-backend.md)。

| 步骤 | 说明 |
| --- | --- |
| 步骤一：获取免登授权码**。** | 当企业管理员登录[钉钉管理后台](http://oa.dingtalk.com/)后，点击**工作台**中的应用，会自动跳转到应用的后台地址，钉钉会把code参数追加到此URL地址中。请保存code参数值，在后面的步骤会用到，如下图：image.png |
| 步骤二：获取应用后台免登的access\_token。 | 调用接口[获取微应用后台免登的accessToken](0025-obtain-the-access-token-of-the-micro-application-background-without-log-on.md)获取应用后台免登的access\_token**。** |
| 步骤三：获取应用管理员的身份信息。 | 使用**步骤一**获取到的code和**步骤二**获取到的access\_token换取应用管理员的身份信息，详情请参考[获取应用管理后台免登的用户信息](0026-obtains-the-identity-of-an-application-administrator.md)。 |
