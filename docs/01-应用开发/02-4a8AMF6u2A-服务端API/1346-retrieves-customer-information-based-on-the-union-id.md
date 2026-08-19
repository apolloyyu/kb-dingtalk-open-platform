---
title: "根据unionId获取客户信息流程"
source_url: "https://open.dingtalk.com/document/development/retrieves-customer-information-based-on-the-union-id"
namespace: "development"
slug: "retrieves-customer-information-based-on-the-union-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 使用教程 > 根据unionId获取客户信息流程"
doc_id: "DqQsdnWUet"
updated_at: "2026-07-21 09:26:16"
---

> Source: https://open.dingtalk.com/document/development/retrieves-customer-information-based-on-the-union-id
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 使用教程 > 根据unionId获取客户信息流程
> Updated: 2026-07-21 09:26:16

# 根据unionId获取客户信息流程

本文档介绍了如何调用客户管理相关接口实现获取客户信息的相关流程。首先创建一个企业内部应用，再使用客户管理提供的API和钉钉统一授权套件，实现获取客户信息流程。

## 流程简介

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二：获取AppKey和AppSecret。

步骤三：[申请客户管理接口权限](https://open.dingtalk.com/document/orgapp/apply-for-crm-api-permission)。搜索“CRM”，申请相应的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五：调用服务端客户管理相关API。

1. 调用服务端API-[创建客户群组](1383-crm-create-group.md)接口，创建企业客户群组，获取加入该群组的邀请链接。
2. 根据加入群组的邀请链接，客户添加进该群组内的客户群，并通过公告的方式展示企业系统页面。
3. 企业系统页面使用[统一授权套件](0007-function-description.md)功能，获取访问该页面的用户unionId。
4. 根据unionId，调用服务端API-[查询客户数据](1358-querying-customer-data.md)接口，获取访问系统页面的客户详情信息。

## 步骤一：创建企业内部应用

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二：获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三：添加接口权限

[申请客户管理接口权限](0003-add-api-permission.md)。搜索“CRM”，申请相应的权限。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6617954871/p499403.png)

## 步骤四：获取应用访问凭证accessToken。

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

> **[!NOTE]**
>
> 以下接口均使用新版服务端API接口，服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。

```
public void getAccessToken() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest accessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("din*********hgn")
                .setAppSecret("9G_O************mBkhgGIO");
        GetAccessTokenResponse accessToken = client.getAccessToken(accessTokenRequest);
        System.out.println(JSON.toJSONString(accessToken.getBody()));
    }
```

## 步骤五：调用服务端客户管理相关API。

1. 调用服务端API-[创建客户群组](1383-crm-create-group.md)接口，创建企业客户群组，获取加入该群组的邀请链接。
2. 根据加入群组的邀请链接，客户添加进该群组内的客户群，并通过公告的方式展示企业系统页面。
3. 企业系统页面使用[统一授权套件](0007-function-description.md)功能，获取访问该页面的用户unionId。
4. 根据unionId，调用服务端API-[查询客户数据](1358-querying-customer-data.md)接口，获取访问系统页面的客户详情信息。
