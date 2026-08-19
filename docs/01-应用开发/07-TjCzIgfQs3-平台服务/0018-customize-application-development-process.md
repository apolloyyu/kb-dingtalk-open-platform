---
title: "授权服务商开发定制应用"
source_url: "https://open.dingtalk.com/document/services/customize-application-development-process"
namespace: "services"
slug: "customize-application-development-process"
group: "应用开发"
tab: "平台服务"
breadcrumb: "合作指南 > 产品方案商 > 定制业务的合作指引 > 授权服务商开发定制应用"
doc_id: "JmUb9d4s9Q"
updated_at: "2026-08-19 09:15:40"
---

> Source: https://open.dingtalk.com/document/services/customize-application-development-process
> Path: 应用开发 / 平台服务 / 合作指南 > 产品方案商 > 定制业务的合作指引 > 授权服务商开发定制应用
> Updated: 2026-08-19 09:15:40

# 授权服务商开发定制应用

通过本文你将学会产品方案商开发钉钉企业内部应用的流程。

企业可根据办公需求，基于钉钉的开放能力，开发个性化办公应用供企业内部使用，例如将企业内部的HR、CRM、业务管理等系统接入钉钉。

企业可以选择授权认证的产品方案商进行应用开发。如下图所示，当选择由产品方案商进行开发时，应用的开发和发布全部由产品方案商来完成。

> **[!NOTE]**
>
> 应用的开发与企业自建相同，本文主要介绍应用的创建和发布过程。

![定制服务商开发](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9273251361/p135173.png)

## 准备工作

- 产品方案商已完成产品方案商审核和认证。详情请参考[授权服务商开发定制应用](#)。

  > **[!NOTE]**
  >
  > 非认证的产品方案商无法被企业授权进行开发。
- 企业已与产品方案商确认了应用需求。
- 企业已获取产品方案商的corpId。

## 步骤一：企业创建应用并授权产品方案商

参考以下操作，创建一个小程序应用：

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，然后依次选择**应用开发** >**钉钉应用**，然后在创建应用按钮中选择**委托服务商开发**。

   > **[!NOTE]**
   >
   > 只有管理员和子管理员可登录开发者后台。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0412017871/p255125.png)
2. 在弹窗中选择**小程序**，填写应用的基本信息，然后单击**确定创建**。

   ![p133352](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0412017871/p255131.png)
3. 应用创建后，在**授权产品方案商开发**区域输入产品方案商的CorpId，然后单击**查找服务商**，再单击**点击授权**。

   ![授权服务商](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0412017871/p135198.png)
4. 在弹出的页面，单击**确认并授权**完成服务商开发授权。

## 步骤二：产品方案商配置应用

在企业完成授权后，产品方案商需要登录开发者后台，完成应用的基础配置：

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**定制服务**，在**定制应用**列表选择已授权的应用，然后单击**设置**按钮。

   ![p135202](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5160360261/p255152.png)
3. 单击**开发管理**，然后单击**修改**。根据以下信息配置开发信息，然后单击**保存**。

   - **服务器出口IP**：输入调用钉钉服务端API时使用的IP即企业服务器的公网IP，多个IP请以","隔开，支持带一个\*号通配符的IP格式。
   - **PC端首页地址**（可选）：输入在PC端钉钉工作台上打开本应用的地址。链接地址必须以http或https开头。

     > **[!NOTE]**
     >
     > 如果未填写，在钉钉PC端工作台点击应用图标时，会提示“电脑版暂不支持显示，请用手机钉钉扫描下方二维码查看”。只能在手机钉钉客户端使用该应用。
   - **管理后台地址**（可选）：输入组织管理员在[钉钉管理后台](https://oa.dingtalk.com/)访问该应用的地址。
4. 单击**人员管理**，然后单击**添加人员**添加开发人员。

   > **[!NOTE]**
   >
   > 如果不添加开发人员，开发人员在小程序IDE中则无法关联要开发的应用。
5. 单击**安全中心**，然后单击**添加**添加一个HTTP安全域名。

   当小程序的前端与服务端需要进行网络通信时，需要设置安全域名。小程序前端只能通过已设置的安全域名（或IP）与服务端进行网络通信。当安全域名更新时，需要在[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)新打包上传版本，设置的域名才会生效。

   安全域名是后端服务部署的服务器的公网IP或域名。
6. 单击**版本管理与发布**，然后单击**设置体验组织**加体验组织。

   ![p135209](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5160360261/p255166.png)
7. 单击**凭证与基础信息**查看应用的CustomKey和CustomSecret。

   ![customKey](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2034199951/p135205.png)

## 步骤三：应用开发

应用开发可参考[开发小程序](../01-XOnnmGCTbn-开发指南/0024-optional-develop-a-small-program-server.md)的示例代码。

## 步骤四：应用发布

产品方案商完成应用开发后，需要在IDE中上传开发版本：

1. 在小程序IDE中，单击**上传**，确认小程序版本，然后再次单击**上传**。

   ![上传ide](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2034199951/p135223.png)
2. 登录开发者后台，单击**定制服务**，在**定制应用**列表选择已授权的应用，然后单击设置按钮。

   ![p135202 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5160360261/p255152.png)
3. 单击**版本管理与发布，**然后在开发版本区域**，**选择灰度发布应用或在体验组织内先进行应用体验。

   ![定制应用灰度](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2034199951/p135226.png)
4. 应用完成测试或灰度后，单击**发布**。
