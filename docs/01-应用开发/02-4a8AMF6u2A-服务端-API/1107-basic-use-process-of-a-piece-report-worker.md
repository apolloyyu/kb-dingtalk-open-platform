---
title: "计件报工基本使用流程"
source_url: "https://open.dingtalk.com/document/development/basic-use-process-of-a-piece-report-worker"
namespace: "development"
slug: "basic-use-process-of-a-piece-report-worker"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 制造业 > 使用教程 > 计件报工基本使用流程"
doc_id: "5XA1zinyHL"
updated_at: "2026-07-20 09:21:38"
---

> Source: https://open.dingtalk.com/document/development/basic-use-process-of-a-piece-report-worker
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 制造业 > 使用教程 > 计件报工基本使用流程
> Updated: 2026-07-20 09:21:38

# 计件报工基本使用流程

本文档介绍了如何调用制造业相关接口实现计件报工操作的相关流程。首先创建一个企业内部应用，再使用制造业提供的API，实现创建计件工单、员工报工流程。

## 流程简介

步骤一，登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二，获取AppKey和AppSecret。

步骤三，[申请制造业接口权限](0003-add-api-permission.md)，申请相应的权限。

步骤四，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五，钉钉应用市场开通**计件日结**应用并完成配置。

步骤六，调用服务端制造业相关API。

1. 调用服务端API-[计件报工](1108-riqing-monthly-settlement-piece-rate-reporting-interface.md)接口，产生报工记录。
2. 调用服务端API-[查询计件报工数据](1109-riqing-monthly-settlement-query-interface-for-piece-rate-reporting.md)接口，查询报工的详情信息。

## 步骤一，创建企业内部应用

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二，获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三，添加接口权限

申请`制造业计件报工数据写权限`和`制造业计件报工数据读权限`。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8940154871/p1087585.png)

## 步骤四，获取应用访问凭证accessToken

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

## 步骤五，开通计件日结应用并完成配置

1. 钉钉应用市场搜索开通**计件日结**应用。

   以PC端开通**计件日结**应用为例：钉钉PC客户端-工作台-应用中心-搜索“计件日结”-开通。

   ![iShot2022-02-28 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2978726461/p409726.png)
2. **计件日结**应用-计件报工内点击新建工单，首次新建工单，需要创建模板。请按照如下流程配置：

   1. 点击**新建工单**

      ![iShot2022-02-28 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8940154871/p409733.png)
   2. 点击**新建模板**

      ![iShot2022-02-28 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8940154871/p409734.png)
   3. 模板创建完成后的效果如图，并点击添加任务

      ![iShot2022-02-28 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8940154871/p409738.png)
   4. 添加任务后，工单创建完成，效果如下图所示：

      ![iShot2022-02-28 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8940154871/p409750.png)
3. 工单创建完成后，再调用服务端接口进行

## 步骤六，调用服务端制造业接口

- 根据创建的工单编号，调用服务端API-[计件报工](1108-riqing-monthly-settlement-piece-rate-reporting-interface.md)接口，对此工单进行报工，得到报工id。

  > **[!NOTE]**
  >
  > - 通过[计件报工](https://open.dingtalk.com/document/orgapp/riqing-monthly-settlement-piece-rate-reporting-interface)接口操作的报工记录仅用于工资核算，需要从**计件算薪-工资核算**中拉取接口报工记录并完成核算，最后可以从计件工资内查看接口报工记录对应的工资信息。![iShot2022-03-01 13](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8940154871/p409936.png)
  > - 通过工单二维码手动扫码操作报工，会显示到**计件报工-报工记录**内。
  >
  >   ![iShot2022-03-01 13](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8940154871/p409937.png)
- 根据报工id，调用服务端API-[查询计件报工数据](1109-riqing-monthly-settlement-query-interface-for-piece-rate-reporting.md)接口，获取本次报工记录的详情数据信息。
