---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/blackboard-announcement-overview"
namespace: "development"
slug: "blackboard-announcement-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "公告 > 概述"
doc_id: "ntP5GfVOFL"
updated_at: "2026-07-02 10:36:24"
---

> Source: https://open.dingtalk.com/document/development/blackboard-announcement-overview
> Path: 应用开发 / 服务端 API / 公告 > 概述
> Updated: 2026-07-02 10:36:24

# 概述

本文介绍了什么是公告，如何开通公告，公告开放了哪些接口能力，以及如何接入公告能力。

## 什么是公告

管理员可以通过公告发布公司或单位的规章制度、节假日信息等通知，快速通知到全体员工。更多功能详情可参考[钉钉使用手册-公告](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/mM3zoYAw1Rr8Dan5xEk6WnZ07y9NpXxD)。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4879592871/p522596.png)

## 如何开通公告

公告是钉钉默认安装的官方应用。员工可以在钉钉工作台打开应用并使用。

- 手机端：钉钉手机客户端-工作台![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4418809661/p522577.png)
- 电脑端：钉钉电脑客户端-工作台![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4879592871/p522579.png)

## 开放概览

### **开放接口列表**

公告提供了丰富的接口开放能力，开发者通过API接口可以实现公告和企业业务系统打通。

| **API** | **API说明** | **API 版本** |
| --- | --- | --- |
| [创建公告](0279-create-an-enterprise-announcement.md) | 创建企业公告。 | 旧版 |
| [删除公告](0280-delete-announcements-based-on-the-announcement-id.md) | 根据公告ID删除公告。 | 旧版 |
| [更新公告](0281-modify-the-announcement-according-to-the-announcement-id.md) | 更新公告。 | 旧版 |
| [获取公告详情](0282-obtains-the-details-get-blackboard.md) | 根据公告ID获取未删除的公告的详情。 | 新版 |
| [获取公告ID列表](0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md) | 获取企业某公告分类下所有未删除公告的ID列表。 | 旧版 |
| [获取公告分类列表](0284-obtains-the-list-of-categories-not-deleted-for-enterprise-announcements.md) | 获取未删除的公告分类列表。 | 旧版 |
| [获取用户可查看的公告](0285-list-the-user-s-announcement-list.md) | 获取指定人员的公告信息，在企业自定义工作首页进行公告轮播展示。 | 旧版 |
| [获取公告钉盘空间信息](0286-obtain-bulletin-nail-disk-space-information.md) | 获取企业组织公告的钉盘空间信息。 | 新版 |
| [查询公告已读未读人员列表](0287-query-bulletin-read-unread-persons-list.md) | 获取指定公告的已读未读人员列表。 | 新版 |

### **回调事件列表**

公告支持[公告发送](../04-LFcRvVD08N-事件订阅/0019-events-blackboard-sent.md)回调事件。

## **使用教程**

钉钉提供了公告接口接入流程示例，请参见[创建、获取、更新及删除公告](0278-create-and-delete-announcements.md)**。**

## 名词解释

- **公告分类**：公告分类的唯一标识字段是category\_id。例如，公告分类“分类1”的category\_id是3b583d630587021beaa3b32d9fxxxxxx。
- **公告ID**：公告的唯一标识字段是blackboard\_id。例如公告“正式公告1”的blackboard\_id是72b4f87d27e815f6fecxxxxxx。
- **公告的保密等级**：公告保密等级的唯一标识是private\_level。

  - **0**：表示普通公告。
  - **1**：表示保密公告。
