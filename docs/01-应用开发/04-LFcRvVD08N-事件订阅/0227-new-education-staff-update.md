---
title: "新教育人员更新"
source_url: "https://open.dingtalk.com/document/development/new-education-staff-update"
namespace: "development"
slug: "new-education-staff-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 新教育人员更新"
doc_id: "UySsQyAyoX"
updated_at: "2025-08-28 19:47:40"
---

> Source: https://open.dingtalk.com/document/development/new-education-staff-update
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 新教育人员更新
> Updated: 2025-08-28 19:47:40

# 新教育人员更新

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 新教育人员更新 |
| 英文名称 | edu\_user\_update |

## 功能描述

家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。教育人员更新事件表示在某个班级中人员相关身份更新触发的事件推送的数据。

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
- `data.classId`（long）：班级ID。
- `data.role`（string）：此人在家校的角色类型：  
  - teacher：老师角色  
  - guardian：监护人角色  
  - student：学生角色
- `data.unionid`（string）：unionid, 无手机号的学生为""。
- `data.feature`（string）：各个角色下存在不同属性，JSON格式。
- `data.name`（string）：此人在此班级的名字。
- `data.errcode`（integer）：返回码。
- `data.errmsg`（string）：返回码说明。
- `data.userid`（string）：用户的userid。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "edu_user_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "classId": 12345,
    "role": "guardian",
    "unionid": "FzyqbxFafVOEExxxwiEiE",
    "feature": "{}",
    "name": "小明爸爸",
    "errmsg": "ok",
    "userid": "123344"
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
- `classId`（long）：班级ID。
- `role`（string）：此人在家校的角色类型：  
  - teacher：老师角色  
  - guardian：监护人角色  
  - student：学生角色
- `unionid`（string）：unionid, 无手机号的学生为""。
- `feature`（string）：各个角色下存在不同属性，JSON格式。
- `name`（string）：此人在此班级的名字。
- `errcode`（integer，必填）：返回码。
- `errmsg`（string）：返回码说明。
- `userid`（string）：用户的userid。

### **事件体示例**

```
{
  "EventType": "edu_user_update",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "errcode": 0,
  "classId": 12345,
  "role": "guardian",
  "unionid": "FzyqbxFafVOEExxxwiEiE",
  "feature": "{}",
  "name": "小明爸爸",
  "errmsg": "ok",
  "userid": "123344"
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
- `biz_data.classId`（long）：班级ID。
- `biz_data.role`（string）：此人在家校的角色类型：  
  - teacher：老师角色  
  - guardian：监护人角色  
  - student：学生角色
- `biz_data.unionid`（string）：unionid, 无手机号的学生为""。
- `biz_data.feature`（string）：各个角色下存在不同属性，JSON格式。
- `biz_data.name`（string）：此人在此班级的名字。
- `biz_data.errcode`（integer）：返回码。
- `biz_data.errmsg`（string）：返回码说明。
- `biz_data.userid`（string）：用户的userid。

### **biz\_data数据示例(biz\_type=51)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 51,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "classId": 12345,
    "role": "guardian",
    "unionid": "FzyqbxFafVOEExxxwiEiE",
    "feature": "{}",
    "syncAction": "edu_user_update",
    "name": "小明爸爸",
    "errmsg": "ok",
    "userid": "123344"
  }
}
```
