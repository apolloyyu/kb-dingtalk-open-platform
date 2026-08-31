---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/ai-overview-of-education"
namespace: "development"
slug: "ai-overview-of-education"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 概述"
doc_id: "lSX1FsRbYd"
updated_at: "2026-07-20 09:25:39"
---

> Source: https://open.dingtalk.com/document/development/ai-overview-of-education
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 概述
> Updated: 2026-07-20 09:25:39

# 概述

本文介绍了什么是新教育，新教育开放了哪些接口能力，以及如何接入新教育能力。

## 什么是新教育

新教育提供了线上授课、在线布置及批改作业等，让家校沟通更高效，给用户良好的使用体验。更多介绍请参见[钉钉使用手册-新教育](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/3xRN9bGQyw4JbAmG3ZDNVzXPADKnorv6)。

![111](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3305725561/p449558.png)

## **家校通讯录2.0**

### **支持类型**

家校通讯录2.0接口，支持“**基础教育通讯录**”和“**自定义家校通讯录**”两种类型的通讯录。

![通讯录类型](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0434199951/p148961.png)

### **部门完整示例**

当前一个测试组织，其下包含基础教育通讯录和自定义通讯录两种类型。以下通过获取部门列表，完整的展示整条链路的数据。

1. 基础教育经典类型

   顶层节点校区ID：4240004

   1. 其中一个校区下的所有学段列表：

      ```
      {
        "result": {
          "details": [
            {
              "dept_id":4242002,
              "nick": "",
              "chain": "[4240004]",
              "feature": "{\"name_mode\":\"number\",\"period_type\":\"kindergarten\"}",
              "name": "幼儿园",
              "contact_type": "classic",
              "dept_type": "period"
            }
          ],
          "has_more": false,
          "super_id": 4240004
        },
        "success": true,
        "errcode": 0,
        "request_id":"63h2j929f9oj"
      }
      ```
   2. 其中一个学段下的所有年级列表

      ```
      {
        "result": {
          "details": [
            {
              "dept_id":4242003,
              "nick": "",
              "chain": "[4240004, 4242002]",
              "feature": "{\"grade_level\":1,\"start_year\":\"2019\"}",
              "name": "一年级",
              "contact_type": "classic",
              "dept_type": "grade"
            },
            {
              "dept_id":4242004,
              "nick": "",
              "chain": "[4240004, 4242002]",
              "feature": "{\"grade_level\":2,\"start_year\":\"2018\"}",
              "name": "二年级",
              "contact_type": "classic",
              "dept_type": "grade"
            },
            {
              "dept_id":4242005,
              "nick": "",
              "chain": "[4240004, 4242002]",
              "feature": "{\"grade_level\":3,\"start_year\":\"2017\"}",
              "name": "三年级",
              "contact_type": "classic",
              "dept_type": "grade"
            }
          ],
          "has_more": false,
          "super_id": 4242002
        },
        "success": true
        "errcode": 0,
        "request_id":"10c0wt6haqhdo"
      }
      ```
   3. 其中一个年级下的所有班级列表

      > **[!NOTE]**
      >
      > 班级是叶子节点，其下不存在接口可返回的结构数据。

      ```
      {
        "result": {
          "details": [
            {
              "dept_id":4242006,
              "nick": "",
              "chain": "[4240004, 4242002, 4242005]",
              "feature": "{\"class_level\":1,\"grade_level\":3}",
              "name": "三年级1班",
              "contact_type": "classic",
              "dept_type": "class"
            }
          ],
          "has_more": false,
          "super_id": 4242005
        },
        "success": true,
        "errcode": 0,
        "request_id":"plqhiw9f9pa0"
      }
      ```
2. 自定义通讯录类型：

   顶层节点id：4240016

   1. 其中一个自定义顶层节点下的所有子节点

      ```
      {
        "result": {
          "details": [
            {
              "dept_id":4240017,
              "nick": "",
              "chain": "[4240016]",
              "feature": "{}",
              "name": "2020",
              "contact_type": "custom",
              "dept_type": "dept"
            }
          ],
          "has_more": false,
          "super_id": 4240016
        },
        "success": true,
        "errcode": 0,
        "request_id":"plqhiw9f9pa0"
      }
      ```
   2. 其中一个自定义节点下的所有班级节点

      ```
      {
        "result": {
          "details": [
            {
              "dept_id":4240018,
              "nick": "",
              "chain": "[4240016, 4240017]",
              "feature": "{\"class_level\":0,\"grade_level\":0}",
              "name": "自定义下的班级",
              "contact_type": "custom",
              "dept_type": "class"
            }
          ],
          "has_more": false,
          "super_id": 4240017
        },
        "success": true,
        "errcode": 0,
        "request_id":"plqhiw9f9pa0"
      }
      ```

