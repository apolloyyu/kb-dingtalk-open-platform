---
title: "查询用户是否完成所有任务"
source_url: "https://open.dingtalk.com/document/development/querying-completed-tasks"
namespace: "development"
slug: "querying-completed-tasks"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 数字化管理师 > 使用教程 > 查询用户是否完成所有任务"
doc_id: "ecIjoFZubK"
updated_at: "2026-07-21 09:26:08"
---

> Source: https://open.dingtalk.com/document/development/querying-completed-tasks
> Path: 应用开发 / 服务端 API / 更多开放 > 数字化管理师 > 使用教程 > 查询用户是否完成所有任务
> Updated: 2026-07-21 09:26:08

# 查询用户是否完成所有任务

本文档介绍了如何调用数字化管理师接口。首先创建一个第三方个人应用，再使用数字化管理师提供的API，实现检查用户是否完成所有任务流程。

## 流程简介

步骤一，登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[第三方个人应用](../01-XOnnmGCTbn-开发指南/0005-create-and-configure-an-application.md)。

步骤二，获取AppId和AppSecret。

步骤三，申请数字化管理师接口权限，查找“数字化管理师“”，申请相应权限。

步骤四，第三方个人应用接入[钉钉统一授权套件](0007-function-description.md)，获取用户个人authCode。

步骤五，根据用户个人authCode，获取个人应用访问凭证[获取用户token](0032-obtain-user-token.md)。

步骤六，调用服务端数字化管理师相关API。

1. 调用服务端API-[检查用户是否完成所有任务](1339-docking-of-provincial-practical-exercises-for-digital-managers.md)接口，检查用户是否完成所有任务。

## 步骤一，创建第三方个人应用

登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[第三方个人应用](../01-XOnnmGCTbn-开发指南/0005-create-and-configure-an-application.md)。

![创建三方个人应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8617954871/p409855.png)

## 步骤二，获取AppId和AppSecret

获取AppId和AppSecret。

![获取个人原因信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8617954871/p409857.png)

## 步骤三，添加接口权限

申请数字化管理师接口权限，查找“数字化管理师“”，申请相应权限。

![申请数字化管理师权限](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8617954871/p409861.png)

## 步骤四，接入钉钉统一授权套件

第三方个人应用接入[钉钉统一授权套件](0007-function-description.md)，获取用户个人authCode。

> **[!NOTE]**
>
> - 用户个人authCode不是用户免登authCode。
> - 统一授权套件中rpcScope列表中需要填入数字化管理师的权限点**DigitalManager.TaskStatus.Read**。

## 步骤五，获取个人应用访问凭证accessToken

根据AppId、AppSecret和用户个人authCode，获取个人应用访问凭证[获取用户token](0032-obtain-user-token.md)。

## 步骤六，调用服务端数字化管理师相关API

1. 调用服务端API-[检查用户是否完成所有任务](1339-docking-of-provincial-practical-exercises-for-digital-managers.md)接口，检查用户是否完成所有任务。
