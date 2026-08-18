---
title: "新教育人员关系删除"
source_url: "https://open.dingtalk.com/document/development/new-education-staff-relation-delete"
namespace: "development"
slug: "new-education-staff-relation-delete"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 新教育人员关系删除"
doc_id: "NwYG7sD0ds"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/new-education-staff-relation-delete
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 新教育人员关系删除
> Updated: 2022-01-19 19:29:22

# 新教育人员关系删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 新教育人员关系删除 |
| 英文名称 | edu\_user\_relation\_delete |

## 功能描述

家校通讯录2.0，人员变更推送。家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系。（目前关系只有监护人与学生的关系)。 在某个班级中人员关系删除，推送此事件。此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，${fromUserid}与${toUserid}的${relationName}关系删除。在家校场景下，fromUserid为监护人，toUserid为学生。

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
  "eventType": "edu_user_relation_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "classId": 4240006,
    "relationName": "妈妈",
    "fromUserid": "34567890",
    "relationCode": "M",
    "errmsg": "ok",
    "toUserid": "34567890"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "edu_user_relation_delete",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "errcode": 0,
  "classId": 4240006,
  "relationName": "妈妈",
  "fromUserid": "34567890",
  "relationCode": "M",
  "errmsg": "ok",
  "toUserid": "34567890"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=51)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 51,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "classId": 4240006,
    "relationName": "妈妈",
    "syncAction": "edu_user_relation_delete",
    "fromUserid": "34567890",
    "relationCode": "M",
    "errmsg": "ok",
    "toUserid": "34567890"
  }
}
```
