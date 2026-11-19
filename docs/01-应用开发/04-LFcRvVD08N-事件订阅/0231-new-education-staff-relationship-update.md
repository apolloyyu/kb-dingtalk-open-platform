---
title: "新教育人员关系更新"
source_url: "https://open.dingtalk.com/document/development/new-education-staff-relationship-update"
namespace: "development"
slug: "new-education-staff-relationship-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 新教育人员关系更新"
doc_id: "RclEujUMyU"
updated_at: "2025-08-28 19:47:42"
---

> Source: https://open.dingtalk.com/document/development/new-education-staff-relationship-update
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 新教育人员关系更新
> Updated: 2025-08-28 19:47:42

# 新教育人员关系更新

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 新教育人员关系更新 |
| 英文名称 | edu\_user\_relation\_update |

## 功能描述

家校通讯录2.0，人员变更推送。家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系。（目前关系只有监护人与学生的关系)。在某个班级中人员关系更新时，推送本事件。此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，${fromUserid}与${toUserid}的关系是 ${relationName}。在家校场景下，fromUserid为监护人，toUserid为学生。此回调事件推送的是最简单的数据，建议配合API查询详情。

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
- `data.classId`（long）：班级ID。
- `data.errmsg`（string）：返回码说明。
- `data.relationName`（string）：关系名。
- `data.fromUserid`（string）：用户id。
- `data.relationCode`（string）：关系code。
- `data.toUserid` （string）：用户id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "edu_user_relation_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "toUserid\t": "34567890",
    "classId": 4240006,
    "relationName": "妈妈",
    "fromUserid": "34567890",
    "relationCode": "M",
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
- `classId`（long，必填）：班级ID。
- `errmsg`（string，必填）：返回码说明。
- `relationName`（string，必填）：关系名。
- `fromUserid`（string，必填）：用户id。
- `relationCode`（string，必填）：关系code。
- `toUserid` （string，必填）：用户id。

### **事件体示例**

```
{
  "EventType": "edu_user_relation_update",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "errcode": 0,
  "toUserid\t": "34567890",
  "classId": 4240006,
  "relationName": "妈妈",
  "fromUserid": "34567890",
  "relationCode": "M",
  "errmsg": "ok"
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
- `biz_data.classId`（long）：班级ID。
- `biz_data.errmsg`（string）：返回码说明。
- `biz_data.relationName`（string）：关系名。
- `biz_data.fromUserid`（string）：用户id。
- `biz_data.relationCode`（string）：关系code。
- `biz_data.toUserid` （string）：用户id。

### **biz\_data数据示例(biz\_type=51)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 51,
  "biz_data": {
    "errcode": 0,
    "toUserid\t": "34567890",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "classId": 4240006,
    "relationName": "妈妈",
    "syncAction": "edu_user_relation_update",
    "fromUserid": "34567890",
    "relationCode": "M",
    "errmsg": "ok"
  }
}
```
