---
title: "教育部门删除"
source_url: "https://open.dingtalk.com/document/development/education-department-delete"
namespace: "development"
slug: "education-department-delete"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 教育部门删除"
doc_id: "4mzC3n4jXV"
updated_at: "2025-08-28 19:47:39"
---

> Source: https://open.dingtalk.com/document/development/education-department-delete
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 教育部门删除
> Updated: 2025-08-28 19:47:39

# 教育部门删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 教育部门删除 |
| 英文名称 | edu\_dept\_delete |

## 功能描述

家校通讯录2.0，部门信息变更。主要包括家校通讯录架构中各个部门发生变更时的信息,该事件为部门节点删除事件数据。

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
- `data.errcode`（integer）：返回码。
- `data.deptId`（long）：部门节点ID。
- `data.isGraduate`（integer）：- 0：表示正常的删除。  
  - 1：表示毕业。
- `data.errmsg`（string）：返回码说明。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "edu_dept_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "isGraduate": 0,
    "deptId": 12345,
    "errmsg": "ok"
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
- `errcode`（integer，必填）：返回码。
- `dept_id`（long，必填）：部门节点ID。
- `is_graduate`（integer，必填）：- 0：表示正常的删除。  
  - 1：表示毕业。
- `errmsg`（string，必填）：返回码说明。

### **事件体示例**

```
{
  "EventType": "edu_dept_delete",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "errcode": 0,
  "errmsg": "ok",
  "dept_id": 12345,
  "is_graduate": 0
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
- `biz_data.errcode`（integer）：返回码。
- `biz_data.dept_id`（long）：部门节点ID。
- `biz_data.is_graduate`（integer）：- 0：表示正常的删除。  
  - 1：表示毕业。
- `biz_data.errmsg`（string）：返回码说明。

### **biz\_data数据示例(biz\_type=50)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 50,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "edu_dept_delete",
    "errmsg": "ok",
    "dept_id": 12345,
    "is_graduate": 0
  }
}
```
