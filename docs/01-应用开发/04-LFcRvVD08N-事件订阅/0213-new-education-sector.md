---
title: "教育部门新增"
source_url: "https://open.dingtalk.com/document/development/new-education-sector"
namespace: "development"
slug: "new-education-sector"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 教育部门新增"
doc_id: "lohqkmi2s3"
updated_at: "2025-08-28 19:47:37"
---

> Source: https://open.dingtalk.com/document/development/new-education-sector
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 教育部门新增
> Updated: 2025-08-28 19:47:37

# 教育部门新增

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 教育部门新增 |
| 英文名称 | edu\_dept\_insert |

## 功能描述

家校通讯录2.0，部门信息变更。主要包括家校通讯录架构中各个部门发生变更时的信息,edu\_dept\_insert表示部门节点新增事件数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.nick`（string）：部门别名。
- `data.errcode`（integer）：返回码。
- `data.chain`（string）：从顶层部门到当前节点部门的部门链，其内容不包含当前节点。 如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区： []。
- `data.feature`（string）：部门feature，JSON格式。 各种节点部门存在不同的属性。
- `data.name`（string）：部门名称。
- `data.deptId`（long）：部门ID。
- `data.errmsg`（string）：返回码说明。
- `data.contactType`（string）：家校通讯录类型：  
  - classic: 传统经典4层结构。校区/学段/年级/班级。  
  - custom：自定义结构，但是叶子节点仍旧是班级。
- `data.deptType`（string）：部门类型：  
  - campus：校区/学院  
  - period：学段  
  - grade：年级  
  - class：班级  
  - dept：没有业务含义，只是一个部门节点。

### **事件体示例**

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

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `nick`（string）：部门别名。
- `errcode`（integer）：返回码。
- `chain`（string）：从顶层部门到当前节点部门的部门链，其内容不包含当前节点。 如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区： []。
- `feature`（string）：部门feature，JSON格式。 各种节点部门存在不同的属性。
- `name`（string）：部门名称。
- `dept_id`（long）：部门ID。
- `errmsg`（string）：返回码说明。
- `contact_type`（string）：家校通讯录类型：  
  - classic: 传统经典4层结构。校区/学段/年级/班级。  
  - custom：自定义结构，但是叶子节点仍旧是班级。
- `dept_type`（string）：部门类型：  
  - campus：校区/学院  
  - period：学段  
  - grade：年级  
  - class：班级  
  - dept：没有业务含义，只是一个部门节点。

### **事件体示例**

```
{
  "EventType": "edu_dept_insert",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "nick": "苹果班",
  "errcode": 0,
  "chain": "[123,456]",
  "contact_type": "classic",
  "feature": "{\"grade_level\":0,\"start_year\":\"2023\"}",
  "name": "一年级2班（苹果班）",
  "errmsg": "ok",
  "dept_type": "grade",
  "dept_id": 123456
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.nick`（string）：部门别名。
- `biz_data.errcode`（integer）：返回码。
- `biz_data.chain`（string）：从顶层部门到当前节点部门的部门链，其内容不包含当前节点。 如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区： []。
- `biz_data.feature`（string）：部门feature，JSON格式。 各种节点部门存在不同的属性。
- `biz_data.name`（string）：部门名称。
- `biz_data.dept_id`（long）：部门ID。
- `biz_data.errmsg`（string）：返回码说明。
- `biz_data.contact_type`（string）：家校通讯录类型：  
  - classic: 传统经典4层结构。校区/学段/年级/班级。  
  - custom：自定义结构，但是叶子节点仍旧是班级。
- `biz_data.dept_type`（string）：部门类型：  
  - campus：校区/学院  
  - period：学段  
  - grade：年级  
  - class：班级  
  - dept：没有业务含义，只是一个部门节点。

### **biz\_data数据示例(biz\_type=50)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 50,
  "biz_data": {
    "nick": "苹果班",
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "chain": "[123,456]",
    "contact_type": "classic",
    "feature": "{\"grade_level\":0,\"start_year\":\"2023\"}",
    "syncAction": "edu_dept_insert",
    "name": "一年级2班（苹果班）",
    "errmsg": "ok",
    "dept_type": "grade",
    "dept_id": 123456
  }
}
```
