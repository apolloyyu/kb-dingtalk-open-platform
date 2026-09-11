---
title: "介绍"
source_url: "https://open.dingtalk.com/document/connection/multidimensional-introduction"
namespace: "connection"
slug: "multidimensional-introduction"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "多维表自动化 > 介绍"
doc_id: "KqDHfDnxjY"
updated_at: "2026-09-10 14:33:15"
---

> Source: https://open.dingtalk.com/document/connection/multidimensional-introduction
> Path: 连接平台 / 连接平台自动化 / 多维表自动化 > 介绍
> Updated: 2026-09-10 14:33:15

# 介绍

## **简介**

多维表自动化旨在帮助用户**将多维表数据的变化自动同步给其他应用**，从而降低人力成本，提高数据同步的效率和准确性。

通过配置自动化流程，当多维表中的记录发生新增、修改或删除时，系统会自动触发预设动作（如发送通知、创建待办、写入其他系统等），实现：

- 📊 **数据驱动工作流**：表格状态变化即时转化为行动指令，告别手动搬运。
- 🔗 **跨应用联动**：多维表与钉钉消息、待办、AI表格、外部系统等无缝打通。
- ⚡ **实时响应**：数据变更秒级触发后续流程，确保信息不遗漏、处理不延误。

## **实现场景**

### 进度更新自动通知

在项目管理AI 表格中，当任务状态从"未开始"变更为"进行中"或"已完成"时，自动化流程会自动触发，向该任务的负责人发送一条进度更新通知。通知内容包含变更的任务名称、变更后的进度状态以及任务重要程度等关键信息，确保负责人第一时间掌握任务动态，无需手动刷新表格或反复询问进度。适用于项目跟踪、任务协同、进度汇报等场景，让信息流转更及时、沟通更高效。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7773735071/p758025.png)

### 高优任务自动创建待办

在AI 表格中，当某条任务的重要程度被修改为"重要且紧急"时，自动化流程会自动为该任务的负责人创建一个钉钉待办事项。待办中清晰展示任务内容、当前进度、截止时间等关键信息，并支持添加提醒和参与人，确保高优先级任务不会被遗漏或延误。适用于任务分级管理、紧急事项跟进、责任人督办等场景，让重要事务得到应有的关注和及时处理。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7773735071/p758027.png)

## **多维表自动化入口**

> **[!NOTE]**
>
> 多维表的所有者，或者有管理权限的协作者能够开启自动化流程。

1. 创建一张多维表，或打开一张已有的多维表，单击右上角**自动化**，即可开启。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4723645071/p758811.png)
2. 在自动化中，可以选择一个模板创建流程，或从空白创建流程。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4723645071/p758812.png)

## **模板案例**

了解功能后，你可以查看[批次码与出库码智能比对](0014-automatic-verification-comparison.md)模板案例，学习如何落地实际场景！

## **相关文档**

- [创建自动化流程](0002-automated-process-usage-guide.md)
