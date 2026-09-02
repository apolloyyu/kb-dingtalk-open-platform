---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/crm-overview"
namespace: "development"
slug: "crm-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 概述"
doc_id: "a6nfglauIw"
updated_at: "2026-05-19 20:32:54"
---

> Source: https://open.dingtalk.com/document/development/crm-overview
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 概述
> Updated: 2026-05-19 20:32:54

# 概述

本文档介绍了什么是客户管理，如何开通客户管理，客户管理开放了哪些接口能力，以及如何接入客户管理能力等。

## 什么是客户管理

客户管理（官方CRM）是钉钉推出的官方应用，以客户为中心一站式管理协同，灵活配置满足各类内部管理诉求，助力企业提升客户转化率。同时提供“客户群”等能力，帮助连接客户、连接组织与组织，让沟通协同更高效。客户管理开放了相关表单、数据的增删改查接口等能力，帮助企业进行系统化的客户全生命周期管理。更多功能详情可参考[钉钉使用手册-客户管理](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/yZvMRzlLwOAWrR6274RAWnjY02pBqGox)。![客户管理概述1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7941692561/p440218.png)

## 如何开通客户管理

客户管理是钉钉默认安装的官方应用。员工可以在钉钉工作台打开应用并使用。

手机端：钉钉手机客户端-工作台

![iShot2022-01-17 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365832461/p385242.png)

PC端：钉钉PC客户端-工作台

![iShot2022-01-17 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8365832461/p385245.png)

## 开放概览

### **开放接口列表**

客户管理提供了丰富的接口开放能力，开发者通过API接口可以实现客户管理和企业业务系统打通。

#### **客户**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建个人或企业客户数据](1348-add-crm-personal-customers.md) | 添加CRM个人客户或企业客户 | 新版 |
| [批量新增个人或企业客户数据](1351-add-multiple-relationship-data-in-batches.md) | 批量新增个人客户、企业客户数据。 | 新版 |
| [更新个人或企业客户数据](1349-update-crm-personal-customers.md) | 更新CRM个人客户或企业客户信息。 | 新版 |
| [批量更新个人或企业客户数据](1352-update-multiple-relational-data-tables-at-a-time.md) | 批量修改个人客户、企业客户数据。 | 新版 |
| [删除个人或企业客户数据](1350-delete-crm-personal-customer.md) | 删除CRM个人客户或企业客户数据。 | 新版 |
| [批量获取个人或企业客户数据](1353-acquire-crm-individual-customers-in-batches.md) | 批量获取CRM个人客户或企业客户。 | 新版 |
| [获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md) | 获取CRM个人客户或企业客户的元数据描述。 | 新版 |
| [获取全量个人或企业客户数据](1354-crm-obtains-all-private-sea-customer-data.md) | 获取CRM个人或企业客户数据。 | 新版 |
| [根据指定条件查询个人或企业客户数据](1355-obtains-crm-individual-customers-in-batches-based-on-specified-query.md) | 根据指定条件查询CRM个人客户或企业客户数据。 | 新版 |
| [获取个人或企业客户查重字段](1356-obtain-duplicate-check-fields.md) | 获取客户管理中设置个人客户、企业客户的查重字段。 | 新版 |
| [查询客户数据](1358-querying-customer-data.md) | 根据客户的unionId查询客户详情信息。 | 新版 |
| [获取客户管理全局信息](1357-get-customer-management-global-information.md) | 获取客户管理全局信息。 | 新版 |
| [获取审批中创建与CRM客户关联的TAB表单元数据](1359-api-getrelatedviewtabmeta.md) | 获取OA审批里创建的与CRM客户关联的tab表单元数据，包括表单标题、关联的联系人控件id。 | 新版 |
| [获取审批里创建的与CRM客户关联的TAB表单数据实例列表](1360-api-getrelatedviewtabdata.md) | 获取OA审批里创建的与CRM客户关联的tab表单的实例数据，包括实例的标题、实例创建时间、实例摘要信息。 | 新版 |

