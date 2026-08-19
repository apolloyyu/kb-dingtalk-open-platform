---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-digital-managers"
namespace: "development"
slug: "overview-digital-managers"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 数字化管理师 > 概述"
doc_id: "BGhjOtXsdg"
updated_at: "2026-07-20 10:44:21"
---

> Source: https://open.dingtalk.com/document/development/overview-digital-managers
> Path: 应用开发 / 服务端API / 更多开放 > 数字化管理师 > 概述
> Updated: 2026-07-20 10:44:21

# 概述

本文介绍数字化管理师开放接口的基本概述和接口调用方式。

## 概述

随着企业数字化的不断推进，数字化管理师的人才紧缺问题也在愈发严重。钉钉开放了相关的一些接口，推进将新职业平台纳入新职业师资、学员培训平台，完成省级对接改造、课程优化和题库优化等工作。

如下图所示，本次开放的接口主要用于查询用户是否完成所有任务平台的实操题任务。

![数字化管理师实操题截图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5280550361/p314383.png)

## 如何调用数字化管理师接口

你可以根据以下流程调用数字化管理师相关接口。

1. 创建第三方个人应用，详情请参考[第三方个人应用学习指南](../01-XOnnmGCTbn-开发指南/0005-create-and-configure-an-application.md)。
2. 使用OAuth 2.0授权流程获取用户`auth_code`。
3. 使用用户同意授权的`auth_code`和应用的信息，调用获取用户token接口得到`access_token`。
4. 使用用户`access_token`调用数字化管理师接口。
