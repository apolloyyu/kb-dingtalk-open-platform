---
title: "企业自建审批中心：批量快捷审批"
source_url: "https://open.dingtalk.com/document/development/enterprise-self-built-approval-center-supports-batch-quick-approval-and-other"
namespace: "development"
slug: "enterprise-self-built-approval-center-supports-batch-quick-approval-and-other"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 自由OA 审批 > 企业自建审批中心：批量快捷审批"
doc_id: "HQGsbadG1m"
updated_at: "2026-07-10 10:11:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-self-built-approval-center-supports-batch-quick-approval-and-other
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 自由OA 审批 > 企业自建审批中心：批量快捷审批
> Updated: 2026-07-10 10:11:22

# 企业自建审批中心：批量快捷审批

## **场景介绍**

客户多套业务系统（企业自研或采购的第三方系统）中的审批任务已接入钉钉OA审批流程中心，希望借助钉钉OA审批专享开放能力获取企业内指定用户的待处理、已处理、已发起、已抄送的审批列表等，帮助企业自建审批中心，来实现分来源筛选、批量审批等个性化业务需求。

如果公司管理层日常审批事项繁多，**希望把多个三方系统的审批流程和钉钉侧流程集中在企业自建应用内统一批量处理**，做一站式沉浸审批。通过钉钉OA审批高级版**专享开放的审批中心列表接口、批量处理审批任务接口等能力**可以快速满足客户需求。

## **业务流程**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1194471471/p925625.png)

## **实现效果**

- PC端效果示例

  ![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1194471471/p925626.gif)
- 移动端效果示例

  ![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1194471471/p925629.gif)

## **开发流程**

### **流程图**

以企业自建审批中心解决方案实现快捷批量审批为例，整体链路实现流程如下：

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1194471471/p925630.png)

### **接入流程简介**

本文档展示了，创建一个企业内部应用，使用钉钉官方OA审批集成模式、自有OA审批集成模式、以及部分钉钉OA高级版专享开放接口，帮助实现企业自建审批中心批量审批等个性化业务需求。通过创建/更新/删除审批模板、创建/更新审批实例、创建/更新/查询审批待办任务等基础API，以及获取钉钉OA审批中心列表接口、批量同意拒绝审批任务等专享开放能力，实现企业自建应用深度集成钉钉OA审批的场景案例。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. **自有OA审批集成：**三方业务系统分别对接钉钉自有OA审批，通过钉钉**自有OA审批相关接口**将业务系统的审批任务数据同步至钉钉OA审批流程中心，具体步骤参考[自有OA审批：三方流程与页面对接](0477-use-three-party-process-and-page-docking.md)。
2. **官方OA审批集成：**三方业务系统也可对接钉钉官方OA审批，通过钉钉**官方OA审批相关接口**直接在业务系统内发起钉钉官方OA审批流程，具体步骤参考：[官方OA审批：钉钉流程与页面对接](0489-use-the-dingtalk-oa-approval-process-and-page-interface.md)。
3. **用户主动发起：**用户也可直接在钉钉官方OA审批应用内提交审批流程，通过步骤1-3可以将分散的业务流程集中到钉钉OA审批中心进行管理。
4. **获取审批中心数据：**企业自建审批中心应用可调用[关于新增OA审批高级版专享OpenAPI和解决方案的说明](1442-description-of-new-oa-approval-premium-exclusive-openapi-and-solutions.md)中的查询审批中心列表相关接口（高级版专享），分别获取用户在钉钉审批中心的[待处理](0535-api-premiumgettodotasks.md)、[已处理](0536-api-premiumgetdonetasks.md)、[已发起的](0527-api-premiumgetsubmittedinstances.md)、[已收到的](0528-api-premiumgetnoticedinstances.md)审批列表数据。
5. **批量审批任务：**企业自建审批中心应用获取到用户审批中心任务列表数据后，可根据待处理列表接口返回的审批类型`processType`（0：官方OA审批、1：自有OA审批），分别对官方OA审批、自有OA审批的任务进行批量更新。

   1. **自有OA审批任务批量更新：**根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
   2. **官方OA审批任务批量更新：**业务系统根据审批实例`processInstanceId`和相应的任务节点`taskId`信息，调用新版服务端API-[批量同意或拒绝审批任务](0537-api-premiumbatchexecuteprocessinstances.md)，对一批具有不同审批实例ID、任务节点ID的审批任务，进行批量处理。
6. 审批单状态发生变化后，OA审批支持将[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)和[审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)等回调事件推送至业务系统侧，可以让企业应用能够更深度地与钉钉平台集成，实现信息共享和业务协同。具体使用教程参考：[事件订阅操作指南](0014-event-subscription-overview.md)。
