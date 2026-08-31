---
title: "添加接口调用权限"
source_url: "https://open.dingtalk.com/document/development/add-api-permission"
namespace: "development"
slug: "add-api-permission"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "API 调用指南 > 申请 API 权限 > 添加接口调用权限"
doc_id: "gbzpopAqPD"
updated_at: "2026-07-02 10:35:03"
---

> Source: https://open.dingtalk.com/document/development/add-api-permission
> Path: 应用开发 / 服务端 API / API 调用指南 > 申请 API 权限 > 添加接口调用权限
> Updated: 2026-07-02 10:35:03

# 添加接口调用权限

调用钉钉服务端接口前，需要先添加所需接口的调用权限，应用创建后，系统默认添加身份验证和消息通知接口权限。鼓励应用使用尽可能多的接口，实现跟钉钉核心能力的全面互通。

## 适用对象

本文档适用于在钉钉开放平台开发的企业内部应用、第三方企业应用和第三方企业应用开发者。

- **企业内部应用**：由企业自主开发并仅供本企业使用的应用，适用于组织内部系统集成场景。
- **第三方企业应用**：由ISV（独立软件开发商）开发，供多个企业客户安装使用的服务型应用。
- **第三方个人应用**：产品方案商开发者开发，提供给钉钉上个人用户使用的应用。

不同应用类型在权限申请、审批流程及接口可用性方面可能存在差异，请根据实际应用类型参考对应操作指引。

## 功能概述

调用钉钉服务端接口前，必须为应用添加对应的接口调用权限。应用创建后，系统默认会授予部分基础权限。建议根据业务需求合理申请所需接口权限，实现与钉钉核心能力的深度集成。

接口权限以**应用为维度**进行授权，各应用之间权限相互独立。即使同一企业的多个应用需要调用相同接口，也需分别在各自应用中单独申请。

例如：企业内同时拥有 A、B 两个应用，即使应用 A 已具备通讯录读取权限，应用 B 若要访问通讯录数据，仍需单独申请“通讯录”相关权限，操作流程与应用 A 一致。

> **[!IMPORTANT]**
>
> 并非所有接口均可直接开通。部分接口属于非公开开放能力，需提交审批并通过审核后方可使用；另有部分高级接口可能涉及付费或特定资质要求，请以具体接口文档中的使用范围说明为准。

## 前置条件

在进行接口权限配置前，请确保满足以下条件：

1. 应用类型为**企业内部应用**、**第三方企业应用或第三方个人应用**，且已在[开发者后台](https://open-dev.dingtalk.com/)完成创建。
2. 当前登录账号具备该应用的管理权限（通常为企业管理员或应用负责人）。
3. 企业已完成认证（部分特殊接口需企业实名认证后方可申请）。
4. 已获取并妥善配置应用的`AppKey`和`AppSecret`，用于调用API的身份验证。

## 添加普通接口调用权限

适用于大多数公开开放的服务端API，可直接在开发者后台自助申请。

操作流程：

1. 在接口文档中，复制目标接口文档中权限模块的权限点。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3079592871/p1003940.png)
2. 登录[开发者后台](https://open-dev.dingtalk.com/)，在**应用开发**页面，单击目标应用进入应用详情页面。

   ![p256853](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8413787161/p261754.png)
3. 在应用详情页，单击**权限管理**，搜索复制的权限点，单击**立即开通**即可。

   ![新教育接口申请](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3079592871/p360897.png)

## 添加特殊接口调用权限

针对非公开开放的敏感或行业专用接口，需经过钉钉方人工审批后方可启用。

操作流程：

1. 在接口文档中，复制目标接口文档中权限模块的权限点。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3079592871/p1003940.png)
2. 管理员登录[开发者后台](https://open-dev.dingtalk.com/)。
3. 在**应用开发**页面，单击目标应用进入应用详情页面。

   ![p256853 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8413787161/p261754.png)
4. 单击**权限管理**，选择需要添加的特殊接口，单击**立即开通**，填写申请说明，最后单击**申请**。

   > **[!NOTE]**
   >
   > - 接口调用权限申请会由对应接口的钉钉小二进行审批，审批一般会在一个工作日内完成，审批通过后状态变为**已开通**。
   > - 若申请被拒绝，可在**申请栏**中定位到该权限条目，将鼠标悬停于**审核未通过**标签上查看具体驳回原因，并根据反馈优化后重新提交。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3079592871/p1084470.png)

## **无权限报错的解决办法**

> **[!NOTE]**
>
> 此解决方法目前仅限于调用[新版服务端API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)时适用。

当调用新版API返回 `403` 错误时，响应体中会包含详细的权限缺失信息：

```
{
  "Code": "Forbidden.AccessDenied.AccessTokenPermissionDenied",
  "StatusCode": 403,
  "Message": "code: 403, 没有调用该接口的权限 request id: 8197EFxxxx59D33E58",
  "Data": "{\"AccessDeniedDetail\":{\"requiredScopes\":[\"Contact.Org.Read\"]},\"Code\":\"Forbidden.AccessDenied.AccessTokenPermissionDenied\",\"HostId\":\"dingtalk-inner.aliyuncs.com\",
  \"Message\":\"没有调用该接口的权限\",\"Recommend\":\"https://next.api.aliyun.com/troubleshoot?q=Forbidden.AccessDenied.AccessTokenPermissionDenied\\u0026product=dingtalk\",
  \"RequestId\":\"8197Exxxx88C759D33E58\",\"statusCode\":403}",
  "Stack": null,
  "Description": "\u003cni\u003e",
  "AccessDeniedDetail": {
    "requiredScopes": [
      "Contact.Org.Read"
    ]
  }
}
```

应用调用接口时返回提示“没有调用该接口的权限”，解决步骤：

1. 提取错误响应中 `AccessDeniedDetail`中的`requiredScopes` 字段的值，即为目标接口所需的权限点 Code。
2. 在当前应用的权限管理页面，搜索该权限点Code后，申请开通对应接口权限。

   > **[!IMPORTANT]**
   >
   > 第三方企业应用在接入[统一授权套件](0010-unified-licensing-suite-sdk.md)时，权限点Code作为的`rpcScope`或`fieldScope`参数值。

   ![iShot_2023-03-28_16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3079592871/p611374.png)
