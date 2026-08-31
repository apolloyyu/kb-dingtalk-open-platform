---
title: "获取应用的API访问凭证"
source_url: "https://open.dingtalk.com/document/development/used-application-authorization"
namespace: "development"
slug: "used-application-authorization"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 访问凭证 > 获取应用的API访问凭证"
doc_id: "ZLtGgNZmXZ"
updated_at: "2026-01-22 20:44:05"
---

> Source: https://open.dingtalk.com/document/development/used-application-authorization
> Path: 应用开发 / 服务端 API / 认证与授权 > 访问凭证 > 获取应用的API访问凭证
> Updated: 2026-01-22 20:44:05

# 获取应用的API访问凭证

本文适用于企业内部自建应用和第三方企业应用，开发者在调用钉钉开放平台OpenAPI前，需先获取应用的访问凭证（accessToken）。该凭证是调用大多数服务端API的身份凭据，有效期为2小时，建议缓存并定期刷新以保障接口调用稳定性。

## 步骤一：创建钉钉应用

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/corpeapp)。
2. 单击应用开发，创建企业内部应用或第三方企业应用。
3. 在应用详情页获取应用的Client ID（原应用AppKey/SuiteKey） 和 Client Secret（原应用AppSecret/SuiteSecret）。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9413550071/p739907.png)

## 步骤二：获取应用的访问凭证

调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口或[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口生成accessToken。
