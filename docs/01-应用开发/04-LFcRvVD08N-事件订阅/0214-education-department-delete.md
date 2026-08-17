---
title: "教育部门删除"
source_url: "https://open.dingtalk.com/document/development/education-department-delete"
namespace: "development"
slug: "education-department-delete"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 教育部门删除"
doc_id: "4mzC3n4jXV"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/education-department-delete
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 教育部门删除
> Updated: 2022-01-19 19:29:22

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