#### **联系人管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [批量新增联系人数据](1361-add-contact-data-in-batches.md) | 批量新增联系人数据。 | 新版 |
| [批量修改联系人数据](1363-modify-contact-data-in-batches.md) | 批量修改联系人数据。 | 新版 |
| [删除联系人数据](1362-delete-crm-contact.md) | 删除当前组织CRM指定联系人的接口。 | 旧版 |
| [根据指定条件查询联系人数据](1365-api-getcontacts.md) | 根据指定查询条件批量获取联系人数据。 | 新版 |
| [按照ID列表批量获取联系人数据](1366-retrieves-contact-data-in-batches-based-on-the-id-list.md) | 根据联系人实例id列表批量获取联系人数据。 | 旧版 |
| [获取联系人的元数据](1364-gets-the-metadata-description-of-a-crm-contact-object.md) | 获取钉钉CRM联系人的元数据描述。 | 旧版 |

#### **跟进记录**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [根据指定条件查询跟进记录数据](1371-query-and-dingtalk-data-of-track-records-in-apsara-stack.md) | 根据指定查询条件批量获取跟进记录数据。 | 旧版 |
| [根据ID列表批量获取跟进记录数据](1372-dingtalk-the-primary-data-of-apsara-stack-agility-paas-allows-you.md) | 根据实例ID列表批量获取跟进记录数据。 | 旧版 |
| [获取跟进记录对象的元数据](1367-obtains-the-metadata-description-of-the-crm-follow-up-record-object.md) | 读取钉钉CRM跟进记录对象的元数据。 | 旧版 |
| [批量新增跟进记录数据](1368-batch-add-follow-up-record-data.md) | 批量新增客户的跟进记录。 | 新版 |
| [批量更新跟进记录数据](1369-batch-update-follow-up-record-data.md) | 批量更新客户的跟进记录。 | 新版 |
| [批量删除跟进记录数据](1370-batch-delete-follow-up-record-data.md) | 批量删除客户的跟进记录。 | 新版 |

#### **自定义对象**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建CRM自定义对象数据](1373-dingtalk-paas-master-create-custom-crm-object-data.md) | 创建自定义对象数据。 | 旧版 |
| [更新自定义对象数据](1375-crm-master-data-opens-interface-for-updating-custom-object-data.md) | 更新CRM自定义对象数据。 | 旧版 |
| [获取自定义对象的元数据](1376-get-metadata-description-of-crm-custom-object.md) | 读取钉钉CRM自定义对象的元数据描述。 | 旧版 |
| [根据指定条件查询自定义对象数据](1377-api-getobjectdata.md) | 根据指定条件分页查询自定义对象数据。 | 新版 |
| [按照ID列表批量获取CRM自定义表单数据](1378-retrieves-custom-crm-forms-from-the-id-list.md) | 根据实例ID列表批量获取CRM自定义表单数据。 | 旧版 |
| [删除CRM自定义对象数据](1374-delete-crm-custom-object-data.md) | 删除CRM自定义对象数据。 | 新版 |

#### **客户群**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建客户群](1379-create-a-customer-group.md) | 创建客户群。 | 新版 |
| [查询客户群列表](1380-query-the-list-of-customer-groups.md) | 根据指定过滤条件和排序规则，查询客户群列表数据。 | 新版 |
| [获取单个客户群详情](1381-obtain-a-single-customer-group.md) | 获取单个客户群的详情数据。 | 新版 |
| [批量查询客户群](1382-query-customer-groups-in-batches.md) | 批量查询客户群的信息。 | 新版 |
| [创建客户群组](1383-crm-create-group.md) | 创建客户群组。 | 新版 |
| [获取单个客户群组详情](1384-queries-the-details-of-a-single-customer-group.md) | 获取单个客户群组详情。 | 新版 |
| [更新客户群组](1385-crm-update-group.md) | 更新客户群组信息。 | 新版 |
| [查询客户群组列表](1386-query-groups.md) | 根据指定的筛选条件和排序规则，查询客户群组列表数据。 | 新版 |

