---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/organizational-brain-overview"
namespace: "development"
slug: "organizational-brain-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "组织大脑 > 概述"
doc_id: "WK7bkeFdsB"
updated_at: "2026-05-19 20:33:13"
---

> Source: https://open.dingtalk.com/document/development/organizational-brain-overview
> Path: 应用开发 / 服务端 API / 组织大脑 > 概述
> Updated: 2026-05-19 20:33:13

# 概述

## **什么是组织大脑**

**组织大脑**是钉钉官方出品的数智化组织人才管理系统，融合了钉钉服务的中大型企业组织的管理实践、行业经验、数据积累与产品能力。助力企业通过组织生产力洞察、数智化人才盘点与管理，做到知人善用、降本增效。更多详情参考[组织大脑使用手册](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Z0LYK27vwxp80YEeXmYlWo5Olb4md9eP?dontjump=true)。

## **组织大脑特点**

- **多元业态包容适配：**

  组织大脑脱胎于钉钉服务的中大企业组织的行业经验、以及阿里巴巴内部多元业务的管理实践，拥有高度的行业适配性及配置能力。
- **与钉融合数据互通：**

  钉钉强大的开放生态，让企业的业务流程、经营管理、组织人才管理实现相互打通、数据融合。
- **AI 加持智能领先：**

  AI 融入组织大脑多个业务场景，基于大数据的协同关系网络、全面人才画像的搜索推荐能力，让组织大脑成为企业管理者和 HR 最佳的数据人才官。

## **如何开通组织大脑**

- 方式一：服务商扫码下单，提供客户corpid即可。
- 方式二：客户组织管理员扫码下单，选择自己需要的规格即可。

  ![image (6)](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8478391171/p787158.png)

## **开放概览**

### **开放接口列表**

组织大脑提供了丰富的接口开放能力，开发者通过API接口可以实现组织大脑和企业业务系统打通。

#### 组织与人员

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [数据集成人员信息同步](0891-api-hrbrainimportempinfo.md) | 人员信息同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成入职信息同步](0892-api-hrbrainimportregist.md) | 入职信息同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成离职信息同步](0893-api-hrbrainimportdimission.md) | 离职信息同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成转正记录同步](0894-api-hrbrainimportregular.md) | 人员转正记录同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成异动记录同步](0895-api-hrbrainimporttransfereval.md) | 人员异动记录同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成组织架构同步](0896-api-hrbrainimportdeptinfo.md) | 组织架构同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成人员信息删除](0897-api-hrbraindeleteempinfo.md) | 删除已同步至组织大脑的人员信息，支持批量删除。 | 新版 |
| [数据集成入职记录删除](0898-api-hrbraindeleteregist.md) | 删除已同步至组织大脑的入职记录，支持批量删除。 | 新版 |
| [数据集成离职记录删除](0899-api-hrbraindeletedimission.md) | 删除已同步至组织大脑的离职记录，支持批量删除。 | 新版 |
| [数据集成转正数据删除](0900-api-hrbraindeleteregular.md) | 删除已同步至组织大脑的转正数据，支持批量删除。 | 新版 |
| [数据集成调岗记录删除](0901-api-hrbraindeletetransfereval.md) | 删除已同步至组织大脑的调岗记录，支持批量删除。 | 新版 |
| [数据集成组织架构数据删除](0902-api-hrbraindeletedeptinfo.md) | 删除已同步至组织大脑的组织架构数据，支持批量删除。 | 新版 |

#### 经历与档案

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [数据集成工作经历同步](0903-api-hrbrainimportworkexp.md) | 工作经历同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成教育经历同步](0904-api-hrbrainimporteduexp.md) | 教育经历同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成培训学习记录同步](0905-api-hrbrainimporttraining.md) | 人员培训学习记录同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成工作经历删除](0906-api-hrbraindeleteworkexp.md) | 删除已同步至组织大脑的工作经历，支持批量删除。 | 新版 |
| [数据集成教育经历删除](0907-api-hrbraindeleteeduexp.md) | 删除已同步至组织大脑的教育经历，支持批量删除。 | 新版 |
| [数据集成培训学习数据删除](0908-api-hrbraindeletetraining.md) | 删除已同步至组织大脑的培训学习数据，支持批量删除。 | 新版 |

