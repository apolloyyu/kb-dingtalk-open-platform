---
title: "创建客户端插件"
source_url: "https://open.dingtalk.com/document/development/creating-a-client-plug-in-1"
namespace: "development"
slug: "creating-a-client-plug-in-1"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "操作指南 > 创建客户端插件"
doc_id: "ZPH5p71x9r"
updated_at: "2026-05-22 18:17:57"
---

> Source: https://open.dingtalk.com/document/development/creating-a-client-plug-in-1
> Path: 专属版客户端插件 / 功能介绍 / 操作指南 > 创建客户端插件
> Updated: 2026-05-22 18:17:57

# 创建客户端插件

本文重点介绍了如何使用平台创建客户端专属插件。

## **前提条件**

1. 组织必须为[钉钉专属版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpages.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FcURBZvRQmHBRaio6srxU5%3Fwh_ttid%3Dphone%26channel%3D$%26corpId%3D$&web_wnd=general&width=480&height=800)，申请权益中请包括**App定制打包**和**专属插件**功能。
2. 拥有组织的[钉钉管理后台](https://oa.dingtalk.com/#/welcome)的登录权限。
3. 需完成插件开发流程：

   - [开发 Android 插件](../02-sakFIe9HDV-Android-插件/0001-process-overview.md)
   - [开发 iOS 插件](../03-gh7c55BOlV-iOS-插件/0001-an-overview-of-the-exclusive-client-plugin-process.md)
   - [创建插件工程](../04-ooCjrSfXpn-HarmonyOS-插件/0001-create-plug-in-project.md)
   - [开发 Windows 插件](../05-9GcTDwdGCc-Windows-插件/0001-create-a-windows-lug-in-project.md)

## **操作步骤**

1. 登录[钉钉企业管理后台](https://oa.dingtalk.com/)，单击**钉钉专属版** > **App定制** > **专属插件** > **新增插件** 。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5715628171/p803491.png)
2. 填写插件信息，单击**创建插件**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5715628171/p803492.png)

   | **字段** | **填写说明** |
   | --- | --- |
   | 插件名称 | 插件对应的业务名称，比如\*\*安全沙箱、\*\*水印相机等。 |
   | 所属端 | 请创建需要的平台，包括Android、iOS、Windows、Mac等。 |
   | BundleID | 平台用于识别插件身份的ID，需与开发插件时定义的 BundleId 保持一致。  **[!IMPORTANT]**  - 假如开发人员已经提前定义，请使用开发人员定义的值。 - 为了避免重复，我们建议采用类似“公司\_产品”的格式填写。**支持字母、数字、下划线，请勿使用其他特殊字符**。 - 如果插件是多端的（比如Android、iOS），请务必使用相同的值。 |
   | 描述信息 | 简要描述插件的功能。 |

创建完成后，在**专属插件列表**中看到我们新创建的插件卡片。

## **后续步骤**

客户端插件创建完成后，你需要[上传并发布插件](0003-upload-and-publish-plug-ins-1.md)。
