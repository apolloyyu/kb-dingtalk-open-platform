---
title: "概述"
source_url: "https://open.dingtalk.com/document/dingstart/member-profile-coolapp-overview"
namespace: "dingstart"
slug: "member-profile-coolapp-overview"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发成员资料页酷应用 > 概述"
doc_id: "rme5VCNeNJ"
updated_at: "2026-06-30 09:01:01"
---

> Source: https://open.dingtalk.com/document/dingstart/member-profile-coolapp-overview
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发成员资料页酷应用 > 概述
> Updated: 2026-06-30 09:01:01

# 概述

如果你想要了解成员资料页和它的开放能力，你可以依据本文档了解成员资料页。

## **概述**

成员资料页是钉钉中用于展示组织成员基本信息的核心界面，包括姓名、职位、所属部门、联系方式等原生数据。为满足企业个性化业务需求，钉钉开放平台提供了“成员资料页扩展”能力，允许开发者在成员资料页中嵌入自定义的卡片内容。

通过该能力，企业可将外部系统中的动态信息（如员工考勤状态、销售业绩、OKR进度、服务评分等）以结构化卡片的形式集成至成员资料页，实现业务数据的实时触达与高效协作。

## **什么是**成员资料页扩展

在日常工作中，用户频繁查看成员资料页以了解同事的基本信息和组织关系。然而，这些信息局限于钉钉平台自带字段，无法反映员工的实时业务表现。

外部系统（如HR系统、CRM、绩效管理系统）中的关键数据（如上下班打卡状态、本月成单数、当前OKR完成率）往往分散独立，难以快速获取。成员资料页扩展能力正是为此场景设计。

## **使用场景举例**

| 场景 | 图注说明 |
| --- | --- |
| **人员在线** | image |
| **OKR展示** | image |
| **服务数据** | image |
| **个人标签** | image |

> **提示**：以上图片仅为示意，实际卡片样式由开发者通过JSON模板自定义。

## **3分钟快速上手流程**

![lv_0_20221113203539](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8389838661/p516645.gif)

## **调用流程图解**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8389838661/p516108.png)

**流程说明**：

1. 用户在钉钉客户端打开某成员资料页；
2. 钉钉客户端向开发者配置的回调地址发起POST请求，携带`userId`等上下文参数；
3. 开发者服务端根据`userId`查询业务系统，组装卡片数据并返回；
4. 钉钉客户端解析返回的JSON卡片结构，渲染展示在成员资料页中。
