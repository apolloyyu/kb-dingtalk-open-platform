---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-yida"
namespace: "development"
slug: "overview-yida"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 概述"
doc_id: "VDv0jenfrW"
updated_at: "2026-08-07 14:50:58"
---

> Source: https://open.dingtalk.com/document/development/overview-yida
> Path: 应用开发 / 服务端 API / 宜搭 > 概述
> Updated: 2026-08-07 14:50:58

# 概述

本文介绍了宜搭产品、开放接口及如何调用宜搭接口流程等。

## 什么是宜搭

宜搭平台集合了页面编排(表单门户等)、业务模型编排、业务流程编排、服务编排、数据展现及分析 5大核心能力。宜搭构建的应用，天然具备云原生 (分布式计算、弹性扩容、异地容灾、CDN加速、企业级云安全) 和钉原生特性 (和钉钉的消息、通讯录 、待办打通，应用可以一键发布到钉钉群、工作台等)。更多介绍请参见[钉钉使用手册-宜搭](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/m0Xw6OYE4D7VLkB7vGP5WRq13rbjgPM5)。

![产品介绍-宜搭](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6736569361/p370764.png)

## 如何开通宜搭

宜搭是钉钉默认安装的官方应用。员工可以在钉钉工作台打开应用并使用。

手机端：钉钉手机客户端-工作台

![iShot2022-01-17 09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4342832461/p385213.png)

PC端：钉钉PC客户端-工作台

![iShot2022-01-17 09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4342832461/p385214.png)

## 开放概览

宜搭提供了丰富的接口开放能力，开发者通过API接口可以实现宜搭和企业业务系统打通。

### **流程**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [发起宜搭审批流程](0311-api-startinstance-v2.md) | 发起宜搭审批流程到钉钉开放平台。 | 新版 |
| [删除流程实例](0309-delete-the-process-instance.md) | 删除流程实例。 | 新版 |
| [终止流程实例](0308-terminate-a-process-instance.md) | 终止流程实例。 | 新版 |
| [预览审批流程](0306-api-previewpublishedprocess.md) | 发起流程前，预览流程流向。 | 新版 |
| [获取实例ID列表](0310-api-getinstanceidlist-v2.md) | 获取实例ID列表。 | 新版 |
| [批量获取流程实例列表](0313-queries-multiple-process-instances.md) | 根据流程实例ID，批量获取对应的流程实例详情。 | 新版 |
| [获取流程实例](0307-api-getinstances-v2.md) | 获取宜搭的流程实例信息。 | 新版 |
| [根据流程实例ID获取流程实例](0315-api-getinstancebyid-v2.md) | 根据指定流程实例ID获取流程实例详情。 | 新版 |
| [通过流程code获取流程定义](0314-obtain-definition-through-process-code.md) | 通过 processCode 获取流程定义。 | 新版 |

### **表单**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取指定应用下的表单列表](0334-depending-on-the-application-id-to-get-the-form-list.md) | 分页获取应用下的表单列表。 | 新版 |
| [获取表单内的组件信息](0332-get-form-field-information-based-on-form-uuid.md) | 根据表单ID，获取单据或流程表单内的组件信息。 | 新版 |
| [查询表单实例数据](0321-api-searchformdatas-v2.md) | 查询表单实例数据。 | 新版 |
| [保存表单数据](0316-api-saveformdata-v2.md) | 新增一条无审批流程的宜搭表单实例。 | 新版 |
| [更新表单数据](0318-api-updateformdata-v2.md) | 更新表单数据。 | 新版 |
| [查询表单数据](0317-api-getformdatabyid-v2.md) | 通过表单实例ID查询表单数据。 | 新版 |
| [获取员工组件的值](0330-gets-the-value-of-the-employee-component.md) | 获取员工组件的值。 | 新版 |
| [获取表单组件定义列表](0333-get-a-list-of-form-component-definitions.md) | 获取表单组件定义列表。 | 新版 |
| [获取子表组件数据](0329-obtain-child-table-component-data.md) | 通过表单实例ID和子表组IDd获取子表组件数据。 | 新版 |
| [删除表单数据](0319-delete-form-data.md) | 删除表单数据。 | 新版 |
| [获取多个表单实例ID](0324-api-searchformdataidlist-v2.md) | 获取多个表单实例ID。 | 新版 |
| [批量获取表单实例数据](0326-obtain-multiple-form-instance-data.md) | 批量获取表单实例详情信息。 | 新版 |
| [批量删除表单实例](0325-delete-multiple-form-instances.md) | 批量删除表单实例数据。 | 新版 |
| [批量创建表单实例](0320-create-multiple-form-instances.md) | 批量创建表单实例数据。 | 新版 |
| [批量更新表单实例内的组件值](0336-batch-update-of-component-values-in-form-instances.md) | 根据宜搭表单实例Id，批量更新宜搭表单实例的组件值。 | 新版 |
| [新增或更新表单实例](0323-api-createorupdateformdata-v2.md) | 使用筛选条件新增或更新表单实例。 | 新版 |
| [通过高级查询条件获取表单实例数据（包括子表单组件数据）](0337-api-searchformdatasecondgeneration-v2.md) | 使用筛选条件获取表单实例详情。 | 新版 |
| [通过高级查询条件获取表单实例数据（不包括子表单组件数据）](0338-obtain-form-instance-data-using-advanced-query-conditions-excluding-subform.md) | 使用筛选条件获取表单实例详情，不包括子表单组件数据。 | 新版 |
| [通过表单实例数据批量更新表单实例](0339-update-multiple-form-instances-with-the-form-instance-data.md) | 根据宜搭表单组件数据，批量更新表单实例信息。 | 新版 |
| [查询表单的变更记录](0322-change-records-of-query-forms.md) | 查询宜搭表单下的变更记录。 | 新版 |
| [获取流程设计结构](0327-api-getprocessdesign.md) | 根据流程版本ID获取宜搭的流程结构，包括流程节点、拓扑关系、高级配置等信息。 | 新版 |
| [获取组件别名列表](0328-api-getformcomponentaliaslist.md) | 获取组件别名列表。 | 新版 |

