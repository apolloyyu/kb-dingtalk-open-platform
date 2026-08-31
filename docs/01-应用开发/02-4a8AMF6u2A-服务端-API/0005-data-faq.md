---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/data-faq"
namespace: "development"
slug: "data-faq"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "API 调用指南 > 申请 API 权限 > 常见问题"
doc_id: "iov7RChVeD"
updated_at: "2026-08-07 14:50:54"
---

> Source: https://open.dingtalk.com/document/development/data-faq
> Path: 应用开发 / 服务端 API / API 调用指南 > 申请 API 权限 > 常见问题
> Updated: 2026-08-07 14:50:54

# 常见问题

本文介绍企业内部应用的开发流程与权限管理相关的常见问题，适用于使用钉钉开放平台进行应用开发的企业开发者。内容主要面向企业管理员及具备开发权限的技术人员。

## **什么是企业授权应用**

企业授权应用属于组织维度的应用，它是钉钉早期版本的一种应用形式。要使用这类应用，你需要根据企业的唯一标识（企业ID，即CorpId）和安全密钥（企业密钥，即CorpSecret）来生成专用的调用凭证，你可以通过生成的调用凭证接入并使用OpenAPI、Webhook和Stream等多种开发能力。

> **[!NOTE]**
>
> 查看和操作企业授权调用的权限仅限于企业管理员，其他成员无法进行此类操作。

## **什么是企业授权调用**

登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，单击**更多** > **基本信息** > [开发信息（旧版）](https://open-dev.dingtalk.com/fe/old#/corpAuthInfo)，开发者可以找到并记录企业标识（CorpId）和企业密钥（CorpSecret）。使用这两项信息，开发者能够生成专用的调用凭证，该凭证用于访问 OpenAPI 接口，这一过程称为企业授权调用。

> 这是早期开放平台的历史遗留产品，如果需要，建议采用企业内部应用的方式调用 OpenAPI。详情参考[获取企业内部应用访问凭证](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)。

## **如何停止企业授权调用**

由于企业密钥（CorpSecret）不支持直接删除，若需停用企业授权调用功能，可通过修改出口 IP 白名单实现逻辑禁用。

**操作路径**：登录开发者后台 → 应用管理 → 对应应用 → 安全设置 → 修改出口IP地址。

**具体步骤**：

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 在应用列表中选择目标应用，进入详情页。
3. 点击 **安全设置**。
4. 在“出口IP地址”字段中填入一个无效的公网 IP 地址（如 `0.0.0.0`）。
5. 单击【保存】按钮完成设置。

> **说明**： 设置无效 IP 后，外部服务将无法通过原有凭证正常调用接口，从而达到停止授权调用的效果。

## 常见问题排查

- **在工作台无法找到企业内部应用**

  答：遇到工作台中找不到相关应用的问题时，可按照如下步骤排查：

  - 确认当前工作台所对应的企业是否与应用所属企业保持一致。
  - 确认应用是否已发布。请管理员至[开发者后台](https://open-dev.dingtalk.com/#/)**> 对应应用 > 版本管理和发布**中确认应用是否处于已发布状态。
  - 确认应用可使用范围。请管理员至[开发者后台](https://open-dev.dingtalk.com/#/)**> 对应应用 > 版本管理和发布**中确认无法找到应用的用户是否在可使用范围中。
- **小程序开发工具调试内部应用提示“抱歉，你不在应用的可使用范围内，请联系管理员修改配置”**

  答：遇到调试内部应用报上述提示的可能原因包括但不限于以下情况：

  - 调试该内部应用的人员不在开发人员列表中。需在[开发者后台](https://open-dev.dingtalk.com/#/)**> 对应应用 > 人员管理**中设置开发人员。
  - 未对该内部应用上传版本。需确保在小程序开发工具中上传该应用的版本，其次在[开发者后台](https://open-dev.dingtalk.com/#/)**> 对应应用 > 版本管理与发布**中发布版本。
  - [开发者后台](https://open-dev.dingtalk.com/#/)**> 对应应用 > 版本管理与发布 > 可使用范围**中未设置该人员。

    > **[!NOTE]**
    >
    > 内部应用小程序需在小程序开发工具上传过版本且在版本管理与发布中发布版本后，才会显示可使用范围。
- **内部微应用及小程序没有AppKey和AppSecret**

  答：创建好的应用未显示AppKey和AppSecret的原因可能如下:

  - 在开发者后台创建内部应用时，如下图所示，选择的开发方式为**委托商服务开发，**导致应用管理中未显示。

    > **[!NOTE]**
    >
    > 若实际上无需委托开发，请选择**企业自主开发**。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3036434661/p495317.png)
  - 非应用创建者，没有相关权限，无法查看AppKey和AppSecret。需联系企业主管理员，在[钉钉管理后台](https://oa.dingtalk.com/#/welcome) **> 安全与权限 > 权限管理**页面，添加对应的应用管理权限。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8281977661/p510150.png)
