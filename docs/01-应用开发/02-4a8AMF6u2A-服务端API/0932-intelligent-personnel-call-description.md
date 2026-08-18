---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-call-description"
namespace: "development"
slug: "intelligent-personnel-call-description"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 概述"
doc_id: "aAXy9wvuXk"
updated_at: "2026-07-14 09:10:43"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-call-description
> Path: 应用开发 / 服务端API / 智能人事 > 概述
> Updated: 2026-07-14 09:10:43

# 概述

本文介绍了智能人事产品，如何开通智能人事，智能人事开放了哪些接口能力，以及如何接入智能人事能力。

## 智能人事介绍

钉钉智能人事提供了强大、灵活、安全的人事解决方案，让企业迅速建立起来员工花名册，搭建员工入职、转正、调岗、离职流程，并给员工良好的使用体验。更多介绍请参见[钉钉使用手册-智能人事](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbEr9aV5DgXLq?dontjump=true%23%23)。

![iShot2022-04-19_11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9283540561/p431291.png)

## 如何开通智能人事

智能人事是钉钉默认安装的官方应用。员工可以在钉钉工作台打开应用并使用。

手机端：钉钉手机客户端-工作台

![智能人事-手机端](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3441993871/p437221.png)

电脑端：钉钉电脑客户端-工作台

![智能人事-电脑端](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3441993871/p437223.png)

## 开放概览

### 开放接口列表

智能人事提供了丰富的接口开放能力，开发者通过API接口可以实现智能人事和企业业务系统打通。

#### **职位管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取企业职位列表](0934-obtain-enterprise-position-information.md) | 用于根据特定条件分页查询企业的职位相关信息。 | 新版 |
| [获取企业职级列表](0935-obtain-enterprise-rank-information.md) | 用于分页查询企业的职级相关信息。 | 新版 |
| [获取企业职务列表](0936-obtain-enterprise-title-information.md) | 用于分页查询企业的职务相关信息。 | 新版 |

#### **花名册**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md) | 调用本接口获取员工花名册的元数据，包括花名册分组、字段等。 | 旧版 |
| [获取花名册字段组详情](0938-get-roster-field-group-details.md) | 调用本接口查询花名册的员工档案信息中有权限的字段列表。 | 旧版 |
| [获取员工花名册字段信息](0939-api-getemployeerosterbyfield.md) | 调用本接口查询员工花名册指定字段的信息，支持明细分组字段。 | 新版 |
| [更新员工花名册信息](0940-intelligent-personnel-update-employee-file-information.md) | 调用本接口更新员工档案信息，支持明细分组。 | 旧版 |
| [新增或删除花名册选项类型字段的选项](0941-intelligent-personnel-roster-field-option-modification.md) | 调用本接口新增或删除智能人事花名册选项类型字段的选项。 | 新版 |
| [查询花名册中有权限的字段列表](0942-query-the-list-of-fields-with-permissions-in-the-roster.md) | 调用本接口产品方案商查询花名册的员工档案信息中有权限的字段列表。 | 新版 |

#### **员工管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取待入职员工列表](0944-intelligent-personnel-query-the-list-of-employees-to-be-hired.md) | 查询企业待入职员工userid列表。 | 旧版 |
| [添加待入职员工](0945-add-employees-to-be-hired-supports-system-and-custom-fields.md) | 添加待入职员工信息。 | 新版 |
| [获取在职员工列表](0946-intelligent-personnel-query-the-list-of-on-the-job-employees-of-the.md) | 查询企业在职员工userid列表。 | 旧版 |
| [获取离职员工列表](0947-obtain-the-list-of-employees-who-have-left.md) | 查询企业离职员工userid列表。 | 新版 |
| [修改已离职员工信息](0948-modify-resigned-employee-information.md) | 修改智能人事中已离职员工的信息。 | 新版 |
| [批量获取员工离职信息](0949-obtain-resignation-information-of-employees-new-version.md) | 根据用户userId，批量查询员工的离职信息，如离职人员的部门ID、离职主动原因和被动原因等。 | 新版 |
| [员工加入待离职](0950-api-empstartdismission.md) | 给员工办理离职，加入到待离职列表。 | 新版 |
| [撤销员工待离职](0951-api-revoketermination.md) | 撤销员工待离职状态，从待离职列表中删除。 | 新版 |
| [更新待离职员工离职信息](0952-api-updateempdismissioninfo.md) | 根据离职用户 userId 和 离职原因 ID 等信息，更新待离职员工的离职信息。 | 新版 |
| [获取企业已有的所有离职原因](0953-api-getalldismissionreasons.md) | 获取企业已有的离职原因（不包含被删除的）。 | 新版 |

#### **员工关系**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [智能人事员工调岗](0954-intelligent-personnel-staff-transfer.md) | 调用本接口给智能人事员工调岗，支持以下内容调整，如员工部门列表、主部门、职务、职位和职级。 | 新版 |
| [确认员工离职并删除](0955-api-hrmprocessterminationandhandover.md) | 根据操作员工 ID、离职人员 ID，实现企业员工离职并删除的功能。 | 新版 |
| [添加企业待入职员工](0956-add-employees-to-be-hired-through-intelligent-personnel.md) | 根据企业待入职员工相关信息添加待入职员工。 | 旧版 |
| [智能人事员工调岗](0954-intelligent-personnel-staff-transfer.md) | 智能人事员工调岗，支持以下内容调整，如员工部门列表、主部门、职务、职位和职级。 | 新版 |

### 回调事件列表

智能人事支持人事档案变动等回调事件。

- [人事档案变动](../04-LFcRvVD08N-事件订阅/0142-personnel-file-change.md)
- [人事解决方案变更事件](../04-LFcRvVD08N-事件订阅/0143-personnel-solution-change-event.md)
- [人事平台员工异动事件v2](../04-LFcRvVD08N-事件订阅/0144-personnel-platform-employee-change-event-v2.md)
- [人事商业化方案事件](../04-LFcRvVD08N-事件订阅/0145-personnel-commercialization-program-event.md)
- [培训学习记录同步事件](../04-LFcRvVD08N-事件订阅/0146-training-learning-record-sync-events.md)
- [智能人事一体化应用授权](../04-LFcRvVD08N-事件订阅/0147-intelligent-personnel-integration-application-authorization.md)

## 使用教程

钉钉提供了智能人事接口接入流程示例，请参见[获取并补全员工的民族信息](0933-realize-automatic-push-of-employee-birthday-wishes-information.md)。

## 名词解释

### 离职原因（reason\_type）

人员离职时选择的离职原因，定义为reason\_type。

![iShot2022-03-09 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3441993871/p412587.png)

### 在职员工状态（status\_list）

在职员工的状态，定义为status\_list。