## **局校关联**

钉钉提供了局校关联接口供开发者使用。关联组织是钉钉推出一项有关组织架构管理的新功能，旨在帮助大型组织解决人员臃肿带来的管理难题，实现管理职责下放，同时与上下游合作伙伴实现跨组织的沟通、协同。

- [局校关联组织概述](0152-associated-organizations-overview.md)
- [获取主干组织列表](0154-obtain-backbone-organization-list.md)
- [获取分支组织列表](0155-obtains-the-branch-organization-list.md)

## 开放概览

### **开放接口列表**

新教育提供了丰富的接口开放能力，开发者通过API接口可以实现新教育和企业业务系统打通。

#### **通用基础**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取学段元数据列表](1128-dingtalk-the-main-data-of-the-education-ecosystem-to-query.md) | 获取学段元数据列表。 | 旧版 |
| [获取学科元数据列表](1134-dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject.md) | 获取学科元数据列表。 | 旧版 |
| [创建学科实例](1129-create-dingtalk-education-subject-instance.md) | 创建学科实例。 | 旧版 |
| [更新学科实例](1130-update-dingtalk-education-instance.md) | 更新学科实例。 | 旧版 |
| [删除学科实例](1131-delete-dingtalk-education-disciplines.md) | 删除学科实例。 | 旧版 |
| [获取学科实例详情](1132-query-dingtalk-education-subject-instances.md) | 获取学科实例详细信息。 | 旧版 |
| [获取学科实例列表](1133-get-the-list-of-subject-examples.md) | 获取学科实例列表。 | 旧版 |

#### **在线课堂**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建课程](1137-create-course.md) | 创建课程。 | 旧版 |
| [修改课程](1138-modify-course.md) | 修改课程。 | 旧版 |
| [删除课程](1139-delete-course.md) | 删除课程。 | 旧版 |
| [获取课程详情](1140-get-course-details.md) | 获取指定课程的详细信息。 | 旧版 |
| [获取课程列表](1141-get-course-list.md) | 获取课程列表。 | 旧版 |
| [添加课程参与方](1142-add-course-participants.md) | 添加课程参与方。 | 旧版 |
| [获取课程参与方列表](1143-get-a-list-of-course-participants.md) | 获取课程参与方列表。 | 旧版 |
| [移除课程参与方](1144-remove-course-participants.md) | 移除课程参与方。 | 旧版 |
| [开始课程](1145-start-course.md) | 开始课程。 | 旧版 |
| [加入课程](1146-join-course.md) | 加入课程。 | 旧版 |
| [结束课程](1147-end-course.md) | 结束课程。 | 旧版 |
| [回放课程](1148-replay-course.md) | 获取授课回放链接，用于进行在线课堂授课的内容回放。 | 旧版 |
| [获取课堂概要数据](1149-get-course-summary-data.md) | 获取课堂概要数据。 | 旧版 |
| [获取课堂明细数据](1150-obtain-course-detail-data.md) | 获取课堂明细数据。 | 旧版 |

#### **家庭**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [家庭Feed同步](1151-dingtalk-education-family-feed-synchronization.md) | 同步钉钉教育家庭Feed。 | 旧版 |
| [查询家庭孩子信息](1152-query-family-child-information.md) | 根据孩子的userId查询家庭孩子信息。 | 旧版 |
| [学习推荐数据回流](1153-learn-to-recommend-data-backflow.md) | 学习推荐数据回流。 | 旧版 |
| [静态推荐数据同步](1154-statically-recommended-data-synchronization.md) | 同步静态推荐数据。 | 旧版 |

