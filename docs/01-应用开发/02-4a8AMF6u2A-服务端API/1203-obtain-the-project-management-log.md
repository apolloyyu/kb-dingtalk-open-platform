---
title: "获取项目管理操作日志"
source_url: "https://open.dingtalk.com/document/development/obtain-the-project-management-log"
namespace: "development"
slug: "obtain-the-project-management-log"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 使用教程 > 获取项目管理操作日志"
doc_id: "pWEFHsBwKu"
updated_at: "2026-07-20 09:21:50"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-project-management-log
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 使用教程 > 获取项目管理操作日志
> Updated: 2026-07-20 09:21:50

# 获取项目管理操作日志

本文档介绍了如何调用项目管理接口获取项目日志流程。首先创建一个企业内部应用，再使用项目管理提供的API，实现查询项目中文件操作日志流程。

## 使用说明

- 项目管理中**旧版项目**操作文件可以调用该接口获取文件日志信息，项目管理中**新版项目**操作文件无法调用该接口获取文件日志信息。
- 如下图，“最近使用的旧版项目”中包含的项目均为旧版项目。

  ![项目管理 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0150154871/p409732.png)

## 流程简介

步骤一，登录[开发者后台](https://open-dev.dingtalk.com/#/)，根据[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)文档，创建企业内部应用。

步骤二，获取AppKey和AppSecret。

步骤三，根据[添加接口调用权限](0003-add-api-permission.md)文档，搜索“项目管理”，申请相应权限。

步骤四，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五，调用服务端项目管理相关API。

1. 调用服务端API-[查询项目中文件操作日志](1220-query-file-operation-logs-of-a-project.md)接口，获取项目管理上传、删除的日志信息。

## 步骤一，创建企业内部应用

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二，获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三，添加接口权限

根据[添加接口调用权限](0003-add-api-permission.md)文档，搜索“项目管理”，申请相应权限。![项目管理权限](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0150154871/p409307.png)

## 步骤四，获取应用访问凭证accessToken

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

## 步骤五，调用服务端项目管理相关API

1. 调用服务端API-[查询项目中文件操作日志](1220-query-file-operation-logs-of-a-project.md)接口，获取项目管理上传、删除的日志信息。

   > **[!NOTE]**
   >
   > - 项目管理中**旧版项目**操作文件可以调用该接口获取文件日志信息，项目管理中**新版项目**操作文件无法调用该接口获取文件日志信息。
   > - 如下图，“最近使用的旧版项目”中包含的项目均为旧版项目。

   ![项目管理 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0150154871/p409732.png)
