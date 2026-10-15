---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/dingtalk-todo-task-overview"
namespace: "development"
slug: "dingtalk-todo-task-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 概述"
doc_id: "H6aJIvi3kT"
updated_at: "2026-07-30 09:19:03"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-todo-task-overview
> Path: 应用开发 / 服务端 API / 待办任务 > 概述
> Updated: 2026-07-30 09:19:03

# 概述

本文介绍了什么是待办，如何开通待办、待办接口能力介绍和如何接入待办接口能力等内容。

## 什么是待办

待办是钉钉的一个协同办公产品，帮助企业员工更高效的进行事项（工作任务）管理。钉钉待办提供了强大的开放能力，各类业务系统或企业自建应用可低成本的接入。更多介绍请查看[钉钉产品使用手册-待办](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmb7Dd340Y3GLq?dontjump=true%23%23)。

### **接入场景**

- **能接入待办的场景**

  适用于任务、打卡、通知、表单等场景。
- **不能接入待办的场景**

  含有广告信息或含有违反国家相关法律法规的内容。

### **接入流程**

#### **待办通知场景**

待办通知场景完全复用钉钉官方待办能力（与用户在钉钉客户端创建的待办完全一致），调用新增待办接口创建待办时不需要传三方详情页链接，用户在钉钉客户端操作时可以在待办列表直接完成，点击跳转详情时将跳转至钉钉官方待办详情页。流程如下图所示：

![待办通知场景](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0809491361/p327964.png)

#### **第三方业务自闭环场景**

第三方业务自闭环场景是创建待办时，需传入业务自身应用详情页链接，用户在钉钉客户端操作时无法在列表直接完成，仅支持直接跳转至三方应用详情页进行操作。流程如下图所示：

![三方业务自闭环场景](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0809491361/p327966.png)

### **使用案例**

| 说明 | 场景示意 | 接入后验证 |
| --- | --- | --- |
| **蚂蚁分工**  蚂蚁分工 | 适用于任务、打卡、通知、表单等场景。准备培训 | 入口：   - 钉钉导航 -> 待办 - 钉钉协作-> 待办（移动端）   调用接口后的能力：   - 待办出现在“首屏导航-待办列表” - 用户可在待办列表查看详情 - 待办未完成，会有红点提醒 - 用户可在列表或详情处理待办 - 用户可以删除待办 |
| **企业自建应用**  企业颞部 |

## 如何开通使用待办

待办是钉钉默认安装的官方应用。员工可以直接使用。

手机端：钉钉手机客户端-待办

![图片排版-手机展示-1张图1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8640488771/p449097.png)

电脑端：钉钉电脑客户端-待办

![图片排版-钉钉端展示-1张图1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8640488771/p449069.png)

## 开放概览

### 开放接口列表

待办提供了丰富的接口开放能力，开发者通过API接口可以实现和企业自由的业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建钉钉待办任务](0793-add-dingtalk-to-do-task.md) | 发起一个钉钉待办任务。 | 新版 |
| [创建钉钉个人待办任务](0794-api-createpersonaltodotask.md) | 创建一个钉钉“个人待办“任务。 | 新版 |
| [删除钉钉待办任务](0795-delete-dingtalk-to-do-tasks.md) | 删除钉钉待办任务信息。 | 新版 |
| [更新钉钉待办任务](0796-updates-dingtalk-to-do-tasks.md) | 更新钉钉待办任务信息及状态。 | 新版 |
| [更新钉钉待办执行者状态](0797-update-dingtalk-to-do-status.md) | 当待办存在多个执行者时，可调用本接口更新部分执行者的完成状态。 | 新版 |
| [查询企业下用户待办列表](0798-query-the-to-do-list-of-enterprise-users.md) | 获取该授权企业下某用户的待办列表。 | 新版 |
| [新增待办卡片类型配置](0799-add-todo-cardtype-configuration.md) | 新增一个待办卡片类型。 | 新版 |
| [更新待办卡片类型配置](0800-update-the-to-do-card-type-configuration.md) | 更新已有的待办卡片类型。 | 新版 |
| [获取待办卡片类型配置详情](0801-queries-the-to-do-card-type-configuration-details.md) | 根据ID获取一个待办卡片类型配置详情。。 | 新版 |

### **回调事件列表**

待办支持待办任务新增、更新、删除等回调事件：

- [待办任务新增](../04-LFcRvVD08N-事件订阅/0027-event-todo-task-create.md)
- [待办任务更新](../04-LFcRvVD08N-事件订阅/0028-event-todo-task-update.md)
- [待办任务删除](../04-LFcRvVD08N-事件订阅/0029-event-todo-task-delete.md)

## 名词解释

### 待办

需要完成的任务事项，分为工作待办和个人待办。一条待办任务包括待办标题、描述、截止时间、优先级、创建人、执行人、参与人等。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6731993871/p522228.png)

### 工作待办

企业内部应用和第三方企业应用创建的待办，以及OA审批、智能填表、项目等钉钉官方应用创建的待办。工作待办需要在业务系统详情页中完成，完成后调用更新待办方法更新状态。

### 个人待办

在钉钉待办中，通过“加号”入口创建的待办。个人待办可以在钉钉待办中直接完成。

### 待办红点

工作待办的红点数是未完成的待办数量，个人待办的红点数是已逾期的待办数量，钉钉客户端的待办红点总数是工作待办和个人待办的红点数之和。待办的红点规则暂时不支持自定义设置。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6731993871/p522225.png)

### 待办角色

待办中的角色包括创建人、执行人、参与人。

- 创建人，即创建待办的人，默认为待办的参与人，可以修改、完成、删除待办。用户创建的未完成待办在视图“我发起的”中。
- 执行人，即待办的执行人，逾期将会提醒执行者，执行人可以完成、删除、评论待办。待办支持多执行人，每个执行人可以完成自己的任务；当创建人完成任务后，每个执行人的任务都会被完成。用户作为执行人的未完成待办在视图“进行中”。
- 参与人，即参与待办的人。参与人的待办在“我参与的”中展示，待办逾期不会提醒参与者，参与人不能修改、完成待办，可以评论待办，具有跟进、抄送的作用。用户作为参与人的未完成待办在视图“我参与的”中。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6731993871/p522227.png)
