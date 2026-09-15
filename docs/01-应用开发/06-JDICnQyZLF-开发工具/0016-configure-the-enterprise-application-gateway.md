---
title: "企业应用网关配置流程"
source_url: "https://open.dingtalk.com/document/download/configure-the-enterprise-application-gateway"
namespace: "download"
slug: "configure-the-enterprise-application-gateway"
group: "应用开发"
tab: "开发工具"
breadcrumb: "内网穿透工具 > 企业应用网关（正式版） > 企业应用网关配置流程"
doc_id: "1bu1ca1V4j"
updated_at: "2026-09-15 09:35:28"
---

> Source: https://open.dingtalk.com/document/download/configure-the-enterprise-application-gateway
> Path: 应用开发 / 开发工具 / 内网穿透工具 > 企业应用网关（正式版） > 企业应用网关配置流程
> Updated: 2026-09-15 09:35:28

# 企业应用网关配置流程

本文介绍了如何配置企业应用网关。本流程适用于已开通企业应用网关的企业内部H5微应用，暂不支持小程序。

## 准备工作

在开始配置前，请确保满足以下前置条件：

- 企业已在钉钉完成组织认证；
- 已创建企业内部应用或第三方企业应用，并为该应用配置了首页地址；
- 操作人员具备管理员权限，可访问钉钉开发者后台及企业应用网关管理平台；如果未开通，需要使用移动端钉钉扫描下方二维码，并安装**钉钉企业应用网关**应用。

  ![下载二维码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2219082361/p328981.png)
- 若服务器出口IP受限制，需提前将相关IP加入钉钉API调用白名单。

## 流程简介

配置企业应用网关主要包括以下三个步骤：

1. 配置**连通器**。
2. 配置**应用管理**。
3. 配置**访问策略**。

请按顺序依次完成各步骤操作。

## 步骤一，配置连通器

1. 访问[钉钉企业应用网关平台](https://ztna-console.dingtalk.com/#/)。
2. 单击**连通器管理**，在内外网连通器管理页面单击**创建连通器**。

   ![iShot2022-06-08 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p447618.png)

   - **请选择需要安装连通器的服务器系统类型**：推荐使用**Linux**类型服务器。
   - **验证和配置环境**：

     - 请根据以下条件判断当前环境是否满足要求。

       ![iShot2022-06-08 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p447620.png)
     - 在终端输入以下命令，下载安装连通器。

       ```
       wget https://open-dev-resource.oss-cn-beijing.aliyuncs.com/ztna/connector.zip && unzip connector.zip && cd connector && ./start.sh -a endpoint.ztna-dingtalk.com:8021 -k 0061ab22f5ec457ab1aab27a0f17ea30 -s a72631f1aa4797468ecc72e9b6653250fe53817ab0a7899c4ff5d0a5f21f5908
       ```

       成功安装后的效果如下图所示。

       ![iShot2022-06-08 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8361015561/p447637.png)

       下载安装连通器完成后，[钉钉企业应用网关平台](https://ztna-console.dingtalk.com/#/)会出现以下提示，点击启用连通器。

       ![iShot2022-06-08 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p447644.png)

       连通器创建完成后，如下图所示，在连通器管理页面内会出现新增的连通器。

       ![iShot2022-06-08 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p447645.png)
3. 创建连通器组，对连通器进行管理。

   ![iShot2022-06-08 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p447646.png)

## 步骤二，配置应用管理

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com)，打开创建的企业H5微应用，暂不支持小程序。

   如果已有应用，则跳过此步骤。已有应用指已在钉钉开发者后台创建并配置了首页地址的H5微应用。请确保该应用的首页地址已正确配置；如需支持PC端访问，还需同步配置PC端地址。这里的地址是指该应用在开发者后台配置的内网访问首页地址。

   ![企业应用网关-配置应用1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9216349871/p448587.png)
2. 在网关后台，应用管理菜单下，“未配置”应用部分找到该应用，点击进入配置页。

   ![iShot2022-06-13 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p448815.png)
3. 打开配置页，填写应用信息。

   ![iShot2022-06-13 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9216349871/p448816.png)

   | 配置项 | 说明 |
   | --- | --- |
   | 应用名称 | 从开发者后台同步过来，无需修改。 |
   | 内外网连通器/组 | 连通器用来打通内网和公网，使用公网可以访问内网应用。只有内网应用才需要选择。 |
   | 应用域名 | 包括主域名和自定义域名, 应用域名必须以http://或https://开头。  - 主域名是直接访问该应用的域名，主域名必须配置且只有一个。这里从开发者后台同步。 - 自定义域名是企业管理员直接通过自定义域名进行访问该应用，需先该域名[配置信任证书](https://ztna-console.dingtalk.com/#/other)并设置cname记录，指向地址：gw-cname.ztna-dingtalk.com。 |
   | 高级设置 | 高级配置项，具体参考页面说明。 |
4. 检查无误后，点击“完成”按钮，完成配置。此时可以看到开发者后台的应用地址自动更新为网关新地址。

   ![企业应用网关-配置应用1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9216349871/p448587.png)

   ![iShot2022-06-08 11 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p447680.png)

## 步骤三，配置访问策略

> **[!NOTE]**
>
> 完成配置访问策略后，有一个月的试用期。试用期结束后，网关会对其试用者进行收费。

策略管理由企业管理员操作，包括注册策略、修改策略、删除策略、停用策略、启用策略、优先级排序等。

1. 管理员进入应用网关管理后台，点击“策略管理”菜单，然后点击“创建策略”按钮，进入创建策略界面。

   ![企业应用网关-配置访问策略图1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p448592.png)
2. 在策略页面，填写策略信息，配置项如下表。

   | 配置项 | 说明 |
   | --- | --- |
   | 策略名称 | 策略名称，不超过15个字。 |
   | 配置安全策略 | 指命中策略后的动作，包括允许访问和拒绝访问。 |
   | 使用策略的部门/员工 | 策略的适用范围，可以对部门、角色、员工生效，部门+角色+员工总数不能超过100 |
   | 使用策略的应用 | 使用策略的应用 |
   | 策略生效的条件 | 目前支持时间范围限制、网络环境限制和设备类型限制。  - 时间范围限制：策略生效的时间，可以指定日期范围，是否工作日（工作日指周一至周五，不考虑法定节假日），具体时间点。 - 网络环境限制：支持IP范围的限制。 - 设备类型限制：支持IOS、Android、Windows和macOS的限制。 |

   ![iShot2022-06-13 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p448820.png)
3. 点击完成，创建策略。
4. 访问策略创建完成后，在策略列表中可以看到该策略。企业管理员也可以在访问策略列表内管理访问策略，包括注册策略、修改策略、删除策略、停用策略、启用策略、优先级排序等。

   > **[!NOTE]**
   >
   > 新创建的策略默认优先级最低（排在最后），当一个请求同时被多个策略适用时，实际上按照优先级最高的那条策略执行。

   ![iShot2022-06-08 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8216349871/p447694.png)