#### **绩效与奖惩**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [数据集成绩效记录同步](0909-api-hrbrainimportperfeval.md) | 绩效记录同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成晋升记录同步](0910-api-hrbrainimportpromeval.md) | 晋升记录同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成奖励记录同步](0911-api-hrbrainimportawarddetail.md) | 奖励记录同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成处分记录同步](0912-api-hrbrainimportpundetail.md) | 处分记录同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成绩效记录删除](0913-api-hrbraindeleteperfeval.md) | 删除已同步至组织大脑的绩效记录，支持批量删除。 | 新版 |
| [数据集成奖励信息删除](0914-api-hrbraindeleteawardrecords.md) | 删除已同步至组织大脑的奖励记录，支持批量删除。 | 新版 |
| [数据集成处分记录删除](0915-api-hrbraindeletepundetail.md) | 删除已同步至组织大脑的处分记录，支持批量删除。 | 新版 |

#### 能力与标签

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [数据集成基础标签同步](0916-api-hrbrainimportlabelbase.md) | 基础标签同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成专业技能同步](0917-api-hrbrainimportlabelprofskill.md) | 专业技能同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成领域经验同步](0918-api-hrbrainimportlabelindustry.md) | 领域经验同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成自定义标签同步](0919-api-hrbrainimportlabelcustom.md) | 自定义标签同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成人员标签删除](0920-api-hrbraindeletetlabelbase.md) | 删除已同步至组织大脑的人员基础标签，支持批量删除。 | 新版 |
| [数据集成专业技能删除](0921-api-hrbraindeletelabelprofskill.md) | 删除已同步至组织大脑的专业技能，支持批量删除。 | 新版 |
| [数据集成领域经验删除](0922-api-hrbraindeletelabelindustry.md) | 删除已同步至组织大脑的领域经验，支持批量删除。 | 新版 |

#### 盘点数据

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [数据集成盘点数据同步](0923-api-hrbrainimportlabelinventory.md) | 盘点数据同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成盘点数据删除](0924-api-hrbraindeletelabelinventory.md) | 删除已同步至组织大脑的盘点数据，支持批量删除。 | 新版 |

#### 人才档案

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [人才档案照片查询](0925-api-hrbraintalentprofileattachmentquery.md) | 查询人员档案照片信息，支持批量查询。 | 新版 |
| [人才档案基础数据查询](0926-api-hrbraintalentprofilebasicquery.md) | 查询人员档案基础信息，支持批量查询。 | 新版 |
| [人员标签数据查询](0927-api-stafflabelrecordsquery.md#undefined) | 分页查询组织人员标签数据。 | 新版 |

#### **人才池**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [人才池信息查询](0928-api-hrbrainemppoolquery.md) | 分页查询人才池信息。 | 新版 |
| [人才池在池人员列表](0929-api-hrbrainemppooluser.md) | 分页获取人才池在池人员列表。 | 新版 |

#### **自定义模型**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [自定义模型数据同步](0930-api-hrbrainimportcustom.md) | 自定义模型信息同步至组织大脑，支持批量同步。 | 新版 |
| [数据集成删除自定义模型数据](0931-api-hrbraindeletecustom.md) | 删除已同步至组织大脑的自定义模型数据，支持批量删除。 | 新版 |

### **回调事件列表**

组织大脑支持人才池新增、人才池编辑和人才池人员新增等回调事件。

- [组织大脑人才池新增](../04-LFcRvVD08N-事件订阅/0182-events-hrbrain-talent-pool-add.md)
- [组织大脑人才池编辑](../04-LFcRvVD08N-事件订阅/0183-events-hrbrain-talent-pool-edit.md)
- [组织大脑人才池删除](../04-LFcRvVD08N-事件订阅/0184-events-hrbrain-talent-pool-delete.md)
- [组织大脑人才池人员新增](../04-LFcRvVD08N-事件订阅/0185-events-hrbrain-talent-pool-staff-add.md)
- [组织大脑人才池人员删除](../04-LFcRvVD08N-事件订阅/0186-events-hrbrain-talent-pool-staff-delete.md)
