---
title: "新教育人员关系新增"
source_url: "https://open.dingtalk.com/document/development/new-education-staff-relations-added"
namespace: "development"
slug: "new-education-staff-relations-added"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 新教育人员关系新增"
doc_id: "Ji2ONU954E"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/new-education-staff-relations-added
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 新教育人员关系新增
> Updated: 2022-01-19 19:29:22

# 新教育人员关系新增

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 新教育人员关系新增 |
| 英文名称 | edu\_user\_relation\_insert |

## 功能描述

家校通讯录2.0，人员变更推送。家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系。（目前关系只有监护人与学生的关系)。 该事件表示在某个班级中人员关系新增。此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，${fromUserid}与${toUserid}的关系是 ${relationName}。在家校场景下，fromUserid为监护人，toUserid为学生。此回调事件推送的是最简单的数据，建议配合API查询详情。

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
  "eventType": "edu_user_relation_insert",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": "0",
    "classId": 4240006,
    "relationName": "爸爸",
    "fromUserid": "1591928760",
    "relationCode": "F",
    "errmsg": "ok",
    "toUserid": "1592301514-87630"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "edu_user_relation_insert",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "errcode": "0",
  "classId": 4240006,
  "relationName": "爸爸",
  "fromUserid": "1591928760",
  "relationCode": "F",
  "errmsg": "ok",
  "toUserid": "1592301514-87630"
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
    "errcode": "0",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "classId": 4240006,
    "relationName": "爸爸",
    "syncAction": "edu_user_relation_insert",
    "fromUserid": "1591928760",
    "relationCode": "F",
    "errmsg": "ok",
    "toUserid": "1592301514-87630"
  }
}
```
