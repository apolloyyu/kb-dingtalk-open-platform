---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/smart-recruitment-overview"
namespace: "development"
slug: "smart-recruitment-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能招聘 > 概述"
doc_id: "2r7JarNC6k"
updated_at: "2026-07-14 09:11:54"
---

> Source: https://open.dingtalk.com/document/development/smart-recruitment-overview
> Path: 应用开发 / 服务端 API / 智能招聘 > 概述
> Updated: 2026-07-14 09:11:54

# 概述

本文介绍了智能招聘的产品，如何开通智能招聘，智能招聘接口能力介绍和如何使用智能招聘接口等。

## 什么是智能招聘

智能招聘为企业提供基于统一通讯的数字化招聘服务，让招聘更简单更高效。一站式招聘全流程管理，助力企业招聘降本增效。更多产品介绍，请参见[钉钉产品使用手册-智能招聘介绍](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbEB5K5JL3XLq?dontjump=true%23%23)。

![iShot2022-06-01_14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4151993871/p445927.png)

## 如何开通智能招聘

开发者可以通过钉钉移动端或PC端开通智能招聘应用，开通后在工作台打开应用并使用。详细步骤可点击[安装智能招聘](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmb5v7KQZoYXLq?dontjump=true%23%23)查看。

### 移动端开通智能招聘

步骤一：打开钉钉移动端，单击**工作台**。

步骤二：在工作台页面，单击**应用中心**。

步骤三：在广场页面，单击**搜索**。

步骤四：在搜索页面，在**搜索框**输入智能招聘。

步骤五：单击搜索出的**智能招聘**应用。

步骤六：在**智能招聘**产品详情页，单击**免费开通**。

![mmexport1649675517593](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7684189461/p428344.gif)

### PC端开通智能招聘

步骤一：打开钉钉PC端，单击**工作台**。

步骤二：在工作台页面，单击**应用中心**。

步骤三：在应用中心页面，在**搜索框**输入智能招聘。

步骤四：单击搜索出的**智能招聘**应用。

步骤五：在智能招聘产品详情页，单击**免费开通**。

![最新](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7534289461/p429444.gif)

## 开放概览

智能招聘提供了丰富的接口开放能力，开发者通过API接口可以实现智能招聘和企业自有的业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [根据手机号获取候选人信息](0965-obtain-candidate-information-based-on-mobile-phone-number.md) | 根据手机号获取候选人信息。 | 新版 |
| [获取候选人的面试信息](0962-query-the-interview-list.md) | 分页查询候选人的面试信息。 | 新版 |
| [通知完成指定的新手任务](0964-notify-the-completion-of-the-specified-novice-task.md) | 通知完成指定的新手任务 | 新版 |
| [获取招聘流程标识](0960-get-recruitment-process-identity.md) | 根据面试的标识ID，获取面试在整个招聘流程中的标识。 | 新版 |
| [确认完成权益的更新](0961-confirm-benefits.md) | 企业用户在智能招聘的权益发生变更后，第三方企业应用需要调用此接口确认权益。 | 新版 |
| [获取智能招聘文件上传信息](0966-obtain-information-about-the-dingtalk-disk-upload-file.md) | 获取智能招聘文件上传到钉盘所需的信息 | 新版 |
| [添加智能招聘文件到钉盘](0967-add-nail-disk-file.md) | 将文件保存到智能招聘的钉盘空间。 | 新版 |
| [导入简历创建候选人](0963-api-importcandidatebyresume.md) | 导入简历创建候选人。 | 新版 |
