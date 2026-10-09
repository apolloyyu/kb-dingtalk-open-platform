---
title: "卡片简介"
source_url: "https://open.dingtalk.com/document/development/what-is-a-card-platform"
namespace: "development"
slug: "what-is-a-card-platform"
group: "互动卡片"
tab: "功能介绍"
breadcrumb: "卡片简介"
doc_id: "nrew2PhnTG"
updated_at: "2026-10-09 14:28:36"
---

> Source: https://open.dingtalk.com/document/development/what-is-a-card-platform
> Path: 互动卡片 / 功能介绍 / 卡片简介
> Updated: 2026-10-09 14:28:36

# 卡片简介

## **概述**

互动卡片是一种可交互的消息类型，由**结构**与**数据**两部分构成：结构决定界面由哪些区块和控件组成，数据决定这些区块最终显示的内容。

结构的构建方式有两种：在卡片平台上**搭建模板**，或使用 **JSON 直接描述**，数据均在发送时随请求提交。两种方式产出的都是互动卡片，可在同一应用内共存。

## 典型用途

| **场景** | **例子** |
| --- | --- |
| 通知与待办 | 审批、告警、任务提醒，附上处理入口。 |
| 进度与状态 | 任务执行进度、Agent 的处理过程，随进展更新同一张卡片。 |
| 表单与操作 | 填写、选择、确认，结果回到业务侧继续处理。 |
| 数据展示 | 报表、指标、图表。 |

## 构建方式

- [模板搭建卡片](../02-MhNX42mFB1-模板搭建卡片/0001-card-template-building-and-publishing.md)：在平台上拖拽搭建，发布后获得模板 ID，适用于结构固定、样式统一、需要运营人员可配置的场景。
- [JSON 构建卡片](../03-lHGhOeTVdR-JSON-构建卡片（AI）/0001-json-build-card.md)：直接使用 JSON 描述结构，无需模板，适用于结构在运行时确定，或由 Agent 动态决定展示内容的场景。

如需逐项对比，请参考[构建方式](0002-card-building-methods.md)，概念容易混淆时，可查阅[名词释义](0003-organization.md)。

## 工作流程

![构建方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6137251971/p1104137.png)

具体的接口、命令和事件在各自的接入文档里：

- 模板搭建，详见[模板搭建卡片](../02-MhNX42mFB1-模板搭建卡片/0001-card-template-building-and-publishing.md)。
- JSON 构建，详见[JSON 构建卡片](../03-lHGhOeTVdR-JSON-构建卡片（AI）/0001-json-build-card.md)。

## 开始使用

1. **选定构建方式**：按上面的场景和对照表确定走哪条。
2. **进入对应分区**：模板搭建从[模板搭建卡片](../02-MhNX42mFB1-模板搭建卡片/0001-card-template-building-and-publishing.md)开始； JSON 构建从[JSON 构建卡片](../03-lHGhOeTVdR-JSON-构建卡片（AI）/0001-json-build-card.md)开始，先看适用范围与前提。
3. **概念不清时查表**：两个「模板」、两个「AI 卡片」这类容易混淆的词，见[名词释义](0003-organization.md)。
