---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/workflow-overview"
namespace: "development"
slug: "workflow-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 概述"
doc_id: "8oAXqBg2Oq"
updated_at: "2026-07-10 10:07:21"
---

> Source: https://open.dingtalk.com/document/development/workflow-overview
> Path: 应用开发 / 服务端 API / OA 审批 > 概述
> Updated: 2026-07-10 10:07:21

# 概述

本文介绍了OA审批产品、OA审批开放了哪些接口能力，如何接入OA审批能力以及审批案例等内容。

## 什么是OA审批

OA审批（智能工作流），是钉钉为企业提供的官方应用，可以快速建立审批流程，如请假、出差等。OA审批开放的接口可以对审批实例等进行操作，将企业原有的业务系统与钉钉OA审批打通。更多功能介绍，请参见[钉钉使用手册-OA审批](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/lo1YvX0prG98keM3X7aqVPw7xzbmLdEZ)。

以下应用类型均支持接入OA审批：

- 企业内部应用
- 第三方企业应用

## 什么是OA高级版

OA高级版，是钉钉 OA 审批团队新推出的商业化版本，详情请参见：[OA高级版全部权益介绍](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FEYs6dgD4wlLHABzOAGksE%3Fdd_mini_app_id%3D5000000004997171&pc_slide=true)

为满足广大开发者在个性化应用开发方面的需求，钉钉OA审批新增了一批面向[OA审批高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)客户的专享OpenAPI&解决方案。这些专享OpenAPI&解决方案将提供更丰富的能力，响应更个性化的业务需求，支持不同场景下的企业内部应用开发，建议开发者更合理、有效地使用OpenAPI，打造更健康的钉钉开放生态。

专享开放能力介绍详情请参见：[关于新增OA审批高级版专享OpenAPI和解决方案的说明](1442-description-of-new-oa-approval-premium-exclusive-openapi-and-solutions.md)。

- OA 高级版提供 30+专享开放API，包含批量同意或拒绝等高效的 API
- OA 高级版提供 2 个专享流程中心对接方案，支持使用三方流程+钉钉 OA 页面对接和自建应用集成钉钉 OA 审批来实现业务定制。

## **开放概览**

### **开放接口列表**

OA审批提供了丰富的接口开放能力，开发者通过API接口可以实现OA审批和企业业务系统打通。

#### **官方OA审批**

##### **审批表单**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建或更新审批表单模板](0491-create-an-approval-form-template.md) | 创建或更新一个OA审批的流程表单模板，可指定表单控件列表并生成默认审批流程。 | 新版 |
| [获取表单 schema](0492-obtain-the-form-schema.md) | 通过 processCode 获取对应表单的 schema 信息。 | 新版 |
| [获取审批单流程中的节点信息](0493-approval-process-prediction.md) | 获取审批单流程中的节点信息。 | 新版 |
| [获取指定用户可见的审批表单列表](0494-obtains-a-list-of-approval-forms-visible-to-the-specified.md) | 根据员工的userid分页获取该用户可见的审批表单列表。 | 新版 |
| [获取当前企业所有可管理的表单](0495-get-all-manageable-forms-for-the-current-enterprise.md) | 获取当前企业所有可管理的审批表单。 | 新版 |
| [查询已设置为条件的表单组件](0496-query-form-components-that-have-been-set-as-criteria-1.md) | 获取用户在当前企业所有可管理的审批表单。 | 新版 |

##### **审批实例**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [发起审批实例](0497-create-an-approval-instance.md) | 发起OA审批实例。 | 新版 |
| [获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md) | 根据审批实例ID，获取审批实例详情。 | 新版 |
| [撤销审批实例](0499-revoke-an-approval-instance.md) | 撤销发起的审批实例。 | 新版 |
| [添加审批评论](0500-official-approval-adds-approval-comments.md) | 对审批实例添加评论。 | 新版 |
| [获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md) | 获取权限范围内的相关部门审批实例ID列表。 | 新版 |

##### **审批钉盘空间&附件**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md) | 获取审批钉盘空间的ID并授予当前用户上传附件的权限。 | 新版 |
| [授权预览审批附件](0503-official-authorized-preview-approval-attachment.md) | 授权预览审批附件。 | 新版 |
| [授权下载审批钉盘文件](0504-download-the-approval-nail-file.md) | 根据钉盘空间spaceId和文件fileId对钉盘文件进行授权审批钉盘空间下载权限。 | 新版 |
| [下载审批附件](0505-download-an-approval-attachment.md) | 获取审批文件下载授权，并且生成下载链接。 | 新版 |

