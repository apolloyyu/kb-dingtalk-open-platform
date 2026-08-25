---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/medical-address-book-overview"
namespace: "development"
slug: "medical-address-book-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 医疗 > 概述"
doc_id: "PQ2koFNU1n"
updated_at: "2026-05-19 11:19:34"
---

> Source: https://open.dingtalk.com/document/development/medical-address-book-overview
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 医疗 > 概述
> Updated: 2026-05-19 11:19:34

# 概述

本文档介绍什么是医疗通讯录，如何开通使用医疗通讯录，以及医疗通讯录接口能力。

## 什么是医疗通讯录

医疗行业-临床科组人管理是钉钉为医院提供的精细化临床组织管理应用。旨在帮助医院明晰准确地掌握全院每个科室下的组织安排、每个医生的工作安排，有效实现对临床科室在组织和人员管理上的事前管控、事中监控、事后留痕、数据分析。同时，基于钉钉的IM、消息通知、端能力，改善传统过程中，管理者与各科室管理者只能通过点对点电话、本地文档的低效协同方式。

- 随时随地掌握科室内所有员工的身份、工作状态、历史工作的医疗组轨迹；
- 在电脑和手机都可快速处理和修正医疗组数据异常、状态异常的员工；
- 与医院各行政科室实时共享数据、减少重复沟通。

![iShot2022-01-24 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046423461/p392786.png)

## 如何开通使用医疗通讯录

目前，医疗行业-临床科组人管理正在全国部分公立三甲医院开展共创，本功能目前需咨询钉钉小二进行开通。

如您有意向，请登录[开发者后台](https://open-dev.dingtalk.com/)-右下角在线答疑-人工客服咨询，详情请查看[技术支持](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)。

## 开放概览

### 开放接口列表

医疗通讯录提供了丰富的接口开放能力，开发者通过API接口可以实现医疗通讯录和企业业务系统打通。

| API | API说明 | API版本 |
| --- | --- | --- |
| [保存人员扩展属性](1105-personnel-extension-property-error.md) | 支持保存人员扩展属性。 | 新版 |

### **回调事件列表**

医疗通讯录支持行业用户属性变动、科室医疗组变动、科室医疗组属性变动等多种回调事件。

- [医疗行业用户属性变动](../04-LFcRvVD08N-事件订阅/0210-user-attribute-change-in-medical-industry.md)
- [医疗行业用户所在科室医疗组变动](../04-LFcRvVD08N-事件订阅/0213-changes-in-the-medical-group-of-the-department-where-the.md)
- [医疗行业科室医疗组变动](../04-LFcRvVD08N-事件订阅/0211-changes-in-medical-departments-and-medical-groups-in-the-medical.md)
- [医疗行业科室医疗组属性变动](../04-LFcRvVD08N-事件订阅/0212-change-of-attribute-of-medical-group-of-medical-department-in.md)
- [医疗通讯录全量同步](../04-LFcRvVD08N-事件订阅/0209-full-synchronization-of-medical-address-book.md)
