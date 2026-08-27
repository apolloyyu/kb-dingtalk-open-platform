---
title: "实现文本内容翻译"
source_url: "https://open.dingtalk.com/document/development/translation-of-text-content"
namespace: "development"
slug: "translation-of-text-content"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > AI > 使用教程 > 实现文本内容翻译"
doc_id: "IhtAgkMji2"
updated_at: "2026-07-20 09:21:34"
---

> Source: https://open.dingtalk.com/document/development/translation-of-text-content
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > AI > 使用教程 > 实现文本内容翻译
> Updated: 2026-07-20 09:21:34

# 实现文本内容翻译

本文档指导开发者通过企业内部应用调用钉钉AI文本翻译API，完成文本内容翻译。

## **前置条件**

- 企业已在钉钉完成实名认证；
- 开发者账号具备该企业后台管理权限；
- 服务端网络可正常访问 `https://open.dingtalk.com`。

【验证与调试】

- 调用服务端API-[钉钉文本翻译](1009-dingtalk-translation.md)接口后，实现文本内容翻译。

## 流程简介

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二：获取AppKey和AppSecret（用于后续换取组织级access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

步骤三：[申请AI接口权限](0003-add-api-permission.md)，搜索“AI”，申请相应权限。

步骤四：调用[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口，获取应用访问凭证access\_token（有效期2小时，建议服务端缓存并自动刷新。

步骤五：调用服务端API-[钉钉文本翻译](1009-dingtalk-translation.md)接口，实现文本内容翻译。

## 步骤一：创建企业内部应用

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二：获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三：添加接口权限

[申请AI接口权限](0003-add-api-permission.md)，搜索“AI”，申请相应权限。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527257.png)

## 步骤四：获取应用访问凭证accessToken

根据步骤二中的AppKey和AppSecret，调用[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取组织级access\_token。

## 步骤五：调用服务端AI相关API

调用服务端API-[钉钉文本翻译](1009-dingtalk-translation.md)接口，实现文本内容的翻译。

### **请求示例代码**

```
curl -X POST 'https://oapi.dingtalk.com/topapi/ai/mt/translate' \
- H 'access_token: <your_org_access_token>' \
- H 'Content-Type: application/json' \
- d '{
  "source_language": "zh",
  "target_language": "en",
  "query": "你好，世界！"
}'
```