##### **审批任务**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [同意或拒绝审批任务](0506-approve-or-reject-the-approval-task.md) | 根据指定模板ID、实例ID、审批节点ID和审批人，对单个审批任务进行处理。 | 新版 |
| [获取用户待审批数量](0508-queries-the-number-of-requests-to-be-approved-by-users.md) | 根据用户的userid获取该用户待处理的审批数量。 | 新版 |
| [转交OA审批任务](0507-transfer-the-oa-approval-task.md) | 转交OA审批任务。 | 新版 |

#### **自有OA审批**

##### **审批表单**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md) | 创建或更新审批模板。 | 新版 |
| [获取模板code](0511-obtain-the-template-code.md) | 根据模板名称查询process\_code。 | 新版 |
| [删除模板](0512-self-owned-approval-deletion-template.md) | 删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。 | 新版 |

##### **审批实例**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建实例](0513-create-a-ticket-approval-instance.md) | 创建不带流程的审批实例。 | 新版 |
| [更新实例状态](0514-update-instance-status.md) | 更新实例状态。 | 新版 |
| [批量更新实例状态](0515-self-owned-batch-update-of-instance-status.md) | 批量更新实例状态。 | 新版 |

##### **流程中心任务**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md) | 创建OA审批的待办任务。 | 新版 |
| [查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md) | 可以查询到用户运行中的审批任务。 | 新版 |
| [更新流程中心任务状态](0518-update-process-center-task-status.md) | 更新待办任务的状态。 | 新版 |
| [批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md) | 批量取消流程中心待处理任务。 | 新版 |
| [清理OA审批数据](0520-clear-oa-approval-data.md) | 清理审批相关数据。 | 新版 |

### **专享开放**

专享开放介绍详情请参见：[关于新增OA审批高级版专享OpenAPI和解决方案的说明](1442-description-of-new-oa-approval-premium-exclusive-openapi-and-solutions.md)。

### 回调事件列表

#### **标准版**

企业内部应用参考：

- [审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)
- [审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)

第三方企业应用参考：

- [审批实例状态变更(广播)](../04-LFcRvVD08N-事件订阅/0033-event-workflow-instance-change-broadcast.md)
- [审批任务状态变更(广播)](../04-LFcRvVD08N-事件订阅/0034-event-workflow-task-change-broadcast.md)
- [审批实例状态变更(定向)](../04-LFcRvVD08N-事件订阅/0035-event-workflow-instance-change-directed.md)
- [审批任务状态变更(定向)](../04-LFcRvVD08N-事件订阅/0036-event-workflow-task-change-directed.md)

#### **高级版专享**

企业内部应用参考：

- [审批模板状态变更](../04-LFcRvVD08N-事件订阅/0040-events-workflow-form-change.md)
- [OA限时审批事件变更](../04-LFcRvVD08N-事件订阅/0037-events-oa-timeout-plugin-task-msg.md)

### **AppLink**

**钉钉应用标准链接协议，可以让钉钉的应用或功能直接通过链接即可访问**，如跳转某个审批页面、打开审批详情页、发起页等功能等。

- [打开审批首页](1424-open-approval-home-page.md)
- [打开审批筛选页](1426-open-approval-filter-page.md)
- [发起审批](1423-initiate-approval.md)
- [打开审批详情](1425-open-approval-details.md)

> **[!IMPORTANT]**
>
> 目前AppLink协议只支持OA审批高级版专享，OA审批标准版不支持。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p925369.png)

## **解决方案**

### **标准版**

- [官方OA审批：钉钉流程与页面对接](0489-use-the-dingtalk-oa-approval-process-and-page-interface.md)
- [自有OA审批：三方流程与页面对接](0477-use-three-party-process-and-page-docking.md)

### **高级版专享**

钉钉 OA 审批提供多种企业流程接入方案，满足企业各类业务管理和对接诉求。

- [官方OA审批：钉钉流程与页面对接](0489-use-the-dingtalk-oa-approval-process-and-page-interface.md)
- [自有OA审批：三方流程与页面对接](0477-use-three-party-process-and-page-docking.md)
- [审批页面托管：三方流程与钉钉页面对接](0482-use-the-three-party-process-to-interface-with-the-dingtalk-oa.md)
- [企业自建应用：专享OpenAPI集成审批](0479-use-the-exclusive-openapi-capability-to-dingtalk-oa-approval-through.md)
- [企业自建审批中心：批量快捷审批](0478-enterprise-self-built-approval-center-supports-batch-quick-approval-and-other.md)
- [自定义快捷审批：三方任务待办卡片审批](0480-custom-quick-approval-supports-quick-approval-of-pending-tasks-from.md)
- [自定义审批业务分组：待办中心业务分类](0481-user-defined-approval-business-group-supports-custom-business-classification-in-the.md)
- [审批流程托管：钉钉流程与三方页面对接](0490-approval-process-hosting-integration-mode-use-the-dingtalk-official-oa.md)

