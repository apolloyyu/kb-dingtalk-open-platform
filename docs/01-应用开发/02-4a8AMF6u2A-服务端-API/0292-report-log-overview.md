---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/report-log-overview"
namespace: "development"
slug: "report-log-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日志 > 概述"
doc_id: "usxyGH9sdA"
updated_at: "2026-07-08 14:38:18"
---

> Source: https://open.dingtalk.com/document/development/report-log-overview
> Path: 应用开发 / 服务端 API / 日志 > 概述
> Updated: 2026-07-08 14:38:18

# 概述

本文介绍了日志产品使用，如何开通日志应用等内容。

## 什么是日志

方便管理者了解员工每日工作情况，可以帮助员工总结沉淀工作经验。更多介绍请参见[钉钉使用手册-日志](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbp6NA6NqzLq2?dontjump=true%23%23)。

![iShot2022-04-18_10 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2865620561/p430918.png)![iShot2022-04-18_10 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2865620561/p430919.png)

## 如何开通日志

开发者可以通过钉钉移动端或钉钉PC端使用日志。

手机端：钉钉移动端-工作台

![iShot2022-01-12 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7531791461/p384033.png)

电脑端：钉钉PC端-工作台

![iShot2022-01-12 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8531791461/p384038.png)

## 开放概览

日志提供了丰富的接口开放能力，开发者通过API接口可以实现日志和企业自由的业务系统打通。

| **API** | **说明** | **API版本** |
| --- | --- | --- |
| [创建日志](0294-create-a-log.md) | 创建日志。 | 旧版 |
| [保存日志内容](0295-save-custom-log-content.md) | 保存自定义的日志内容。 | 旧版 |
| [获取模板详情](0296-query-template-details.md) | 根据日志模板名称获取模板详情。 | 旧版 |
| [获取用户发出的日志列表](0297-query-logs-sent-by-an-employee.md) | 获取用户发出的日志列表。 | 旧版 |
| [获取用户发送日志的概要信息](0298-view-log-summary-data.md) | 获取员工在一段时间范围内发送的日志概要信息。 | 旧版 |
| [获取用户可见的日志模板](0303-obtains-the-list-of-visible-log-templates-based-on-the.md) | 根据userId获取用户可见的日志模板。 | 旧版 |
| [获取日志相关人员列表](0299-obtains-a-list-of-log-related-personnel-by-type.md) | 查询日志已读人员列表、评论人员列表或点赞人员列表。 | 旧版 |
| [获取日志接收人员列表](0300-queries-log-sharing-personnel.md) | 获取日志接收人员列表。 | 旧版 |
| [获取用户日志未读数](0302-querying-the-employee-s-log-is-not-reading.md) | 获取员工有多少数量的日志（一个月内）是未读状态。 | 旧版 |
| [获取日志评论详情](0301-queries-log-comment-details.md) | 获取评论详情。 | 旧版 |

## 使用教程

钉钉提供了日志接口接入流程示例，请参见[三方系统发起和查看日志信息](0293-log-api-use-cases.md)。

## 名词解释

### 日志模板标识字段（report\_code）

日志模板标识字段，定义为report\_code。例如周报、日报都属于日志模板，都有分别对应的report\_code值。![iShot2022-04-18_10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2865620561/p430885.png)

### 日志内容（contents）

日志内容，包含日志内每一个组件的排序、类型、文本内容等属性信息，定义为contents。![iShot2022-04-18_10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2865620561/p430887.png)

### 日志唯一标识字段（report\_id）

每篇日志对应唯一标识字段report\_id。![iShot2022-04-18_11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1865620561/p430920.png)
