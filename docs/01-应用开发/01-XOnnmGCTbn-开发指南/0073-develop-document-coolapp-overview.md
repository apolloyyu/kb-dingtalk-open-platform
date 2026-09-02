---
title: "概述"
source_url: "https://open.dingtalk.com/document/dingstart/develop-document-coolapp-overview"
namespace: "dingstart"
slug: "develop-document-coolapp-overview"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发文档酷应用 > 概述"
doc_id: "oKCDSLG7WO"
updated_at: "2026-06-30 09:01:05"
---

> Source: https://open.dingtalk.com/document/dingstart/develop-document-coolapp-overview
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发文档酷应用 > 概述
> Updated: 2026-06-30 09:01:05

# 概述

本文档旨在帮助开发者全面了解文档酷应用及其开放能力，指导如何接入和开发文档酷应用。通过本文档，开发者可掌握文档酷应用的核心概念、适用场景、关键组件及完整接入流程。

## **什么是**文档酷应用

在日常使用钉钉文档时，用户常需完成重复且耗时的编辑任务，例如频繁检查协作者是否更新内容、手动校对文档准确性，或反复切换网页将外部系统数据录入至钉钉文档中。

文档酷应用能够将这些重复性操作转化为自动化流程。接入后，可帮助用户自动感知特定事件、快速读写文档内容并执行校验逻辑，显著提升工作效率。

目前，文档酷应用支持在 **钉钉表格** 中使用，提供扩展右侧面板和弹窗容器的能力。开发者可基于其丰富的 UI 渲染与交互能力，实现各类文档相关的业务自动化场景。

## 应用场景

### **使用案例1：填表信息管理**

实现钉钉表格中的数据自动导入与内容校验，减少人工干预，确保数据一致性。

![实现数据导入](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5621872871/p578855.png)

### **使用案例2：**接入企业内部业务系统数据

将企业内部系统的数据（如CRM、ERP）同步至钉钉表格，实现实时筛选与统计分析，提升协作效率。

![导入企业内部数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5621872871/p578858.png)

## **开发视频**

本视频介绍了如何快速开发体验文档酷应用。

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20230303/hojl/文档酷应用流程_1.mp4)

## **名词解释**

- **脚本服务**

  脚本服务页面负责接收来自文档酷应用UI页面的调用请求，对文档进行读写，由开发者提供。开发者可在该页面中使用文档酷应用JSAPI初始化文档酷应用脚本服务、访问钉钉文档模型以及定义脚本服务应如何读写文档。钉钉文档向开发者提供了一个全局变量「DingdocsScript」，开发者可通过调用「DingdocsScript」注册一组用于读写钉钉文档模型的脚本函数。
- **脚本函数**

  是用于读写钉钉文档对象模型的函数。在文档酷应用中，必须以函数形式定义脚本服务应该如何读写文档，并通过文档酷应用 JSAPI 注册函数。
- **UI页面视图界面**

  UI页面负责渲染文档酷应用在文档中的交互面板，由开发者提供。开发者可在该页面中使用文档酷应用JSAPI初始化文档酷应用视图、请求脚本服务页面读写文档、监听文档的操作。

  钉钉文档向开发者提供了一个全局变量「Dingdocs」，开发者可在自定义的 UI界面中通过「Dingdocs」实现调用脚本服务、监听文档操作等行为。
- **Manifest**

  Manifest是描述一个文档酷应用基本信息的JSON文件，开发者可在Manifest文件中配置文档酷应用脚本服务页面和UI页面的访问地址，指定酷应用在文档中如何进行渲染。接入文档酷应用时开发者必须在开发者后台上传Manifest文件。详情参考[配置文档酷应用Manifest](0075-configure-document-coolapp-manifest.md)。
