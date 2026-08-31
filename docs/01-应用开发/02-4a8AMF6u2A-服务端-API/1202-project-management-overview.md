---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/project-management-overview"
namespace: "development"
slug: "project-management-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 概述"
doc_id: "TobEGr3v2I"
updated_at: "2026-07-20 09:25:42"
---

> Source: https://open.dingtalk.com/document/development/project-management-overview
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 概述
> Updated: 2026-07-20 09:25:42

# 概述

本文档介绍了什么是Teambition 项目管理，如何开通使用Teambition 项目管理，Teambition 项目管理接口能力，以及如何接入Teambition 项目管理接口能力等。

## 什么是项目管理

钉钉项目（钉钉 Teambition）是一款集项目、任务协同于一体的数字化协同工具，在钉钉项目，协同不再以沟通为主线，而是围绕着“事”协作，工作内容从此变得聚焦、有始有终。让你的工作件件有着落，事事有回应。更多功能介绍，请参见[钉钉使用手册-项目管理](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/od245kZmnOeW4qZQ25pkVYbzxL6R0wMQ?dontjump=true# 「项目管理」)。

![项目管理2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p451173.png)

## 如何开通项目管理

注册钉钉组织后，默认开通 Teambition 项目管理应用。用户可以在钉钉 PC 端或移动端使用钉钉项目。

### 移动端入口

移动端可以从**协作 > 项目**、**工作台 > 项目**或者**项目群 > 项目概述**进入项目，如下图所示。

![移动端](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p451422.png)

### PC端入口

- PC端可以从**钉钉左侧导航栏 > 项目**进入项目，如下图所示。

  ![图片排版-钉钉端展示-1张图1备份 9](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p451427.png)
- PC端可以从**工作台 > 项目**进入项目，如下图所示。

  ![2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p451431.png)
- PC端可以从**项目群 > 群内tab > 项目概况**进入项目，如下图所示。

  ![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p451432.png)

## 新旧版本说明

> **[!NOTE]**
>
> 该模块内容仅限企业内部应用。

目前用户所登录使用的项目应用，默认都属于新版本项目，新版本项目应用的界面截图如下图所示：

![iShot2022-06-27 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p459853.png)

如果需要从新版本切换到旧版，可在新版本项目应用左下角点**击更多 > 回到旧版**。

![iShot2022-06-27 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p459858.png)

## 开放概览

### **开放接口列表**

项目管理提供了丰富的接口开放能力，开发者通过API接口可以实现项目管理和企业业务系统打通。

> **[!IMPORTANT]**
>
> 以下接口适用范围是**新版项目**，**旧版项目**无法调用以下接口。在项目产品中，一般是新版项目，点击最近使用的旧版项目，进入旧版项目。

![概述1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2470154871/p480119.png)

#### **项目**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建项目](1206-create-project.md) | 调用本接口创建项目，项目均为私有项目。 | 新版 |
| [查询项目](1207-query-enterprise-all-projects.md) | 根据用户ID，实现查询企业下的所有项目，支持项目名模糊搜索。 | 新版 |
| [归档项目](1208-archiving-project.md) | 根据项目ID和用户ID，实现将项目进行归档操作。 | 新版 |
| [恢复项目归档](1209-cancel-project-archiving.md) | 根据项目ID和用户ID，实现恢复项目归档。 | 新版 |
| [获取项目成员](1210-get-project-members.md) | 根据操作者ID和项目ID，查询项目中的成员。 | 新版 |
| [查询项目状态](1211-query-project-status.md) | 根据操作者ID和项目ID，查询项目状态。 | 新版 |
| [添加项目成员](1212-add-project-members.md) | 批量添加项目成员。 | 新版 |
| [删除项目成员](1213-delete-project-members.md) | 根据操作者ID和项目ID，删除项目成员 | 新版 |
| [项目放入回收站](1214-items-in-recycle-bin.md) | 根据操作者ID和项目ID，实现将项目放入回收站。 | 新版 |
| [获取用户加入的项目](1215-get-projects-joined-by-users.md) | 根据用户userId信息，获取用户加入的项目Id列表。 | 新版 |
| [搜索企业项目模板](1216-search-for-enterprise-custom-templates-by-project-template-name.md) | 按模板名字搜索项目模板信息。 | 新版 |
| [根据项目模板创建项目](1217-create-a-project-from-a-project-template.md) | 根据项目模板创建项目。 | 新版 |
| [查询员工可见的项目分组](1218-query-available-project-groups.md) | 查询员工可见的项目分组列表。 | 新版 |
| [更新项目所在的分组](1219-update-project-grouping.md) | 更新项目所在分组。 | 新版 |
| [查询项目中文件操作日志](1220-query-file-operation-logs-of-a-project.md) | 获取钉钉项目空间任务中文件的操作日志列表。 | 新版 |
| [创建或更新项目概览中自定义字段值](1221-create-or-update-field-values-project-overview.md) | 为概览中自定义字段的赋值 | 新版 |

#### **任务**

##### **自由任务**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建自由任务](1242-create-a-free-task.md) | 创建一个钉钉自由任务。 | 新版 |
| [获取自由任务详情](1243-queries-free-task-details.md) | 通过任务ID获取自由任务的详情 | 新版 |
| [查询优先级列表](1244-query-a-priority-list.md) | 查询企业下设置的任务优先级列表。 | 新版 |
| [批量获取自由任务详情](1245-obtains-details-about-multiple-free-tasks.md) | 根据一组自由任务id，批量获取自由任务详情信息。 | 新版 |
| [更新自由任务标题](1246-change-free-task-title.md) | 更新自由任务的标题。 | 新版 |
| [更新自由任务状态](1247-change-free-task-status.md) | 更新自由任务的状态。 | 新版 |
| [更新自由任务执行者](1249-change-free-task-executor.md) | 更新自由任务的优先级。 | 新版 |
| [更新自由任务备注](1248-update-free-task-notes.md) | 更新自由任务的备注信息。 | 新版 |
| [更新自由任务执行者](1249-change-free-task-executor.md) | 更新自由任务的执行者。 | 新版 |
| [更新自由任务的优先级](1250-change-free-task-priority.md) | 更新自由任务的优先级。 | 新版 |
| [更新自由任务截止时间](1251-change-free-task-deadline.md) | 更新自由任务的截止时间。 | 新版 |
| [增加或删除自由任务的参与者](1252-change-task-participant.md) | 增加或删除自由任务的参与者。 | 新版 |

##### **项目任务**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建项目任务](1222-create-a-project-task.md) | 创建关联项目的任务 | 新版 |
| [删除任务](1223-delete-task.md) | 删除任务，该删除操作为永久删除，仅任务创建者和执行者可以操作删除。 | 新版 |
| [获取任务详情](1224-get-task-details.md) | 获取任务详情信息 | 新版 |
| [查询任务分组](1225-query-task-grouping.md) | 根据用户ID和项目ID，查询用户任务分组信息。 | 新版 |
| [获取任务列表](1226-get-task-list.md) | 根据用户ID和项目ID，查询用户任务列表信息。 | 新版 |
| [查询任务工作流](1227-query-task-workflow.md) | 根据操作者ID和项目ID，查询项目任务的工作流信息。 | 新版 |
| [查询用户任务信息列表](1228-querying-user-tasks.md) | 根据操作者的userId信息和用户的任务角色类型，查询所关联项目中的任务信息列表。 | 新版 |
| [添加任务的关联内容](1230-create-a-linked-object-associated-with-a-task.md) | 添加任务的关联内容。 | 新版 |
| [查询项目中的任务](1229-query-tasks-in-a-project.md) | 可根据指定条件查询项目中的任务。 | 新版 |
| [任务迁移至回收站](1231-archive-tasks.md) | 根据操作者ID和任务ID，将项目迁移至回收站。 | 新版 |
| [搜索任务工作流状态](1232-search-task-workflow-status.md) | 搜索指定项目下任务工作流的各个状态。 | 新版 |
| [更新任务工作流状态](1233-update-task-workflow-status.md) | 更新指定项目下的任务工作流状态 | 新版 |
| [更新任务备注](1234-update-task-notes.md) | 根据操作者ID和任务ID，实现更新任务备注信息。 | 新版 |
| [更新任务标题](1235-update-task-content.md) | 根据操作者ID和任务ID，实现更新任务标题信息。 | 新版 |
| [更新任务执行者](1236-update-task-performer.md) | 根据操作者ID、任务ID和执行者ID，实现更新任务的执行者。 | 新版 |
| [更新任务优先级](1237-update-task-priority.md) | 根据操作者ID、任务ID和优先级枚举值，更新任务优先级。 | 新版 |
| [更新任务参与者](1238-update-task-participants.md) | 根据操作者ID和任务ID，将用户ID添加到参与者。 | 新版 |
| [更新任务截止时间](1239-update-task-deadline.md) | 根据操作者ID和任务ID，实现更新任务的截止时间。 | 新版 |
| [更新任务开始时间](1240-update-task-start-time.md) | 根据操作者ID、任务ID和任务开始时间，更新任务开始时间信息。 | 新版 |
| [更新项目任务的自定义字段值](1241-update-task-custom-field-value.md) | 更新项目任务的自定义字段值。 | 新版 |

#### **工时**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建计划工时](1253-create-planned-work.md) | 新增项目任务中对应的计划工时。 | 新版 |
| [创建实际工时](1254-create-actual-work.md) | 添加任务的实际工时。 | 新版 |

#### **企业和用户**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取Teambition项目企业ID](1255-obtain-the-teambition-enterprise-id.md) | 根据钉钉用户userId获取该用户所属钉钉企业绑定的Teambition项目企业ID。 | 新版 |
| [根据userId获取Teambition项目用户ID](1256-obtain-dingtalk-teambition-user-id-based-on-userid.md) | 根据userId获取Teambition项目用户ID。 | 新版 |

### **回调事件列表**

Teambition 项目管理支持工时变更、项目变更、成员变更和应用变更等时间。

- [Teambiton工时变更事件](../04-LFcRvVD08N-事件订阅/0020-event-project-worktime-updated.md)
- [Teambiton项目变更事件](../04-LFcRvVD08N-事件订阅/0021-teambiton-project-change-event.md)
- [Teambition成员变更事件](../04-LFcRvVD08N-事件订阅/0022-teamposition-member-change-event.md)
- [Teambition应用变更事件](../04-LFcRvVD08N-事件订阅/0023-teamposition-application-change-event.md)
- [Teambition项目任务变更事件](../04-LFcRvVD08N-事件订阅/0024-teamposition-project-task-change-event.md)
- [Teambition任务更新事件](../04-LFcRvVD08N-事件订阅/0025-teamposition-task-update-event.md)
- [Teambition项目更新事件](../04-LFcRvVD08N-事件订阅/0026-teamposition-project-update-event.md)

## 使用教程

钉钉提供了企业内部应用项目管理接口接入流程示例。

- [获取项目管理操作日志](1203-obtain-the-project-management-log.md)
- [创建、更新和获取自由任务](1204-teambition-free-task-operation-process.md)
- [创建项目任务和工时](1205-team-ambition-project-operation-process.md)

## 名词解释

### 自由任务

自由任务是在项目应用中创建，但是不关联任何项目的任务。![iShot2022-06-23 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286795561/p459466.png)

### 优先级（priority）

自由任务优先级。

- 使用项目默认的优先级，如下图所示。优先级默认为以下。

  - **-10**：较低，默认值。
  - **0**：普通
  - **1**：紧急
  - **2**：非常紧急

![iShot2022-06-23 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286795561/p459473.png)

- 用户自定义优先级，如下图所示，新增**一般紧急**并调整优先级顺序。

  该参数值以接口实际调用结果为准。优先级越高，数值越大。![iShot2022-06-23 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286795561/p459475.png)

### 参与者（involveMembers）

任务的参与者，可以全程参与该任务的进度，不需要执行任务。

任务的创建者和执行者默认为参与者。![8C920981-52E6-41F8-B6F9-DC6411F6DF7F](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286795561/p459519.png)

### 执行者（executorId）

任务的执行者，需要执行任务的人。任务完成后执行者可以将任务状态修改为已完成。![F7444AC0-4617-463D-97AF-E1B35D8ED5F1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286795561/p459522.png)

### 项目名称（project\_name）

项目名称。在项目管理应用中，可以创建多个项目。![mcjs1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2166944561/p444540.png)

### 任务名称（task\_name)

任务名称。可以在每个项目下创建任务并将任务指派给其他一名或者多名员工。![mcjs2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2166944561/p444543.png)
