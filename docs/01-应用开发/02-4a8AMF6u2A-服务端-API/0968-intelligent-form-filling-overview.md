---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/intelligent-form-filling-overview"
namespace: "development"
slug: "intelligent-form-filling-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能填表 > 概述"
doc_id: "thzhTAdWnw"
updated_at: "2026-07-14 09:12:14"
---

> Source: https://open.dingtalk.com/document/development/intelligent-form-filling-overview
> Path: 应用开发 / 服务端 API / 智能填表 > 概述
> Updated: 2026-07-14 09:12:14

# 概述

本文介绍了智能填表产品，如何开通智能填表，智能填表开放了哪些接口能力，以及如何接入智能填表能力。

## 智能填表介绍

智能填表是钉钉提供的一款基础应用，用于问卷调查、报名统计等场景，支持数据统计和下载。钉钉提供了丰富的基础表单模板，用户也可以创建填表，以满足更多的使用场景。更多功能介绍，请参见[钉钉使用手册-智能填表](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbOpy0RkKGLq2?dontjump=true)。

![表单 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7559672061/p174044.png)

## 如何开通智能填表

智能填表是钉钉默认安装的官方应用。员工可以在钉钉工作台打开应用并使用。

手机端：钉钉手机客户端-工作台

![1张图a备份 5](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4351993871/p432079.png)

电脑端：钉钉电脑客户端-工作台

![局部内容展示备份 3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4351993871/p432080.png)

## 开放概览

智能填表提供了丰富的接口开放能力，开发者通过API接口可以实现智能填表和企业业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取用户创建的填表模板列表](0970-new-obtains-the-template-that-a-user-creates.md) | 获取用户创建的填表模板列表。 | 新版 |
| [获取填表实例列表](0971-obtain-the-table-filling-instance-list-data.md) | 根据填表的Code获取填表实例列表。 | 新版 |
| [获取单条填表实例详情](0972-obtains-the-instance-details-of-a-single-fill-table.md) | 获取单条填表实例详情。 | 新版 |

## 使用教程

如何获取表单、及表单数据等接入流程，请参见[获取用户的填表数据详情](0969-use-case-form.md)。

## 名词解释

### 表单（form\_code）

智能填表中，用户可以创建多个表单。每个表单有唯一标识字段，定义为form\_code。

![智能填表-用户创建的表单示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4351993871/p430841.png)

### 表单实例

智能填表中，填写表单后会生成一个表单实例，如下图所示。

> **[!NOTE]**
>
> 每个表单实例有一个唯一标识字段，定义为formInstance\_id或form\_instance\_id。

![表单实例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4351993871/p430840.png)