### 回调事件列表

客户管理支持元数据实例和主数据实例新增、更新及删除回调事件。

- [主数据实例新增事件](../04-LFcRvVD08N-事件订阅/0167-events-ding-paas-object-data-create.md)
- [主数据实例删除事件](../04-LFcRvVD08N-事件订阅/0168-event-ding-paas-object-data-delete.md)
- [主数据实例更新事件](../04-LFcRvVD08N-事件订阅/0169-event-ding-paas-object-data-update.md)
- [CRM元数据](../04-LFcRvVD08N-事件订阅/0165-event-ding-crm-object-meta.md)

## 使用教程

钉钉提供了客户管理接口接入流程示例：

- [CRM客户数据操作流程](1341-customer-management-operation-process.md)
- [CRM联系人数据操作流程](1342-crm-contact-data-operation-process.md)
- [CRM跟进记录数据操作流程](1343-crm-follow-up-record-data-operation-process.md)
- [CRM自定义对象数据操作流程](1344-crm-custom-object-data-operation-process.md)
- [CRM客户群操作流程](1345-crm-customer-group-operation-process.md)
- [根据unionId获取客户信息流程](1346-retrieves-customer-information-based-on-the-union-id.md)

## 主数据结构

CRM中客户、联系人和跟进记录的表单结构如下表所示：

| 字段名 | 对象名称 | 字段类型 | 字段名称 | 字段描述 |
| --- | --- | --- | --- | --- |
| 企业客户 | crm\_customer | TextField | bizAlias:customer\_name | 客户姓名 |
| DDSelectField | bizAlias:customer\_follow\_up\_status | 客户跟进状态 |
| AddressField | bizAlias:address | 地址 |
| 个人客户 | crm\_customer\_personal | TextField | bizAlias:customer\_name | 客户姓名 |
| DDSelectField | bizAlias:customer\_follow\_up\_status | 客户跟进状态 |
| AddressField | bizAlias:address | 地址 |
| PhoneField | bizAlias:customer\_phone | 电话 |
| DDSelectField | bizAlias:gender | 性别 |
| DDDateField | bizAlias:birthday | 生日 |
| DDSelectField | bizAlias:identity | 身份 |
| TextField | bizAlias:wechat | 微信号 |
| TextField | bizAlias:qq | QQ |
| TextField | bizAlias:email | 邮箱 |
| 联系人 | crm\_contact | FormRelatedField | bizAlias:contact\_related\_customer | 关联的客户 |
| TextField | bizAlias:contact\_name | 联系人姓名 |
| PhoneField | bizAlias:contact\_phone | 电话 |
| 跟进记录 | crm\_follow\_record | FormRelatedField | bizAlias:follow\_record\_related\_customer | 关联的客户 |
| FormRelatedField | bizAlias:follow\_record\_related\_contact | 关联的联系人 |

## 名词解释

### **联系人**

联系人可以归属于某个企业客户或个人客户，一个企业/个人客户下最多30个联系人。

### **跟进记录**

用于保存对企业/个人客户的跟进记录。

### **自定义对象**

用户自定义的表单数据。

### **元数据**

客户管理中的企业客户、个人客户、联系人、跟进记录、自定义对象都支持用户自行设计对象结构的能力，元数据描述了这些对象的数据结构（字段名、类型、是否必填等）。

#### **客户动态**

客户相关的操作记录，修改客户、添加联系人、添加跟进记录等动作都会生成对应客户的客户动态。

#### **查重**

指防止客户数据重复创建的能力，企业客户默认查重规则为客户名称唯一，个人客户默认查重规则为电话号码唯一，企业可以自行在客户管理后台修改查重规则。

#### **客户群**

企业员工和客户沟通协作的IM群。

#### **客户群组**

客户群组是同类客户群的集合，客户群组拥有自动裂变的能力，当某个客户群内满员时，会自动裂变出一个新的客户群用于加人，助力企业的营销活动。