## **接入方案**

### **说明**

通过钉钉OA审批开放能力，提供四种企业业务系统接入钉钉OA审批的方案，实现业务系统发起审批，在钉钉端内处理审批，同时无缝连接钉钉沟通、待办、通知等功能，实现企业各种业务流程集中审批、高效协同。

更多功能介绍，请参见[钉钉使用手册-OA审批](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/lo1YvX0prG98keM3X7aqVPw7xzbmLdEZ)。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6666525271/p843389.png)

### **接入方式**

钉钉OA审批提供四种企业流程接入方案，满足企业各类业务管理和对接诉求。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p843388.png)

| **接入方式** | **方案说明** | **方案特点&价值** |
| --- | --- | --- |
| 三方流程+页面（钉钉端内打开） | [自有OA审批：三方流程与页面对接](0477-use-three-party-process-and-page-docking.md)  可在业务系统发起流程，调用钉钉**自有OA审批相关接口**创建钉钉OA审批流程，在钉钉端打开业务系统审批详情页处理流程。 | **更轻量**  1、接入简单，直接在钉钉端内打开业务系统页面审批  2、只有同意拒绝等基础操作，无和钉钉连接操作，如拉群  3、延续用户原来使用的流程和页面习惯，低成本快速使用 |
| 钉钉OA审批流程+页面 | [官方OA审批：钉钉流程与页面对接](0489-use-the-dingtalk-oa-approval-process-and-page-interface.md)  可在业务系统发起流程，调用钉钉**官方OA审批相关接口**创建钉钉OA审批流程，在钉钉端打开钉钉官方审批详情页处理流程。 | **更标准**  1、标准化对接，使用钉钉OA流程和页面能力，无缝和钉钉聊天、待办、通知连接，高效审批  2、复用钉钉官方OA审批流程引擎和表单组件能力，帮助不同业务的审批流程上钉，为用户在钉钉上提供一站式、多端统一的OA 审批产品体验 |
| 三方流程+钉钉OA审批页面（钉钉OA审批高级版专享） | [审批页面托管：三方流程与钉钉页面对接](0482-use-the-three-party-process-to-interface-with-the-dingtalk-oa.md)  可在业务系统发起流程，基于钉钉官方OA审批提供的**审批单据详情页搭建能力**，调用钉钉接口**用三方流程业务数据渲染钉钉OA审批页面**，在钉钉端打开钉钉官方OA审批详情页处理流程。 | **更灵活**  1、灵活对接，将不同业务系统的审批单结构、样式统一，为用户提供多端（移动端/PC/平板）一致体验  2、审批操作区按钮可自定义，同意、拒绝、转交、打印等等  3、托管后三方审批流转情况将汇集到钉钉官方审批效率看板中，管理层可通过流程效率统计报告全方位诊断企业的审批效率和合理性。 |
| 自建应用，集成钉钉OA审批（钉钉OA审批高级版专享） | [企业自建应用：专享OpenAPI集成审批](0479-use-the-exclusive-openapi-capability-to-dingtalk-oa-approval-through.md)  通过**钉钉OA审批高级版专享开放接口和前端页面AppLink协议**，支持企业自建应用，来实现业务应用的流程和钉钉侧流程**在自建应用统一批量处理**，帮助**实现企业自建审批中心**等个性化业务需求。 | **更定制**  1、定制对接，企业可根据业务，实现页面和功能逻辑的定制  2、专享OpenAPI和前端页面AppLink协议开放，将提供更丰富的能力，响应更个性化的业务需求，支持企业自建审批中心、流程交接等业务解决方案 |

## **名词解释**

### **审批表单**

一个预定义的模板，可以包含多个表单控件。员工填写表单提交后会生成审批实例。钉钉也提供了一系列通用的审批表单，例如请假、出差等，单击**创建新表单**可以直接使用。管理员可在[OA审批管理后台](https://aflow.dingtalk.com/dingtalk/web/query/dashboard?dinghash=aflowSetting#/aflowSetting)页面查看所有审批表单。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553867.png)

### **审批表单控件**

钉钉提供了丰富的审批表单控件，方便用户快捷定制审批表单。您可以新建或编辑已有的审批表单，单击**表单设计**，可新增或修改控件。请假表单的控件如下图所示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553861.png)

### **审批流程**

