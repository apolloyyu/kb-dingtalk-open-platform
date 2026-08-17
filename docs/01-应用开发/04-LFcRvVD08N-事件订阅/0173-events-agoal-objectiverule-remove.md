---
title: "Agoal删除目标规则事件"
source_url: "https://open.dingtalk.com/document/development/events-agoal-objectiverule-remove"
namespace: "development"
slug: "events-agoal-objectiverule-remove"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "Agoal > Agoal删除目标规则事件"
doc_id: "IG5C4xaopv"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-agoal-objectiverule-remove
> Path: 应用开发 / 事件订阅 / Agoal > Agoal删除目标规则事件
> Updated: 2022-01-19 19:29:22

# Agoal删除目标规则事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Agoal删除目标规则事件 |
| 英文名称 | agoal\_objectiveRule\_remove |

## 功能描述

Agoal删除目标规则事件：当用户在Agoal中删除目标规则时，会发送事件通知订阅方目标规则的信息，主要是用来给三方合作伙伴使用，合作伙伴接收事件以同步删除目标规则相关信息。

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
  "eventType": "agoal_objectiveRule_remove",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding23980uodfijladkfja",
    "bizid": "djk23894jfkleuid8djf",
    "eventTime": "1774522643",
    "body": {
      "objectiveRuleId": "68c8fxxxe4b0beb9547f45a4"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "agoal_objectiveRule_remove",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "ding23980uodfijladkfja",
  "bizid": "djk23894jfkleuid8djf",
  "eventTime": "1774522643",
  "body": {
    "objectiveRuleId": "68c8fxxxe4b0beb9547f45a4"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=460)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 460,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "ding23980uodfijladkfja",
    "syncAction": "agoal_objectiveRule_remove",
    "bizid": "djk23894jfkleuid8djf",
    "eventTime": "1774522643",
    "body": {
      "objectiveRuleId": "68c8fxxxe4b0beb9547f45a4"
    }
  }
}
```
