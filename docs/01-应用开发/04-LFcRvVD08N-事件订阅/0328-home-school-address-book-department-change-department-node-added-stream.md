---
title: "家校通讯录部门变更(部门节点新增)"
source_url: "https://open.dingtalk.com/document/development/home-school-address-book-department-change-department-node-added-stream"
namespace: "development"
slug: "home-school-address-book-department-change-department-node-added-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录部门变更(部门节点新增)"
doc_id: "uhnRKEYC2J"
updated_at: "2025-10-16 15:06:48"
---

> Source: https://open.dingtalk.com/document/development/home-school-address-book-department-change-department-node-added-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录部门变更(部门节点新增)
> Updated: 2025-10-16 15:06:48

# 家校通讯录部门变更(部门节点新增)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 家校通讯录部门变更(部门节点新增) |
| 英文名称 | edu\_dept\_insert |

## 功能描述

家校通讯录2.0，部门信息变更。主要包括家校通讯录架构中各个部门发生变更时的信息,eventType为edu\_dept\_insert，表示部门节点新增事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `nick`（string）：部门别名。
- `errcode`（integer）：返回码。
- `chain`（string）：从顶层部门到当前节点部门的部门链，其内容不包含当前节点。 如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区： []。
- `feature`（string）：部门feature，JSON格式。 各种节点部门存在不同的属性。
- `name`（string）：部门名称。
- `deptId`（long）：部门ID。
- `errmsg`（string）：返回码说明。
- `contactType`（string）：家校通讯录类型：  
  - classic: 传统经典4层结构。校区/学段/年级/班级。  
  - custom：自定义结构，但是叶子节点仍旧是班级。
- `deptType`（string）：部门类型：  
  - campus：校区/学院  
  - period：学段  
  - grade：年级  
  - class：班级  
  - dept：没有业务含义，只是一个部门节点。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "edu_dept_insert",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "nick": "苹果班",
    "errcode": 0,
    "chain": "[123,456]",
    "feature": "{\"grade_level\":0,\"start_year\":\"2023\"}",
    "name": "一年级2班（苹果班）",
    "deptId": 123456,
    "errmsg": "ok",
    "contactType": "classic",
    "deptType": "grade"
  }
}
```