#### **家校通讯录2.0**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取部门详情](1155-obtains-queries-department-details.md) | 查看某个部门详情。 | 旧版 |
| [获取部门列表](1156-obtains-the-department-node-list.md) | 查看某个部门下的所有子部门列表。 | 旧版 |
| [获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md) | 查看班级下的人员身份列表。 | 旧版 |
| [获取人员详情](1158-obtain-the-identity-details-of-home-school-personnel.md) | 查看班级下的人员详细信息。 | 旧版 |
| [获取班级内学生的关系列表](1159-queries-the-list-of-relationships.md) | 查看班级下的所有学生的关系列表。 | 旧版 |
| [获取学生监护人详情](1160-obtain-the-relationship-between-home-and-school-personnel.md) | 查看班级下某个监护人的详情。 | 旧版 |
| [初始化家校架构](1161-initialize-the-home-school-architecture.md) | 初始化家校结构。 | 旧版 |
| [创建学段](1162-create-a-learning-segment.md) | 在指定校区下创建学段。 | 旧版 |
| [创建年级](1163-create-grade.md) | 创建年级。 | 旧版 |
| [创建班级](1164-create-a-class.md) | 在指定的年级下创建班级。 | 旧版 |
| [添加学生](1165-add-student.md) | 在指定的班级下新增学生信息。 | 旧版 |
| [添加家长](1166-add-parent.md) | 在指定的班级下添加家长信息。 | 旧版 |
| [添加老师](1167-add-teacher.md) | 在指定班级下新增老师信息。 | 旧版 |
| [学生调班](1168-shift-students.md) | 学生调班。 | 新版 |
| [更新班级](1171-api-updateclass.md) | 在指定的班级下更新班级信息。 | 新版 |
| [更新学生](1172-api-updatestudent.md) | 在指定的班级下更新学生信息。 | 新版 |
| [更新家长](1173-api-updateguardian.md) | 在指定的班级下更新学生家长信息。 | 新版 |
| [删除老师](1174-delete-teacher.md) | 删除老师。 | 新版 |
| [删除学生](1175-delete-student.md) | 删除学生。 | 新版 |
| [删除家长关系](1176-delete-parent-relationship.md) | 删除与此家长关联的家长身份。 | 新版 |
| [删除家校部门](1177-delete-home-school-department.md) | 删除家校部门。 | 新版 |
| [创建自定义校区或部门](1178-create-a-custom-campus-or-department.md) | 创建自定义校区或部门。 | 新版 |
| [创建自定义部门下的班级](1179-create-classes-in-a-custom-department.md) | 创建自定义部门下的班级。 | 新版 |

#### **高校通讯录**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建个人账号用户](1182-api-addcollegecontactuser.md) | 创建新的个人账号用户。 | 新版 |
| [创建高校账号用户](1183-api-addcollegecontactexclusive.md) | 创建新的高校账号用户。 | 新版 |
| [更新个人账号用户信息](1184-api-updatecollegecontactuser.md) | 更新个人账号用户信息。 | 新版 |
| [更新高校账号用户信息](1185-api-updatecollegecontactexclusive.md) | 更新高校账号用户信息。 | 新版 |
| [修改用户成员类型](1186-api-updatecollegeuseremptype.md) | 修改用户成员类型，将教职工转变成学生，或学生转变成教职工。 | 新版 |
| [查询用户信息详情](1187-api-querycollegecontactuserdetail.md) | 获取指定用户的详细信息。 | 新版 |
| [创建组织单元](1188-api-createcollegecontactdept.md) | 创建新的组织单元(即部门)。 | 新版 |
| [更新组织单元](1189-api-updatecollegecontactdept.md) | 更新指定的组织单元（即部门）。 | 新版 |
| [获取组织单元详情](1190-api-getcollegecontactdeptdetail.md) | 根据组织单元ID获取指定组织单元（即部门）详情。 | 新版 |
| [获取子组织单元列表](1191-api-listcollegecontactsubdepts.md) | 获取组织单元下的所有直属子组织单元列表。 | 新版 |
| [获取组织单元支持的部门类型](1192-api-listcollegecontactdepttypeconfig.md) | 获取组织单元可以配置的部门类型。 | 新版 |
| [获取行政组织架构部门详情](1193-api-getcollegecontactstandardstrudeptdetail.md) | 获取行政组织架构部门详情。 | 新版 |

#### **班级圈**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取班级圈话题列表](1194-obtain-a-topic-list-of-class-circles.md) | 获取班级圈话题列表。 | 旧版 |
| [获取班级圈动态列表](1195-dynamic-list-opening-of-class-circle.md) | 获取班级圈动态列表。 | 旧版 |

#### **数字化证书**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取数字化证书](1196-obtain-digital-certificate.md) | 获取数字化证书。 | 旧版 |

### **回调事件列表**

新教育支持部门新增、部门更新、部门删除及人员新增等多种回调事件，更多事件参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

## **开发教程**

钉钉提供了签到接口接入流程示例：

- [钉钉教育接入流程](1127-education-application-solution.md)