### **任务**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取审批记录](0342-queries-an-approval-record.md) | 获取审批记录。 | 新版 |
| [同意或拒绝宜搭审批任务](0345-execute-approval-tasks.md) | 同意或拒绝宜搭审批任务。 | 新版 |
| [获取组织内某人提交的任务](0348-obtains-the-tasks-submitted-by-someone-in-an-organization.md) | 获取组织内某人提交的任务。 | 新版 |
| [获取组织内已完成的审批任务](0350-obtains-the-completed-approval-tasks-in-an-organization.md) | 获取组织内已完成的审批任务。 | 新版 |
| [转交任务](0341-transfer-tasks.md) | 转交任务。 | 新版 |
| [查询流程运行任务（VPC）](0346-query-process-running-tasks-vpc.md) | 查询流程运行任务（VPC）。 | 新版 |
| [获取任务列表（组织维度）](0347-query-tasks-from-the-organization-dimension.md) | 获取组织维度任务列表。 | 新版 |
| [获取发送给用户的通知](0344-get-notifications-sent-to-users.md) | 获取发送给用户的通知。 | 新版 |
| [查询抄送我的任务列表（应用维度）](0351-query-copied-my-task-list-application-dimension.md) | 查询抄送我的任务列表（应用维度）。 | 新版 |
| [批量执行宜搭审批任务](0343-batch-execution-should-take-the-lead-of-approval-tasks.md) | 批量执行宜搭表单实例的审批任务。 | 新版 |
| [提交评论](0340-submit-comment.md) | 提交表单或流程实例下的评论。 | 新版 |
| [批量查询宜搭表单实例的评论](0349-batch-query-of-comments-appropriate-for-form-instances.md) | 批量查询宜搭表单下的所有评论。 | 新版 |

### **附件**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取宜搭附件临时免登地址](0352-obtain-the-temporary-free-access-address-of-yixian-accessories.md) | 获取宜搭附件临时免登地址。 | 旧版 |

### **应用**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询宜搭应用列表](0353-query-the-application-list.md) | 查询组织下的宜搭应用列表。 | 旧版 |

### **平台管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建代理关系](0354-api-createagenttask.md) | 设置代理人在有效期内承担被代理人流程审批工作。 | 新版 |
| [修改代理信息](0355-api-updateagenttask.md) | 根据代理关系唯一标识（agentUuid）修改指定代理的配置信息。 | 新版 |
| [撤销代理关系](0356-api-cancelagenttask.md) | 根据代理关系唯一标识（agentUuid）撤销指定的代理关系。 | 新版 |
| [获取代理列表](0357-api-getagenttasks.md) | 批量查询代理关系列表。 | 新版 |
| [批量更新宜搭角色成员](0358-batch-rolemembers.md) | 根据角色uuid批量新增或更新宜搭角色成员（可同时指定成员的角色管理范围）。 | 新版 |
| [批量删除宜搭角色成员](0359-batch-deleterolemembers.md) | 根据角色id和角色成员id列表删除指定角色成员。 | 新版 |
| [获取指定宜搭角色的角色详情](0361-get-roledetailbyid.md) | 获取指定宜搭角色的角色详情。 | 新版 |
| [更新指定矩阵的明细数据](0360-api-saveandupdatematrixdata.md) | 根据矩阵ID批量修改或新增指定矩阵的明细数据。 | 新版 |
| [获取指定权限矩阵的明细数据](0362-api-getmatrixdetailbyid.md) | 根据矩阵ID获取指定权限矩阵的明细数据，返回信息包含矩阵的表头定义数据。 | 新版 |
| [批量删除指定矩阵的明细数据](0363-api-deletematrixdatabyrowids.md) | 通过矩阵ID和行ID列表批量删除指定矩阵的明细数据。 | 新版 |

### **服务调用**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询宜搭表单服务调用执行记录](0364-the-query-should-be-based-on-the-execution-records-of.md) | 根据宜搭表单Id查询对应的服务调用执行记录信息。 | 新版 |

### **服务日志**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取集成自动化日志详情](0365-api-getautoflowlogdetail.md) | 通过集成自动化的实例 id 获取日志详情信息。 | 新版 |
| [分页获取集成自动化日志列表](0366-api-pageautoflowlog.md) | 根据表单信息数据，获取集成自动化日志列表。 | 新版 |