用户可以根据实际需求设计审批流程，例如设置审批人、审批条件等。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553876.png)

### **审批实例**

企业用户发起一个审批，即会产生一个审批的实例，如下图所示。每个审批实例，包含了用户在发起审批时填写的表单数据、审批人、审批人操作记录等数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553932.png)

### **审批节点**

一个审批流程可以有多个审批节点，每一个审批节点配置一个或多个审批人，根据节点审批人的不同可以分为以下两种情况：

- **单个审批节点只有一个审批人**，在当前审批人对此审批节点执行同意或拒绝操作时，此流程节点随即结束，并自动进行下一级审批。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553933.png)
- **单个审批节点有多个审批人**。每一个审批人对应一个审批任务。根据多个审批人审批方式的不同，可以分为以下三种情况：

  - **多个审批人依次审批**，一个审批人处理完成后按顺序自动发送审批任务给下一级审批人。
  - **多个审批人会签**，需要当前审批节点所有人都执行审批通过操作后，才会流到下一节点，否则流程被拒绝。
  - **多个审批人或签**，只需要当前审批节点中的一个审批人执行审批操作，当前流程节点随即结束。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553941.png)

### **审批任务**

一个审批节点可以生成一个或多个审批任务。每个审批任务会表明审批人是谁，审批人接到任务后可以做同意或拒绝等操作。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553946.png)

### **processCode**

审批表单的唯一编码。可以在审批表单编辑页-基础设置-页面底部查看。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1429463871/p553950.png)

### **bizCategoryId**

审批表单所属的业务分类标识。可通过[OA审批事件的事件体](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)或[获取表单 schema](0492-obtain-the-form-schema.md)接口获取。常用的套件业务分类标识参见下方**OA审批****套件业务分类标识**内容。

### **OA审批****套件业务分类标识**

| **业务分类标识** **bizCategoryId** | **套件名称** | **业务名称** |
| --- | --- | --- |
| open.com.dd.at.approveCheck | 打卡审批 | 考勤 |
| attendance.batchovertime | 加班 | 考勤 |
| attendance.supply | 补卡 | 考勤 |
| attendance.goout | 外出 | 考勤 |
| attendance.relieve | 换班 | 考勤 |
| alitrip.business | 出差 | 考勤 |
| hrm.termination | 离职 | 智能人事 |
| hrm.transfer | 转岗 | 智能人事 |
| hrm.regular | 转正 | 智能人事 |
| hrm.hire | 入职 | 智能人事 |
| hrm.terminationAndHandover | 离职&离职交接 | 智能人事 |
| hrm.handOver | 离职交接 | 智能人事 |
| hrm.hireTrial | 试岗入职 | 智能人事 |
| hrm.promotion | 晋升 | 智能人事 |
| hrm.transferAndSalary | 调岗调薪 | 智能人事 |
| hrm.hireAndSalary | 入职定薪 | 智能人事 |
| hrm.regularAndSalary | 转正调薪 | 智能人事 |
| hrm.promotionAndSalary | 晋升调薪 | 智能人事 |
| dingtalk.hrm.offer | offer审批 | 智能人事 |
| dingtalk.hrm.integratedSuite | 人事综合套件 | 智能人事 |
| dingtalk.businessFinance.reimbursement | 报销套件 | 智能财务 |
| dingtalk.businessFinance.payment | 付款套件 | 智能财务 |
| dingtalk.businessFinance.collection | 收款套件 | 智能财务 |
| dingtalk.businessFinance.receivable | 应收套件 | 智能财务 |
| dingtalk.businessFinance.returned | 应收回款 | 智能财务 |
| dingtalk.businessFinance.badDebt | 应收坏账 | 智能财务 |
| dingtalk.businessFinance.payable | 应付套件 | 智能财务 |
| dingtalk.businessFinance.payablePayment | 应付实付 | 智能财务 |
| dingtalk.businessFinance.noPayment | 应付免付 | 智能财务 |
| dingtalk.businessFinance.reserve | 备用金 | 智能财务 |
| dingtalk.businessFinance.reserveVerification | 备用金核销 | 智能财务 |
| dingtalk.businessFinance.reserveReturned | 备用金还款 | 智能财务 |
| dingtalk.businessFinance.transfer | 转账 | 智能财务 |
| dingtalk.businessFinance.invoiceApplication | 开票申请 | 智能财务 |
| dingtalk.businessFinance.costApplication | 费用申请 | 智能财务 |
| open.com.dd.suite.seal | 用印申请 | 智能合同 |
| open.com.dd.suite.icontract | 合同审批 | 智能合同 |
