---
title: "家校通讯录事件"
source_url: "https://open.dingtalk.com/document/development/home-school-address-book-event"
namespace: "development"
slug: "home-school-address-book-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 家校通讯录事件"
doc_id: "7JrImsVaxN"
updated_at: "2025-10-16 14:31:57"
---

> Source: https://open.dingtalk.com/document/development/home-school-address-book-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 家校通讯录事件
> Updated: 2025-10-16 14:31:57

# 家校通讯录事件

本文介绍了家校通讯录事件的相关说明。

## 事件类型

家校通讯录事件支持以下类别：

| **类别** | **企业自主开发应用** | **服务商开发** |
| --- | --- | --- |
| 人员变更事件 | 支持 | 支持 |
| 部门变更事件 | 支持 | 支持 |

当家校通讯录发生变化，并且注册回调事件时填写的事件类型“call\_back\_tag”包含家校通讯录事件，比如call\_back\_tag字段为“edu\_user\_insert”“[,“edu\_user\_relation\_insert”]”，那么家校通讯录发生“家校通讯录人员身份新增”和“家校通讯录人员关系新增”，钉钉服务器会向回调url推送事件。此回调事件推送的是最简单的数据，建议配合API查询详情。

| **事件类型** | **类别** | **说明** |
| --- | --- | --- |
| edu\_user\_insert | 人员身份新增 | 人员身份新增。 |
| edu\_user\_update | 人员身份更新 | 人员身份更新。 |
| edu\_user\_delete | 人员身份删除 | 人员身份删除。 |
| edu\_user\_relation\_insert | 人员关系新增 | 人员关系新增。 |
| edu\_user\_relation\_update | 人员关系更新 | 人员关系更新。 |
| edu\_user\_relation\_delete | 人员关系删除 | 人员关系删除。 |
| edu\_dept\_insert | 部门节点新增 | 部门节点新增。 |
| edu\_dept\_update | 部门节点更新 | 部门节点更新。 |
| edu\_dept\_delete | 部门节点删除 | 部门节点删除。 |

## 人员身份新增

**示例：**

```
{
    "EventType": "edu_user_insert",
    "corpId":"dinge8a56572f80b02a8ffexxxx",
    "role":"teacher",
    "feature":"{\"isAdviser\":0}",
    "classId":4240006,
    "name":"eliot",
    "userId":"manager9707"
  }
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | 12344556 | 组织id。 |
| userId | String | 123344 | 用户id。 |
| role | String | teacher | 此人在家校的角色类型。   - **teacher**：老师 - **guardian**：监护人。 - **student**: 学生 |
| name | String | eliot | 此人在此班级的名字。 |
| classId | Number | 4240006 | 班级ID。 |
| feature | String |  | JSON格式，各个角色下存在不同属性。 |
| isAdviser |  |  | 是否班主任，老师角色下有效。 |
| studentNo |  |  | 学号，学生角色下有效。 |
| syncAction | String | edu\_user\_insert | 事件类型。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 人员身份更新

**示例：**

```
{
    "EventType": "edu_user_update",
    "corpId":"1233445556",
    "role":"guardian",
    "feature":"{}",
    "classId":4240006,
    "name":"alex爸爸/alan爸爸",
    "userId":"manager9707"
  }
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | 12344556 | 组织id。 |
| userId | String | 123344 | 用户id。 |
| role | String | teacher | 此人在家校的角色类型。   - **teacher**：老师 - **guardian**：监护人。 - **student**: 学生 |
| name | String | alan爸爸 | 此人在此班级的名字。 |
| classId | Number | 4240006 | 班级ID。 |
| feature | String |  | JSON格式，各个角色下存在不同属性。 |
| isAdviser |  |  | 是否班主任，老师角色下有效。 |
| studentNo |  |  | 学号，学生角色下有效。 |
| syncAction | String | edu\_user\_update | 事件类型。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 人员身份删除

**示例：**

```
{
    "EventType": "edu_user_delete",
    "corpId":"1233445556",
    "role":"guardian",
    "feature":"{}",
    "classId":4240006,
    "userId":"manager9707",
    "isGraduate":0
  }
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | 12233445 | 组织id。 |
| userId | String | manager9707 | 用户id。 |
| role | String | teacher | 此人在家校的角色类型。   - **teacher**：老师 - **guardian**：监护人 - **student**：学生 |
| classId | Number | 4240006 | 班级ID。 |
| isGraduate | Number | 0 | - **0**：正常的删除 - **1**：由于毕业业务导致的人员删除 |
| feature | String |  | 扩展，老师身份提前下有效。 |
| isAdviser | Integer | 1 | 是否班主任。只有在teacher的角色下有效。   - **0**：非班主任身份 - **1**：班主任身份 |

## 关系新增

**示例：**

```
{
    "EventType": "edu_user_relation_insert",
    "corpId":"1233445556",
    "fromUserId":"1591928760",
    "toUserId":"1592301514-87630",
    "classId":4240006,
    "relationName":"爸爸",
    "relationCode":"F"
  }
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | 1233445556 | 组织id。 |
| fromUserId | String | 1591928760 | 用户id。 |
| toUserId | String | 1592301514-87630 | 用户id。 |
| classId | Number | 4240006 | 班级ID。 |
| relationCode | String | F | 关系code。 |
| relationName | String | 爸爸 | 关系名。 |

## 人员关系更新

**示例：**

```
{
    "EventType": "edu_user_relation_update",
    "corpId":"1233445556",
    "fromUserId":"1591928760",
    "toUserId":"1592301514-87630",
    "classId":4240006,
    "relationName":"爸爸",
    "relationCode":"F"
  }
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | 1233445556 | 组织id。 |
| fromUserId | String | 1591928760 | 用户id。 |
| toUserId | String | 1592301514-87630 | 用户id。 |
| classId | Number | 4240006 | 班级ID。 |
| relationCode | String | F | 关系code。 |
| relationName | String | 爸爸 | 关系名。 |

## 人员关系删除

**示例：**

```
{
    "EventType": "edu_user_relation_delete",
    "corpId":"1233445556",
    "fromUserId":"1591928760",
    "toUserId":"1592301514-87630",
    "classId":4240006,
    "relationName":"爸爸",
    "relationCode":"F"
  }
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | 1233445556 | 组织id。 |
| fromUserId | String | 1591928760 | 用户id。 |
| toUserId | String | 1592301514-87630 | 用户id。 |
| classId | Number | 4240006 | 班级ID。 |
| relationCode | String | F | 关系code。 |
| relationName | String | 爸爸 | 关系名。 |

## 部门节点新增

**示例：**

```
{   
  "EventType":"edu_dept_insert",
  "corpId":"ding97d07b05aea229fe",
  "deptId":4288001
}
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | ding97d07b05aea229fe | 组织id。 |
| deptId | Number | 4288001 | 部门id。 |

## 部门节点更新

**示例：**

```
{   
  "EventType":"edu_dept_update",
  "corpId":"ding97d07b05aea229fe",
  "deptId":4288001
}
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | ding97d07b05aea229fe | 组织id。 |
| deptId | Number | 4288001 | 部门id。 |

## 部门节点删除

**示例：**

```
{
  "EventType":"edu_dept_delete",
  "isGraduate":0,
  "corpId":"ding97d07b05aea229fe",
  "deptId":4288001
}
```

**参数说明：**

| **名称** | **类型** | **示例** | **说明** |
| --- | --- | --- | --- |
| corpId | String | ding97d07b05aea229fe | 组织id。 |
| deptId | Number | 4288001 | 部门id。 |
| isGraduate | Number | 0 | - **0**：删除成功 - **1**：毕业 |
