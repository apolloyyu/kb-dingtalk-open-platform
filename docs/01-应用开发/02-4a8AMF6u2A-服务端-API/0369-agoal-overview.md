---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/agoal-overview"
namespace: "development"
slug: "agoal-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Agoal > 概述"
doc_id: "Ac2STnLDbF"
updated_at: "2026-07-10 10:04:51"
---

> Source: https://open.dingtalk.com/document/development/agoal-overview
> Path: 应用开发 / 服务端 API / Agoal > 概述
> Updated: 2026-07-10 10:04:51

# 概述

## **什么是Agoal**

Agoal是一款从战略拆解、目标管理&协同推进、到评价的一站式战略落地到执行管理工具（包含战略解码、组织目标、个人目标+任务协同、组织绩效、员工绩效等产品能力）。更多介绍参考[Agoal帮助手册](https://alidocs.dingtalk.com/i/p/nb9XJx9A7PRxPGyA/docs/ZgpG2NdyVXRmQ0jgCMvOOw258MwvDqPk?utm_medium=dingdoc_doc_plugin_url&utm_source=dingdoc_doc)。

## **Agoal的特点**

- **兼容多种目标类型**

  支持OKR、KPI、PBC等多种目标类型的录入，更加适合中国企业。
- **一体化目标管理**

  从战略&组织绩效→目标制定→过程跟进→绩效评价,实现目标绩效管理一体化。
- **多年实践经验打磨**

  基于阿里巴巴以及其他大型企业从战略到执行的实践经验，一起共创打磨。
- **与钉钉的深度融合**

  与钉钉底座深度融合，同Teambition、钉钉文档、组织大脑等一方品深度链接，实现高效协作

## **如何开通Agoal**

- **方式一**：拨打钉钉官方电话：400-111-6555
- **方式二**：点击[立即联系](https://survey.alibaba.com/apps/zhiliao/c4oUXo9uB)咨询我们的专业顾问

## **开放概览**

Agoal提供了丰富的接口开放能力，开发者通过API接口可以实现Agoal和企业业务系统打通。

### **开放接口列表**

#### **业务实体**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建业务实体](0371-api-agoalentitycreate.md) | 创建业务实体，如目标、指标等，并挂载到周期、考核任务下。 | 新版 |
| [更新业务实体](0372-api-agoalentityupdate.md) | 更新业务实体，如目标、指标等，并挂载到周期、考核任务下。 | 新版 |
| [Agoal业务数据查询](0373-agoal-business-biz-data-query.md) | 调用该接口通过组织目标Id，查询该目标详情信息。 | 新版 |

#### **计分卡**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取计分卡指标详情](0374-api-getindicatordetail.md) | 调用本接口获取计分卡指标详情，结果以json形式返回。 | 新版 |
| [获取Agoal指定部门下的计分卡维度和指标id](0375-api-getdeptscorecardindicator.md) | 调用本接口获取指定部门下计分卡的维度和指标。 | 新版 |

#### **指标库**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [通过指标编码批量查询指标列表](0376-api-agoalindicatorbatchquery.md) | 通过该接口，使用Agoal系统中的指标编码批量查询指标的详情信息。 | 新版 |
| [通过指标编码推送指标时间维度数据](0377-api-agoalindicatordatapush.md) | 通过该接口可以对该编码的指标时间维度数据做更新操作。 | 新版 |

#### **绩效考核**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建目标规则下的考核任务](0378-api-agoalperftaskcreate.md) | 创建目标规则下的任务，用于展示考核系统导入的指标列表。 | 新版 |
| [更新目标规则下的考核任务](0379-api-agoalperftaskupdate.md) | 更新目标规则下的考核任务，用于展示考核系统导入的指标列表。 | 新版 |
| [查询企业下的所有考核计划](0380-api-agoalorgperfplanquery.md) | 用于查询企业下的所有考核计划。 | 新版 |
| [查询某个考核计划的部门得分](0381-api-agoalorgperfdocquery.md) | 调用该接口通过组织计划Id，查询某个考核计划下的部门得分。 | 新版 |

目标与关键行动

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询组织目标详情](0382-api-agoalorgobjectivequery.md) | 调用本接口，通过业务编码分页查询Agoal业务数据。 | 新版 |
| [查询企业下个人目标详情](0383-api-getobjectivedetail.md) | 调用该接口通过目标id，查询该目标详情。 | 新版 |
| [获取 Agoal 组织目标列表](0384-api-agoalorgobjectivelist.md) | 调用本接口获取组织目标列表。 | 新版 |
| [查询企业下目标规则列表](0385-api-agoalobjectiverulelist.md) | 调用本接口查询企业下目标规则列表。 | 新版 |
| [查询企业下单个目标规则详情](0386-api-getobjectiveruledetail.md) | 调用该接口通过单个目标规则Id，查询目标规则详情。 | 新版 |
| [查询企业下指定个人目标的所有进展](0387-api-agoalobjectiveprogresslist.md) | 调用该接口通过个人目标Id，查询该目标下的所有进展。 | 新版 |
| [获取Agoal指定目标规则下的周期列表](0388-api-agoalobjectiveruleperiodlist.md) | 调用本接口获取指定目标规则下的周期列表。 | 新版 |
| [获取Agoal目标或关键结果关联的关键行动](0389-api-agoalobjectivekeyactionlist.md) | 调用本接口获取Agoal指定目标或者关键结果下关联的关键行动。 | 新版 |
| [获取Agoal指定组织下的所有目标规则列表](0390-api-agoalorgobjectiverulelist.md) | 调用本接口获取组织下的所有已启用目标规则列表。 | 新版 |
| [获取Agoal指定规则周期下负责人的目标列表](0391-api-agoaluserobjectivelist.md) | 调用本接口获取指定的规则周期下负责人的目标列表。 | 新版 |

系统协同与权限管理

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取Agoal用户管理员列表](0392-api-agoaluseradminlist.md) | 调用本接口获取Agoal用户管理列表。 | 新版 |
| [通过Agoal系统账号发送消息](0393-api-agoalsendmessage.md) | 调用本接口通过Agoal助手系统账号发送消息卡片。 | 新版 |

### **回调事件列表**

Agoal支持新增指标事件、修改指标事件、新增目标进展事件和个人目标删除事件等回调事件，更多事件可参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。
